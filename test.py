"""
Test program for mood REST API
--------------------------------------------------------------------------------
Emma Jin
03/17/2021
"""
import requests
from requests.auth import HTTPBasicAuth

USER_DATA = {
    "admin":{"pwd":"SecretPassword"},
    "Emma":{"pwd":"SecretPassword2"}
}

BASE = "http://127.0.0.1:5000/"

############################### ANONYMOUS USER #################################
# This part performs GET and POST for users who are not logged in
# Anonymous users may still POST mood values that are temporarily persisted,
# but cannot access any userful information with GET
def anonymous(mood):
    print("POST and GET without credentials")

    response = requests.post(BASE + "mood", {"mood": mood})
    print("Response of POST:", response.json())

    response = requests.get(BASE + "mood")
    print("Response of GET:", response.json())

############################### LOGGED IN USER #################################
# This part performs GET and POST for logged in users
# When logged in users POST a mood, it is stored and their streak is updated
# When they perform a GET, they will see the mood they last posted and their streak
def loggedin_user(username, password, mood):
    print("Log in as %s, POST and GET with credentials" % username)

    response = requests.post(BASE + "mood", {"mood": mood}, \
               auth=HTTPBasicAuth(username, password))
    print("Response of POST:", response.json())

    response = requests.get(BASE + "mood")
    print("Response of GET:", response.json())

########################## LOGGED IN USER: EMMA ################################
def main():
    # If we try to GET before POSTing anything
    print("------------------------GET before POSTing--------------------------")
    response = requests.get(BASE + "mood")
    print("Response of GET:", response.json())
    print()

    # Test POSTing and GETing for anonymous users (not logged in)
    print("--------------------------anonymous user----------------------------")
    anonymous(8)
    print()

    # Test POSTing and GETing when logged in as 'admin'
    print("---------------------------user 'admin'-----------------------------")
    loggedin_user('admin',USER_DATA['admin']['pwd'], 6)
    print()

    # Test POSTing and GETing when logged in as 'Emma'
    print("---------------------------user 'Emma'------------------------------")
    loggedin_user('Emma',USER_DATA['Emma']['pwd'], 10)
    print()

    # If we GET/POST again without credentials after logging in before, stay
    # logged in as the latest user
    print("-----------------------without credentials--------------------------")
    anonymous(8)


if __name__ == "__main__":
    main()
