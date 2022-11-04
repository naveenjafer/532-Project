import json
import os
import requests
import sys

from extraction.utils.api_authentication import requests_access


def main(inputRepoMetaFile, outputRepoUserFile):
    with open(inputRepoMetaFile) as f:
        inputRepoMetaFileData = json.load(f)
    
    repoNames = inputRepoMetaFileData["repo_list"]

    repoNameContributors = {}
    for repo_name in repoNames:
        print("Extracting contributors for: ", repo_name)
        url = f"https://api.github.com/repos/{requests_access.owner}/{repo_name}/contributors"
        # make the request and return the json
        contributors= requests.get(url,headers=requests_access.headers).json()
        repoNameContributors[repo_name] = contributors
    
    output_obj = {
        "org_name" : requests_access.owner,
        "repo_contributors" : repoNameContributors
    }

    with open(outputRepoUserFile, "w") as f:
        json.dump(output_obj, f, indent=4)

if __name__ == "__main__":
    inputRepoMetaFile = sys.argv[1]
    outputRepoUserFile = sys.argv[2]
    main(inputRepoMetaFile, outputRepoUserFile)