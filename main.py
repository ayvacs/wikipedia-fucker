import json
import requests

f = open("config.json")
config = json.load(f)
f.close()

f = open("newcontent.txt")
newcontent = f.read()
f.close()


def make_post():
    print("req")

for i in range(2):
    make_post()