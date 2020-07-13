# TextAnalysis
Text Analysis Program designed for Telegram-exported JSon files

## Files
`TextWriter.py` - Contains the `write_file()` command, which reads JSon files and writes the contents to a .txt file \
`analysis.py` - Contains the textAnalyst class, detailed below

## Text Analyst Class
Reads contents of a text file and returns patterns using `Counter` and `gensim` libraries
### Constructor 
```python
textAnalyst(user_file)
```
#### User File
User file can be linked to existing text files:
* Path to text file
* List of paths to text files

User file can also be linked to a json file with a provided user to look for and a path for a text file

#### Usage
```python
from analysis import textAnalyst

ta_example = textAnalyst('example.txt') #Reads from a text file
ta_multiple = textAnalyst(['example.txt','example2.txt']) #Reads from multiple text files
ta_json = textAnalyst(['text.json','user',"text_file.txt"]) #Writes all text from 'user' in .json to .txt and reads it
```

### Functions

* `most_frequent_words(n)` Returns the n most common words in the text 
* `return_most_similar(word, num)` Returns n words most similar to the provided word based on the provided text
* `set_text(user_file)` Sets the instance's text data to provided user file
* `print_word()` Prints out current text data


## Exporting From Telegram
From a chat, click on the three vertical dots in the upper right-hand corner. This will drop down a menu. \
![Image of Menu](https://i.imgur.com/QffDE6D.png) \
This will pull up the Chat Export Settings. Click on 'HTML'. \
![Image of Chat Export Settings](https://i.imgur.com/FzolMEa.png) \
Select the 'Machine-readable JSON' button from the provided menu and click save. \
![Image of format menu](https://i.imgur.com/DpHfTmu.png) \
This will bring you back to the Chat Export Settings. Note the path next to format. De-select any other export inclusions and press export. \
![Image of final menu](https://i.imgur.com/1bVTWFG.png) \
Upon successful export, you will be prompted to press 'Show My Data' as seen below. Select it. \
![Successful Export](https://i.imgur.com/mTdtgKa.png) \
This will pull up result.json file. Provide the path, including the 'result.json' to user_file along with the user and path to text file. 
![JSon File Location](https://i.imgur.com/KWISjOT.png)

