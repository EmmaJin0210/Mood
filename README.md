# Mood
This is a small backend REST API that allows users to post their mood values and
see their streak.
--------------------------------------------------------------------------------
### How to run this application:

After cloning this git repository to your local desktop:

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
 utilize a structure like this:

2. **Authentication**
 To keep this API to the backend and stateless, I only used HTTPBasicAuth for
 authentication. This basic authentication only checks for

 To protect user security, I would also use some kind of password hash to ensure
 that we are not storing the actual password. I will also generate a token that
 expires after e.g. 30 minutes, so an inactive user does not stay logged in.

 As this is not yet a deployed service, I am only keeping track of the
 "current_user" on the local machine. If the application needed to handle more users:
 First of all, I would use a database such as SQLLite or MangoDB, instead of a
 simple Python dictionary.
