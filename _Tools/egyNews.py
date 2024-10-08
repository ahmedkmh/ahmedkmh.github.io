# Be careful, the reson why i made them 2 seperate files is because when i ran the orignal file, it crashed my pc (i still dont know why it did that)

from github import Github
import requests
import json
import os

try:
    SOME_SECRET = os.environ["MEDIASTACK_TOKEN"]
except KeyError:
    SOME_SECRET = "Token not available!"

# To get the apikey, go to newsapi website and make an account
egypt = f"https://newsdata.io/api/1/news?apikey={SOME_SECRET}&country=eg"
print(egypt[0:44])

ego = requests.get(egypt)

# Convert data to dict
egy = json.loads(ego.text)
 
# Convert dict to string
egy = json.dumps(egy)

# opening the file in write only mode
f = open("assets/EgyptNews.json", "w")
# f is the File Handler
f.write(egy)
