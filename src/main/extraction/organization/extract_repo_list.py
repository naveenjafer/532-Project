import json
import os
import requests
import sys
#sys.path.insert(1, '../extraction/utils.api_authentication')
from src.main.extraction.utils.api_authentication import consts, dummy_util


repos=[]
for page_num in range(1,20):
    if True:
        # to find all the repos' names from each page
        print("Extracting Page Numbers: ", page_num)
        url=f"https://api.github.com/orgs/{consts['owner']}/repos?page={page_num}" 
        print(url)
        print(consts["headers"])
        repo=requests.get(url,headers=consts["headers"]).json()
        repos.append(repo)
        print(repos)
        quit(1)
    else:
        repos.append(None)

all_repo_names=[]
for page in repos:
    for repo in page:
        try:
            all_repo_names.append(repo['full_name'].split("/")[1])
        except:
            pass
print(len(all_repo_names))

output_obj = {"org_name" : consts["owner"], "repo_list" : all_repo_names}

with open("metadata/extraction/repoList.json", "w") as f:
    json.dump(output_obj, f, indent=4)

