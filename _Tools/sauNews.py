# Be careful, the reson why i made them 2 seperate files is because when i ran the orignal file, it crashed my pc (i still dont know why it did that)

from github import Github
import requests
import json

# To get the apikey, go to newsapi website and make an account
saudia = "https://newsapi.org/v2/top-headlines?country=sa&apiKey=APIKEY"

sao = requests.get(saudia)

# Convert data to dict
sau = json.loads(sao.text)
 
# Convert dict to string
sau = json.dumps(sau)

g = Github("GITHUB_TOKEN")
# or  g = github.Github(login, password)

repo = g.get_user().get_repo("ahmedkmh.github.io")
file2 = repo.get_contents("assets/SaudiaNews.json")

# update
repo.update_file(file2.path, "updating saudia news", sau, file2.sha)

input("enter")