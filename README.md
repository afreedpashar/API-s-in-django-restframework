## Table of Contents

- [Project Description]
- [Features]
- [prerequisites]
- [getting started]

  
#Project Description

* RESTful API using the HTTP methods GET, POST, PUT, PATCH, and DELETE. In your project, you've encapsulated these functionalities within a class, providing a structured and organized approach to handling API requests. The implementation includes well-defined API endpoints and serializers, emphasizing best practices in web development.
* By incorporating a class-based approach,project exhibits modularity and maintainability, making it easy to extend and enhance functionality in the future. The utilization of serializers highlights the commitment to data validation and transformation, ensuring that incoming and outgoing data adheres to predefined standards.
* The API endpoints serve as the entry points for clients to interact with the application, each corresponding to a specific HTTP method. This design promotes a clear and intuitive interface for developers consuming the API. The inclusion of endpoints for GET, POST, PUT, PATCH, and DELETE operations reflects a comprehensive coverage of CRUD (Create, Read, Update, Delete) functionality, providing a robust foundation for various application scenarios.


## Features
* views.py file  where the logic is build to run the Api's.
* models.py file where database fields are present to interact with the databse and to store the data.
* urls..py file where all the urls are present those are nothing but API end points.
* settings.py file where all the settings are done such adding the app name in installed apps etc.
* serialzers.py file added the required files ,used the model serializers to get the fields from models.py file
  converting queryset to json or xml form.

  ### Prerequisites
* Create a virtual environment out the project and inside the folder for creating python virtual environment write a
  command "python -m venv environment_name".
* After creating virtual environment make sure to activate it command-"virtual\Scripts\activate"
* Install few python packages:
* pip install django
* pip install djangorestframework
* make sure to migrate 

## Getting Started
* Once you are done with the prerequisites run the command - "python manage.py runserver" to check whether your server 
is running.
* Use  the api endpoints to run the api example "http://127.0.0.1:8000/studentapi/" you will land on page where you will
  get post,get,put,patch and delete methods choose either of them and run the api.
