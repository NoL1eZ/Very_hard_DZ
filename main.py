import pprint
import requests
import sys
import json

response = requests.get("https://akabab.github.io/superhero-api/api/all.json")
response.text
# print(response.text)
with open('heroes.json') as f:
    json_data = json.load(f)



class Hero:
    def __init__(self, name):
        self.name = name
        self.intelligence = 0

    def get_intelligence(self):
        intelligence = 0
        for heroes in json_data:
            if self.name == heroes["name"]:
                intelligence = heroes["powerstats"]["intelligence"]
                self.intelligence += intelligence
        return self.intelligence

hero1 = Hero("Hulk")
hero2 = Hero("Captain America")
hero3 = Hero("Thanos")
print(hero1.get_intelligence())
print(hero2.get_intelligence())
print(hero3.get_intelligence())

if hero1.intelligence > hero2.intelligence and hero1.intelligence >hero3.intelligence:
    print("самый умный -", hero1.name)
elif hero2.intelligence > hero1.intelligence and hero2.intelligence >hero3.intelligence:
    print("самый умный -", hero2.name)
else:
    print("самый умный -", hero3.name)
