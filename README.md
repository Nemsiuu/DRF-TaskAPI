# DRF-TaskAPI

created with django rest framework

# Description

DRF API TaskList, users can create, update, delete their tasks. They can also see a list of users and their tasks. Admin can create users and edit every task.
Used SessionAuthentication to authenticate users before they can do anything relevant.

# End Points

* /admin - admin panel
* /api-auth/login/?next=/ - login view for users
* '' -  List of tasks dedicated to logged in user ( Or all tasks if user is admin )
* /< pk > - See details, update, delete your task with id=pk
* /users/ - list of users
* /users/<int:user_id>/ - Details of user with id = user_id, all of his tasks in a list
* /users/<int:user_id>/<int:pk>/ - See details, update, delete task of a user

# Installation

* Install MySQL: v8.0 — https://dev.mysql.com/downloads/mysql/
* Install Git
* Install Pip
* ( Optionally ) create virtual environment and activate it
* Clone the repository - git clone https://github.com/Nemsiuu/DRF-TaskAPI.git
* run pip install -r requirements.txt inside directory
* Create new database in MySQL CLI - CREATE DATABASE IF NOT EXISTS zadania;
* run - python manage.py migrate
* create superuser - python manage.py createsuperuser
* run server - python manage.py runserver

  
              
