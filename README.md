# DWP Digital Code Test - Kwasi
### Brief 
Using the language of your choice please build your own API which calls the API at [https://bpdts-test-app.herokuapp.com/](https://bpdts-test-app.herokuapp.com/), and returns people who are listed as either living in London, or whose current coordinates are within 50 miles of London.

## Technology Used and Installs
This API was built using Python/Django framework.

### To Run
From root directory, run the following command to pipevn shell to run server:

 - pipenv shell
 - pip install -r requirements.txt (to install all packages if needed)
 - python manage.py runserver

## How to use
After the server is up and running use http://localhost:8000/ with the following endpoint;

 - user/users/ (To retrieve all users)
 - user/nearlondon (To retrieve users with 50 miles from London)

Example

 - http://localhost:8000/user/nearlondon/
