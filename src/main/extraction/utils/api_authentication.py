import os

def requests_access():
    access_token = os.environ["github_access_token"]

    if access_token == None or access_token == "":
        print("Please provide your access token in the env variable - github_access_token")

    owner='google-research'
    headers = {'Authorization':"Bearer "+access_token, "Accept" : "application/vnd.github+json"}

