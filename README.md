# CCD Placement Portal Usage Instructions

Welcome to the CCD Placement Portal.

## Instructions to run the website on a local machine:

- Ensure that you have a Functional Text Editor (Atom, Sublime Text, Notepad++ etc.) installed on your System

#### Install Anaconda/Miniconda/Python 

#### Install Django

To use virtual environment for installation of packages and then activate the environment:

	$ conda create --name environment_name 
	$ conda install package_name 
	$ conda activate environment_name

where environment_name is the name of the virtual environment and package_name is the name of the package 
Example: $ conda create --name DjangoEnv django 

#### Install Django Import Export 
	$ conda install -c conda-forge django-import-export  

## Run following commands:
	
	$ python manage.py migrate
	$ python manage.py makemigrations

### To login, create account using command:

	$ python manage.py createsuperuser

### Run website:

	$ python manage.py runserver





