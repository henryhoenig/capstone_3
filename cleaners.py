import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
import string
import re
from itertools import combinations

def load_tweets(csv_filename):
    ''' takes in csv of tweets, 
    strips unwanted cols (for this case) '''
    
    df = pd.read_csv(csv_filename)
    df.drop(columns=['time', 'photos', 'video', 'timezone', 'place', 'language', 
                     'cashtags', 'thumbnail', 'near', 'geo', 'source', 'user_rt_id', 
                     'user_rt', 'retweet_id', 'retweet_date', 'translate', 
                     'trans_src', 'trans_dest'], inplace=True)
    return df
    

    
def clean_hashtags(df_col):
    ''' each row in hashtags column is a single string
    takes in the hashtags of each tweet,
    returns cleaned text (list of strings)
    NOTE: Unnecessary if putting into df: use
    hashtags_to_df instead''' 

    columnSeriesObj = df_col
    tweets = columnSeriesObj
    
    master_list = []
    for i in tweets:
        words = i.split()
        table = str.maketrans('', '', string.punctuation)
        i = [w.translate(table) for w in words]
        i = " ".join(i)
        i = i.lower()
        i = re.sub(r'[^a-zA-Z0-9_\s]+', '', i)
        master_list.append(i)
        
    hashtags_df = pd.DataFrame(master_list, columns=['text'])
    
    return hashtags_df



def hashtags_to_df(df_col):
    ''' takes hashtags from dataframe column, strips all 
    punctuation, eliminates all tweets with only one hashtag, 
    creates list of lists of remaining, puts into dataframe ''' 
    
    columnSeriesObj = df_col
    tags = columnSeriesObj
    
    master_list = []
    for i in tags:
        i = i.replace("[", "")
        i = i.replace("]", "")
        i = i.replace("'", "")
        i = i.replace(",", "")
        i = i.split(' ')
        if len(i) < 2:
            continue
        else:
            i_list = []
            for j in i:
                i_list.append(j)
            master_list.append(i_list)

    hashtags_df = pd.DataFrame(master_list)
    
    return hashtags_df


# returns list of hashtag edges based on co-occurences

def get_hashtag_edges(df_of_hashtags):

    edges_df = pd.DataFrame([None, None])
    for index, row in df_of_hashtags.iterrows():
        hold = [x for x in row.values if x == x]
        edges = (list(combinations(hold, 2)))    
        edges_series=pd.Series(edges)
        new_edges_df = pd.DataFrame(edges_series)
        edges_df = edges_df.append(new_edges_df, ignore_index=True)
    edges_df.rename(columns={0 : 'edges'}, inplace=True)

    return edges_df



# consolidates duplicates (with reverse order), adds up weights, puts into new dataframe

def consolidate_edges(top_edges_df):

    edges_dict = {}
    for index, row in top_edges_df.iterrows():
        tup = row[0]
        weight = row[1]
        reverse_tup = tup[::-1]
        if tup not in edges_dict and reverse_tup not in edges_dict:
            edges_dict[tup] = weight
        if reverse_tup in edges_dict:
            edges_dict[reverse_tup] = edges_dict[reverse_tup] + weight

    new_top_edges = pd.DataFrame(list(edges_dict.items()), columns = ['edges','weight'])
    
    return new_top_edges





def clean_tweet_text(df_col):
    ''' takes in the body of each tweet
    returns cleaned text''' 
    
    columnSeriesObj = df_col
    tweets = columnSeriesObj
    
    master_list = []
    for i in tweets:
        words = i.split()
        table = str.maketrans('', '', string.punctuation)
        i = [w.translate(table) for w in words]
        i = " ".join(i)
        i = i.lower()
        i = re.sub(r'[^a-zA-Z0-9_\s]+', '', i)
        master_list.append(i)
        
    tweets_df = pd.DataFrame(master_list, columns=['text'])
    
    return tweets_df




def make_single_string(df_col):
    ''' creates one string of all pre-cleaned tweets
    df_col parameter should be from df returned by 
    clean_tweet_text ('text' is col header)''' 
    
    columnSeriesObj = df_col
    tweets = columnSeriesObj
    
    master_list = []
    for i in tweets:
        master_list.append(i)
    
    single_string_list = []
    master_string = " ".join(master_list)
    single_string_list.append(master_string)
    
    return single_string_list


def make_mentions_list(df_col):
    
    columnSeriesObj = df_col
    mentions = columnSeriesObj
    
    master_mentions_list = []
    for i in mentions:          # i is single string, sometimes containing only [], sometimes multiple entries
        i = i.split("}, ")      # splits by entry (each entry is dict of len 3); 
                                # empty i or i with only one name won't get split, will filter
        if len(i) < 2:          # ie, if didn't split because only one entry, skip
            continue
        else:
            name_list = []      # moved up from new creation for each j (this likely biggest problem): ie, under "for j in i"
            for j in i:         # i is still list of multiple mentions, with j as each element of list a single FULL entry
                j = j.split(", ") # splits each entry j between screen name half and name half
                j = j[1].replace("'", "")    # assigns name half of j to j, stripping some punctuation
                j = j.replace(":", "")       # more cleaning of punctuation
                j = j.split("name ")         # now splits "name half" of j btween "name " and actual name, 
                                            # creating new 2-element list
                name = j[1]                  # assigns name to second element of new list (actual name) 
                name_list.append(name)       # should contain all names mentioned in a given tweet (original i in mentions)
        master_mentions_list.append(name_list) # once all names in single entry appended to name_list, 
                                                # this list appended to master, then return to outer for loop
                                                # in test case, there should be two lists 
                                                # (only two tweets in first 10 contained more than one mention)
            
    return master_mentions_list