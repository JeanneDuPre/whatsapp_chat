import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re
import string
import emoji


# Function to find emojis in a given text
def find_emojis(text):
    emojis = [c for c in text if c in emoji.distinct_emoji_list(c)]
    return emojis

# Function to count all emojis in a given text
def count_emojis(text):
    emojis = [c for c in text if c in emoji.distinct_emoji_list(c)]
    return len(emojis)

# Function to count unique emojis in a list
def count_unique_emojis(lst):
    unique_emojis = set()
    for emoji in lst:
        if emoji not in unique_emojis:
            unique_emojis.add(emoji)
    return len(unique_emojis)

# Function to remove emojis in the text column
def remove_emojis(text):
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)

## CLEANING column 'Text'
def basic_cleaning(sentence):
    sentence = sentence.strip() # remove whitespaces
    sentence = sentence.lower() # lowercase
    sentence = ''.join(char for char in sentence if not char.isdigit()) # remove digits
    for punctuation in string.punctuation:  # remove punctuation
        sentence = sentence.replace(punctuation, ' ') 
    return sentence

                                ################## MAIN FUNCTION ######################
def get_data():
    #load the datatset
    df = pd.read_csv("whatsapp_data.csv")
    # create a new column named 'Date 2'
    df['Date2'] = pd.to_datetime(df['Date'], format='%d.%m.%y').dt.strftime('%Y-%m-%d')
    # create a new column named 'Year'
    df['Year'] = pd.to_datetime(df['Date2']).dt.year
    # create a new column named 'Month'
    df['Month'] = pd.to_datetime(df['Date2']).dt.month
    # create a new column named 'Grouped_Time'
    df['Grouped_Time'] = df['Time'].str.replace(r'(\d{2}):(\d{2})', r'\1:00')
    # Extract the day of the week in a new column
    df['Day_of_Week'] = df['Date2'].dt.day_name()
    # remove whitespace from column 'Name'
    df['Name'] = df['Name'].str.strip()

    # select only the data from 2017 until 2022
    df = df[df['Year']!=2023]
    
    # Apply the find_emojis function to the 'Text' column
    df['Emojis'] = df['Text'].apply(find_emojis)
    # Apply the count_emojis function to the 'Text' column
    df['EmojiCount'] = df['Text'].apply(count_emojis)  
    # Apply the count_unique_emojis function to the column
    df['EmojiCountdifferent'] = df['Emojis'].apply(count_unique_emojis)
    # Create new columns for each emoji and count their occurrences
    emojis = set([emoji for row in df['Emojis'] for emoji in row])  # Get unique emojis in the column

    for emoji in emojis:
        df[f'{emoji}_Count'] = df['Emojis'].apply(lambda x: emoji in x)
    df = df*1
    
    # Remove emojis
    df['TextohneEmojis'] = df['Text'].apply(remove_emojis)
    ## Clean the Text
    df['Text_cleaned']= df['TextohneEmojis'].apply(basic_cleaning)
    ## Create new columns 'letter_count' and 'word_count'
    df['letter_count']= df['Text_cleaned'].apply(lambda s: len(s))
    df['word_count']= df['Text_cleaned'].apply(lambda s: len(s.split(' ')))
    return df

                ################## MAIN FUNCTION FOR STEPHIE AND JANINE ######################

def get_data_stephie(df):
    # select only the stephie rows
    df_stephie = df[df['Name'] == "Stephie"]
    return df_stephie

def get_data_janine(df):
    # select only the stephie rows
    df_janine = df[df['Name'] == "Janine"]
    return df_janine
