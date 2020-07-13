import json

class timeAnalyzer:
    
  
    def __init__(self, json_file):
        with open(json_file,encoding="utf8") as f:
            data = json.load(f)

        self.data = data["messages"]
    
    def count_messages(self):
        users = {}
        for message in self.data:
            if message.get('from') not in users.keys():
                users[message.get('from')] = 1
            else:
                users[message.get('from')] += 1
        return users


ta = timeAnalyzer('../Carolette.json')
