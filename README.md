# fetchrepos
[![Build Status](https://travis-ci.org/tahtaciburak/fetchrepos.svg?branch=master)](https://travis-ci.org/tahtaciburak/fetchrepos)
This project aims to download all the repositories of an Github user. It's very useful for organizing all your projects in one directory. You can download all the public repositories of a user by running following command.
```bash
fetchrepos --username <YOUR_GITHUB_USERNAME> --output-path <OUTPUT_PATH>
```

## Installation
You can install fetchrepos by running following command
```bash
git clone https://github.com/tahtaciburak/fetchrepos
sudo chmod +x fetchrepos
sudo cp fetchrepos /usr/local/bin
```

## Usage
```bash
usage: fetchrepos.py [-h] -u USERNAME -o OUTPUT [-e]

fetchrepos: A tool for downloading all public repositories of a user.

optional arguments:
  -h, --help            show this help message and exit
  -u USERNAME, --username USERNAME
                        Username for fetching repos.
  -o OUTPUT, --output OUTPUT
                        Destination path for your download.
  -e, --exclude-forks   Ignore forks, download repositories that created by
                        user
```

## Examples

```bash
# This will download all public projects of user tahtaciburak
fetchrepos --username tahtaciburak --output my_projects

 # This will.
fetchrepos --username tahtaciburak --output my_projects --exclude-forks
```
## Contributing
If you have some ideas about fetchrepos please feel free to open PR or issue.