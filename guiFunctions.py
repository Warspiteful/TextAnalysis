from textAnalysis import textAnalyst, json
from timeAnalysis import timeAnalyst

def get_users(file_name):
    users = []
    with open(file_name, 'r+', encoding='utf-8') as f:
        file = json.load(f)
    for message in file['messages']:
        if message.get('from') not in users:
            users.append(message.get('from'))
    return users
