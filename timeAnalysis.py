import json
import numpy as np
import matplotlib.pyplot as plt
from fileNames import json_files
import ntpath

class timeAnalyst:
    
    #Goal:
    #Dictionary of Messages:
    #Each message should have user, year, month, day, time
    def __init__(self, json_file):
        with open(json_file,encoding="utf8") as f:
            data = json.load(f)
        self.data = self.create_data(data["messages"])
        self.text_name = ntpath.basename(json_file)
    
    def create_data(self, data):
        data_dict = []
        for text in data:
            message = {}
            message['user'] = text.get('from')
            message['year'] = int(text.get('date')[:4]) 
            message['month'] = int(text.get('date')[5:7])
            message['day'] = int(text.get('date')[8:10])
            data_dict.append(message) 
        return data_dict

    def count_messages(self):
        users = {}
        for message in self.data:
            if message['user'] not in users.keys():
                users[message['user']] = 1
            else:
                users[message['user']] += 1
        return users, "Messages broken down by sender"

    def monthly_breakdown(self, found_year):
        months = ["Jan","Feb","Mar","Apr","May", "Jun", "Jul", "Aug", "Sept","Oct","Nov","Dec"]
        storage = [0]*12
        for message in self.data:
            if(message['year'] == found_year):
                storage[message['month']-1] += 1
        return dict(zip(months, storage)), "Breakdown by Month for " + str(found_year) 
    
    def day_breakdown(self, month):
        months = ["Jan","Feb","Mar","Apr","May", "Jun", "Jul", "Aug", "Sept","Oct","Nov","Dec"]
        day_dict = {}
        for message in self.data:
            if message['month'] == (month+1):
                if message['day'] in day_dict.keys():
                    day_dict[message['day']] += 1
                else:
                    day_dict[message['day']] = 1
        sorted_days = sorted(day_dict)
        sorted_resuts = [day_dict[index] for index in sorted_days]

        return dict(zip(sorted_days,sorted_resuts)), "Days in " + months[month]
    
    def season_breakdown(self):
        seasons = {'winter':0, 'spring': 0, 'summer':0, 'fall':0}
        for message in self.data:
            if message['month'] == 12 or message['month'] <= 2:
                seasons['winter'] += 1
            elif 3 <= message['month'] <= 5:
                seasons['spring'] += 1
            elif 6 <= message['month'] <= 8:
                seasons['summer'] += 1
            else:
                seasons['fall'] += 1
        return seasons, "Seasons"

    def create_graph(self, data):
        height = data[0].values()
        bars = data[0].keys()
        

        plt.suptitle(data[1] + " from " + self.text_name)
        
        y_pos = np.arange(len(bars))

        # Create bars
        plt.bar(y_pos, height)
 
        # Create names on the x-axis
        plt.xticks(y_pos, bars)
    
        # Show graphic
        plt.show()

ta = timeAnalyzer(json_files[2])

ta.create_graph(ta.count_messages())
