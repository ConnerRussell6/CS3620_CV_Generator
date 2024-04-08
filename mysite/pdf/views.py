from django.shortcuts import render, get_object_or_404
from .models import Profile
import pdfkit
from django.http import HttpResponse
from django.template import loader
import io


# Create your views here.
def accept(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        summary = request.POST.get('summary', '')
        degree = request.POST.get('degree', '')
        school = request.POST.get('school', '')
        university = request.POST.get('university', '')
        previous_work = request.POST.get('previous_work', '')
        skills = request.POST.get('skills', '')
        profile = Profile(name=name, email=email, phone=phone, summary=summary, degree=degree, school=school,
                          university=university, previous_work=previous_work, skills=skills)
        profile.save()
    return render(request, 'pdf/accept.html')


def resume(request, id):
    user_profile = Profile.objects.get(pk=id)
    template = loader.get_template('pdf/resume.html')
    html = template.render({'user_profile': user_profile})
    options = {
        'page-size': 'Letter',
        'encoding': 'UTF-8'
    }
    pdf = pdfkit.from_string(html, False, options)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="resume.pdf"'

    return response

# def resume(request, id):
#     # Get the Profile object with the given id or return a 404 error if it doesn't exist
#     user_profile = get_object_or_404(Profile, pk=id)
#
#     # Load the template and render it with the user_profile data
#     template = loader.get_template('pdf/resume.html')
#     html = template.render({'user_profile': user_profile})
#
#     # PDFKit options
#     options = {
#         'page-size': 'Letter',
#         'encoding': 'UTF-8'
#     }
#
#     # Specify the path to the wkhtmltopdf executable
#     config = pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin')
#
#     # Generate PDF from the HTML content
#     pdf = pdfkit.from_string(html, False, options=options, configuration=config)
#
#     # Prepare the HTTP response with the PDF content
#     response = HttpResponse(pdf, content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="resume.pdf"'  # Set filename for download
#
#     return response


def list(request):
    profiles = Profile.objects.all()
    return render(request, 'pdf/list.html', {'profiles': profiles})
