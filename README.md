# Mood
This is a small backend REST API that allows users to post their mood values and
see their posting streak.
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
