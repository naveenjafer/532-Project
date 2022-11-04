import os

access_token = os.environ["github_access_token"]

consts = {
    "owner":'google-research',
    "headers": {"Authorization":"Bearer " + access_token, "Accept" : "application/vnd.github+json"}
}

def dummy_util():
    ...

    

