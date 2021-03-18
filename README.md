# Mood
This is a small backend REST API that allows users to post their mood values and
see their streak.
--------------------------------------------------------------------------------
### How to run this application:

After cloning this git repository to your local computer: (you may also run this
in a virtual environment)

1. First, run the requirements.txt file in the directory to install all the
dependencies.

    If you are using pip, run   
    `pip install -r requirements.txt`  

    Alternatively, you can also download these dependencies manually:   

     ```
     Flask_RESTful==0.3.8
     Flask==1.1.2
     requests==2.25.1
     Flask_HTTPAuth==4.2.0
     ```

2. In the directory, run   

    `python mood.py`     or      `python3 mood.py`

    The application would now be running on http://127.0.0.1:5000/mood

3. To test the GET and POST methods and see what they return, run   

    `python test.py`      or      `python3 test.py`

    To add more tests, go to test.py and modify the code there.

--------------------------------------------------------------------------------
### Things I would do differently if this were a production application
If this were a production application that allows users post their mood values,
I would do several things differently:

1. **Structure**   

    As this assessment is only a small backend REST API, I only created one main file.
    If this were a full production application with both frontend and backend, I would
    utilize create more modules and files, organize the application with blueprints,
    and the overall application would have a structure like this:   

    |----moodapp/
    |     |----init.py
    |     |----db.py
    |     |----auth.py
    |     |----mood.py
    |     |----templates/
    |     |     |----base.html
    |     |     |----auth/
    |     |     |----mood/
    |     -----static/
    |----tests/
    |----venv/
    |----setup.py

2. **Authentication**   

    To keep this API to the backend and stateless, I only used HTTPBasicAuth for
    authentication. This basic authentication only asks for the username and
    password, and lets the user stay "logged in" if the user provides the correct
    credentials.   

    In a production application, I would make use of built-in features such as
    flask-login that, together with frontend HTML, renders login forms to users.   
    
    To protect user security, I would also use some kind of password hash (e.g.
    werkzeug) to ensure that we are not storing the actual password. I will also
    generate a token that expires after e.g. 30 minutes, so an inactive user does
    not stay logged in.


3. **Database**   

    As this is not yet a deployed service and only runs locally, I am only keeping
    track of the "current_user" on the local machine.

    If the application needed to handle more users:
    First of all, I would use a database such as flask_sqlalchemy, instead of a
    simple Python dictionary, so user data can be stored more permanently in a
    configurable database, instead of just in memory. Afterwards, I would also
    create user models in a models.py.
