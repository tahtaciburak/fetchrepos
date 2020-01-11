#!/usr/bin/python3
import requests
import argparse


def get_public_repo_names(username,exclude_forks):
    response = requests.get("https://api.github.com/users/"+username+"/repos")
    repos = response.json()
    urls = []
    for repo in repos:
        if exclude_forks:
            if not repo["fork"]:
                urls.append(repo["html_url"])
        else:
            urls.append(repo["html_url"])
    return urls

def parse_arguments():
    parser = argparse.ArgumentParser(description="A tool for downloading all public repositories of a user.")
    parser.add_argument("-u", "--username", required=True,help="Username for fetching repos.")
    parser.add_argument("-e", "--exclude-forks", action="store_true", help="Ignore forks.")
    parser.add_argument("-o", "--output", required=True,help="Generate report when download finish.")
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    import os
    
    args = parse_arguments()
    output_path = args.output
    urls = get_public_repo_names(args.username, args.exclude_forks)
    try:
        os.mkdir(output_path)
    except:
        pass
    if len(urls)>1:
        for url in urls:
            os.system("git clone "+url + " "+ output_path+"/"+url.split("/")[-1])