# Be careful, the reson why i made them 2 seperate files is because when i ran the orignal file, it crashed my pc (i still dont know why it did that)

from github import Github
import requests
import json

# To get the apikey, go to newsapi website and make an account
egypt = "https://newsapi.org/v2/top-headlines?country=eg&apiKey=APIKEY"

ego = requests.get(egypt)

# Convert data to dict
egy = json.loads(ego.text)
 
# Convert dict to string
egy = json.dumps(egy)

g = Github("GITHUB_TOKEN")
# or  g = github.Github(login, password)

repo = g.get_user().get_repo("ahmedkmh.github.io")
file1 = repo.get_contents("assets/EgyptNews.json")

# update
repo.update_file(file1.path, "updating egypt news", egy, file1.sha)

input("enter")