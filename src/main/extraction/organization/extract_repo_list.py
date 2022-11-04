import json
import os
import requests

# setup owner name , access_token, and headers 
owner='google-research'
access_token='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' # change later
headers = {'Authorization':"Bearer "+access_token, "Accept" : "application/vnd.github+json"}



repos=[]
for page_num in range(1,20):
    try:
    # to find all the repos' names from each page
        print("Extracting Page Number: ", page_num)
        url=f"https://api.github.com/users/{owner}/repos?page={page_num}" 
        repo=requests.get(url,headers=headers).json()
        repos.append(repo)
    except:
        repos.append(None)

all_repo_names=[]
for page in repos:
    for repo in page:
        try:
            all_repo_names.append(repo['full_name'].split("/")[1])
        except:
            pass
print(len(all_repo_names))

output_obj = {"org_name" : owner, "repo_list" : all_repo_names}

with open("metadata/extraction/repoList.json", "w") as f:
    json.dump(output_obj, f, indent=4)

