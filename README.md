# Project Awwwards 
A Django application that allows a user to post a project he/she has created and get it reviewed by his/her peers.

A project can be rated based on 3 different criteria

1. Design
2. Usability
3. Content

These criteria can be reviewed on a scale of 1-10 and the average score is taken.

### Demo
[The Nightngale Project Awwwards](https://thenightngale-project-awwwards.herokuapp.com/)]

### Author
[Florence Kotohoyoh](https://github.com/Flokots)

### User Stories
As a user, I would like to:

1. View posted projects and their details
2. Post a project to be rated/reviewed
3. Rate/ review other users' projects
4. Search for projects 
5. View projects overall score
6. View my profile page

### Technologies and Dependencies Used
* Django
* Python
* Heroku
  
### Project Setup
1. Clone this repository.
2. `cd` into the cloned repository.
3. Create a virtual environment
4. Install the dependencies using:
   ```
   pip install -r requirements.txt
   ```
5. Create the database
   ```
   $ python
   >>> psql;
   >>> CREATE DATABASE database_name;
   ```
6. In the `settings.py` update the database configurations.
7. Make initial migrations 
   ```
   python manage.py makemigrations main
   python manage.py manage.py migrate
   ```
8. Run `python manage.py runserver` to run the application locally. View the app on the `localhost:8000'
9. Run `python manage.py test main` to run the tests.
10. Have fun exploring!
  
### Contributions
Should you notice any bug or  want to add a feature, follow these steps to contribute:
1. Fork this repository.
2. Clone the forked repository.
3. Make changes.
4. Create a pull request.

### Known Bugs
Copy Link button not functional
### Contact
florencekotohoyoh@gmail.com
### License
[MIT](choosealicense.com/licenses/mit)
Copyright (c) 2022
