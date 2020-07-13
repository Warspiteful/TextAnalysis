import json, re, emoji
from fileNames import file1, text1, text2, name2, file2, text3, text4, name3

def write_file(file_path, name, text_path):
    writer = open(text_path,"a") 
    with open(file_path,encoding="utf8") as f:
        data = json.load(f)


    #List of Dictionaries
    data = data["messages"]
    texts = []

    emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U0001F1F2-\U0001F1F4"  # Macau flag
        u"\U0001F1E6-\U0001F1FF"  # flags
        u"\U0001F600-\U0001F64F"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U0001F1F2"
        u"\U0001F1F4"
        u"\U0001F620"
        u"\u200d"
        u"\u2640-\u2642"
        u"\uFFF0-\uFFFF"
        
        "]+", flags=re.UNICODE)


    for message in data:
        if message.get('from') == name:
            if type(message.get('text')) is not list:
                texts.append(message.get('text'))
    for text in texts:
        text = emoji_pattern.sub(r'',text)
        allchars = [str for str in text]
        emoji_list = [c for c in allchars if c in emoji.UNICODE_EMOJI]
        clean_text = ' '.join([str for str in text.split() if not any(i in str for i in emoji_list)])
        clean_text = clean_text.encode('utf-8').strip().decode()
        clean_text.strip("~")
        clean_text = emoji_pattern.sub(r'',clean_text)
        clean_text = re.sub(r'[^\x00-\x7F]+',' ', clean_text)
        writer.write(str((clean_text)))
        writer.write('\n')
    writer.close()
