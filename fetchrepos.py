#!/usr/bin/python3
import os
import requests
import argparse
from multiprocessing.pool import ThreadPool
from itertools import repeat

def get_public_repo_names(username,exclude_forks):
    try:
        response = requests.get("https://api.github.com/users/"+username+"/repos")
    except requests.exceptions.ConnectionError:
        print("Failed to connect GitHub check your internet connection.")
        exit(-1)
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
    parser = argparse.ArgumentParser(description="fetchrepos: A tool for downloading all public repositories of given user.")
    parser.add_argument("-u", "--username", required=True,help="Username for fetching repos.")
    parser.add_argument("-o", "--output", required=True,help="Destination path for your download.")
    parser.add_argument("-e", "--exclude-forks", action="store_true", help="Ignore forks, download repositories that created by user")
    args = parser.parse_args()
    return args

def start_download(url, output_path):
    try:
        os.system("git clone "+url + " "+ output_path+"/"+url.split("/")[-1])
    except:
        print("Git client error. Check your git installation via 'git --version'")
        exit(1)

def create_output_path(output_path):
    try:
        if not os.path.isdir(output_path):
            os.mkdir(output_path)
    except:
        print("Failed to create directory.")
        exit(1)

if __name__ == "__main__":    
    args = parse_arguments()
    output_path = args.output
    urls = get_public_repo_names(args.username, args.exclude_forks)
    create_output_path(output_path)
    t_pool = ThreadPool(4)
    results = t_pool.starmap(start_download, zip(urls,repeat(output_path)))

    t_pool.close()
    t_pool.join()
