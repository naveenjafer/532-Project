import json
import os
import requests
import sys

owner='google-research'
access_token='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' # change later
headers = {'Authorization':"Bearer "+access_token, "Accept" : "application/vnd.github+json"}

def main(inputRepoMetaFile, outputRepoUserFile):
    with open(inputRepoMetaFile) as f:
        inputRepoMetaFileData = json.load(f)
    
    repoNames = inputRepoMetaFileData["repo_list"]

    repoNameContributors = {}
    for repo_name in repoNames:
        print("Extracting contributors for: ", repo_name)
        url = f"https://api.github.com/repos/{owner}/{repo_name}/contributors"
        # make the request and return the json
        contributors= requests.get(url,headers=headers).json()
        repoNameContributors[repo_name] = contributors
    
    output_obj = {
        "org_name" : owner,
        "repo_contributors" : repoNameContributors
    }

    with open(outputRepoUserFile, "w") as f:
        json.dump(output_obj, f, indent=4)

if __name__ == "__main__":
    inputRepoMetaFile = sys.argv[1]
    outputRepoUserFile = sys.argv[2]
    main(inputRepoMetaFile, outputRepoUserFile)