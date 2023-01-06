# Be careful, the reson why i made them 2 seperate files is because when i ran the orignal file, it crashed my pc (i still dont know why it did that)

from github import Github
import requests
import json
import os

try:
    SOME_SECRET = os.environ["SOME_SECRET"]
except KeyError:
    SOME_SECRET = "Token not available!"

# To get the apikey, go to newsapi website and make an account
saudia = f"https://newsapi.org/v2/top-headlines?country=sa&apiKey={SOME_SECRET}"

sao = requests.get(saudia)

# Convert data to dict
sau = json.loads(sao.text)
 
# Convert dict to string
sau = json.dumps(sau)

# opening the file in write only mode
f = open("assets/EgyptNews.json", "w")
# f is the File Handler
f.write(sau)