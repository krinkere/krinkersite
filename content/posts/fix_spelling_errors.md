Title: How to remove typos from entity names via fuzzywuzzy module in python.
Date: 2018-03-30 11:44
Modified: 2018-03-30 11:44
Status: published
Category: How To article
Tags: python
Slug: fix_spelling_errors
Authors: Al Krinker
Summary: Remove typos by leveraging fuzzywuzzy module in python

While cleaning data in csv file, it is often common to see entity name such 
as city, person name, organization, etc being misspelled a little slightly and 
hence not producing same type of statistic as you might want. For example, 
let's say that you try to collect stats on number of times user accessed your page.
In that user name can be entered manually or it provided by different systems, 
then it might be different slight. Here I mean that we need to ensure that
case is the same not to throw our stats and any spaces are cleaned as well
just as a prelim step. Also, the username might be slightly misspelled with an
extra dash, space or single character. Here lays the danger though, there
can we two usernames that vary just by a character. I remember the days of hotmail
and that you would often get emails sent to blackwolf to your black.wolf account.
Gmail saw this as a problem and now it ignores periods in the emails to avoid this
issue. What I am trying to say is that you need to use typos with care. Now how you do it?

First of all, clean the text from spaces and make it lowercased.

```python
import pandas as pd

# read in our dataset
df = pd.read_csv("my_data.csv")
# convert to lower case
df['username'] = df['username'].str.lower()
# remove trailing white spaces
df['username'] = df['username'].str.strip()

# let's take a look at list of unique usernames values
username = df['username'].unique()

# sort them alphabetically and then take a closer look
username.sort()
print(username)
```

We should see some usernames that seem too close of a match... let's 
try to find all usernames that are more that 90% close to each other 
and replace them to the most common name

```python
import fuzzywuzzy

# function to replace rows in the provided column of the provided dataframe
# that match the provided string above the provided ratio with the provided string
def replace_matches_in_column(df, column, string_to_match, min_ratio = 90):
    # get a list of unique strings
    strings = df[column].unique()
    
    # get the top 10 closest matches to our input string
    matches = fuzzywuzzy.process.extract(string_to_match, strings, 
                                         limit=10, scorer=fuzzywuzzy.fuzz.token_sort_ratio)

    # only get matches with a ratio > 90
    close_matches = [matches[0] for matches in matches if matches[1] >= min_ratio]

    # get the rows of all the close matches in our dataframe
    rows_with_matches = df[column].isin(close_matches)

    # replace all rows with close matches with the input matches 
    df.loc[rows_with_matches, column] = string_to_match
    
    # let us know the function's done
    print("All done!")
```

Now you can call it as such

```python
# use the function we just wrote to replace close matches to "d.i khan" with "d.i khan"
replace_matches_in_column(df=df, column='username', string_to_match="black.wolf")
```

All done!