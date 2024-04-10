CV Generator using Django
This project is a simple web application built with Django that allows users to create and download their CVs in PDF format. Users can input their information into a form, which is then stored in a database. The application utilizes wkhtmltopdf to convert the HTML template into a PDF document.

Features
User-friendly interface for inputting CV information.
Database storage for user data.
Conversion of CVs into PDF format for easy download.
Simple and intuitive workflow.
Prerequisites
Before running this project, ensure that you have the following installed:

Python 3.x
Django
wkhtmltopdf
You can install wkhtmltopdf by following the instructions on the official website.

Installation
Clone the repository to your local machine:
bash
Copy code
git clone https://github.com/your-username/cv-generator-django.git
Navigate into the project directory:
bash
Copy code
cd cv-generator-django
Install the required Python packages:
bash
Copy code
pip install -r requirements.txt
Run migrations to create the necessary database tables:
bash
Copy code
python manage.py migrate
Start the Django development server:
bash
Copy code
python manage.py runserver
Visit http://localhost:8000 in your web browser to access the application.
Usage
Enter your CV information into the provided form fields.
Click on the "Generate PDF" button to create your CV in PDF format.
Once generated, click on the "Download PDF" link to download your CV.
