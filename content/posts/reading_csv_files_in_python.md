Title: How to detect encoding of CSV file in python
Date: 2018-03-30 9:27
Modified: 2018-03-30 9:27
Status: published
Category: How To article
Tags: python
Slug: encoding_csv_file_python
Authors: Al Krinker
Summary: How to read CSV file in python and detect its encoding

In my line of work, I have to deal with a lot of spreadsheets coming 
my way with different type of data. I don't control these csv files, hence
I never know how they are being generated. If I were to simply read
the file, I would often get something like that.

```commandline
UnicodeDecodeError Traceback (most recent call last)
    pandas/_libs/parsers.pyx in pandas._libs.parsers.TextReader._convert_tokens()
    pandas/_libs/parsers.pyx in pandas._libs.parsers.TextReader._convert_with_dtype()
    pandas/_libs/parsers.pyx in pandas._libs.parsers.TextReader._string_convert()
    pandas/_libs/parsers.pyx in pandas._libs.parsers._string_box_utf8()

UnicodeDecodeError: 'utf-8' codec can't decode byte 0x99 in position 11: invalid start byte
```

Basically, when you specify the following, you assume that the information
was encoded in UTF-8 ()default) format 

```python
data = pd.read_csv("my_data.csv")
```

However, if that's not the case and format is not UTF-8 then you get a nasty error 
shown previously. What to do? Try manually some common encoders, or look at the file
and try to figure it out? <br/>
A much better way is to use chardet module to do it for you. Here we going to 
read first ten thousand bytes to figure out the encoding type. Note that chardet
is not 100% accurate and you would actually see the level of confidence of 
encoder detection as part of chardet output. But it is still better than guessing manually.

```python
# look at the first ten thousand bytes to guess the character encoding
with open("my_data.csv", 'rb') as rawdata:
    result = chardet.detect(rawdata.read(10000))

# check what the character encoding might be
print(result)
```

The result is

```commandline
{'encoding': 'Windows-1252', 'confidence': 0.73, 'language': ''}
```

So chardet is 73% confidence that the right encoding is "Windows-1252".  Now we can use
this data to specify encoding type as we trying to read the file

```python
data = pd.read_csv("my_data.csv", encoding='Windows-1252'))
```

No errors! 