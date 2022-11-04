import json
import os
import requests
import sys
#sys.path.insert(1, '../extraction/utils.api_authentication')
from extraction.utils.api_authentication import requests_access

repos=[]
for page_num in range(1,20):
    try:
        # to find all the repos' names from each page
        print("Extracting Page Number: ", page_num)
        url=f"https://api.github.com/users/{requests_access.owner}/repos?page={page_num}" 
        repo=requests.get(url,headers=requests_access.headers).json()
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

output_obj = {"org_name" : requests_access.owner, "repo_list" : all_repo_names}

with open("metadata/extraction/repoList.json", "w") as f:
    json.dump(output_obj, f, indent=4)

