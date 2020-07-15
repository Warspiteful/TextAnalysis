# TextAnalysis
Text Analysis Program designed for Telegram-exported JSON files

## Files

`textAnalysis.py` - Contains the [textAnalyst class](#text-analyst-class) \
`timeAnalysis.py` - Contains the [timeAnalyst class](#time-analyst-class)\
`GUI.py` - Contains the [GUI class](#gui-class) \
`stopwords.txt` - contains custom stopwords read through [textAnalyst functions](#stopword-handling) 

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

User file can also be linked to a JSON file with a provided user to look for and a path for a text file

#### Usage
```python
from analysis import textAnalyst

ta_example = textAnalyst('example.txt') #Reads from a text file
ta_multiple = textAnalyst(['example.txt','example2.txt']) #Reads from multiple text files
ta_json = textAnalyst(['text.json','user',"text_file.txt"]) #Writes all text from 'user' in .json to .txt and reads it
```

### Functions
#### Data Handling
* `write_file(file_path, name, text_path)` Reads a JSON file and writes all text from user `name` to .txt file
* `read_file(file_name)` Opens and returns the text from a .txt file 
* `process(text)` Cleans and breaks up text into tokens 
* `append_text(user_file)` Parses file input and appends text data to model 
* `remove_text_file(file_name)` Removes file_name from the model data and refreshes text data


#### Text Analysis
* `most_frequent_words(n)` Returns the n most common words in the text 
* `return_most_similar(word, num)` Returns n words most similar to the provided word based on the provided text
* `find_favorite_pos(pos)` Returns the most used word associated with the given part-of-speech

#### Stopword Handling
* `set_stopwords()` Creates, if it does not exist, and reads custom stopwords from 'stopwords.txt'.
* `get_stopwords()` Returns all stopwords in the model

### Printing Functions
* `print_text_files()` Prints all text files currently in model data 
* `print_word()` Prints text data
* `print_processed()` Prints all tokenized text data

## Time Analyst Class
Reads contents of JSON files and creates graphs based on statistics

### Constructor 
```python
timeAnalyst(json_file)
```

#### User File
User file is exclusively a path to a JSON file

#### Usage
```python
from timeanalysis import timeAnalyst

ta_example = timeAnalyst('example.json') #Reads from a JSON file
```

### Functions

#### Data Handling
* `create_data(data)` Creates the data set from which the rest of the functions pull from (user, year, month, day)
* `create_graph(data)` Creates a bar graph to visualize data returned by data analysis functions

#### Data Analysis
* `count_messsages()` Returns dict of users to number of messages they sent
* `monthly_breakdown(found_year)` Returns the a dict of months to messages sent during that period for given year `found_year`
* `day_breakdown(month)` Returns a dict of days to messages sent on that given day for given month `month`
* `season_breakdown()` Returns a dict of seasons to messages sent in that given season



## GUI Class
Created to handle both Time Analyzer and Text Analyzer in a user-friendly and accessible Guided User Interface

### Constructor
```python
from GUI import GUI

GUI_example = GUI()
```
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
This will pull up result.json file. Provide the path, including the 'result.json' to user_file along with the user and path to text file. \
![JSon File Location](https://i.imgur.com/KWISjOT.png)

## Release History
* 0.1.0 - Minimum Viable Product: TextAnalyzer Class 
