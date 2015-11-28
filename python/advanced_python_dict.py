import pandas as pd
import numpy as np
import re

df = pd.read_csv('faculty.csv', header=0)
df.rename(columns=lambda x:x.strip(),inplace=True)

#Cleaning
df['titleobj'] = df['title'].map(lambda x: re.match(r'(.*?)? (of|is) Biostatistics',x).group(1))
df['degree'] = df['degree'].map(lambda x: x.strip())

def dictionary_build(key):
    d = {}
    a = []
    for i in range(0,len(df[key])):
        a.append(df['degree'][i])
        a.append(df['titleobj'][i])
        a.append(df['email'][i])
        try:
            b = d[df[key][i]]
            b.append(a)
            d[df[key][i]] = b
        except KeyError:
            d[df[key][i]] = [a]
        a = []
    return d

###Question 6
df['lastname'] = df['name'].map(lambda x: re.match(r'.* (.*)',x).group(1))



d = dictionary_build('lastname')
three_keys = {k:d[k] for k in sorted(d.keys())[:3]}
print three_keys


###Question 7
#Create column of names as tuples without middle initial
def dictionary_build_unique(key):
    d = {}
    a = []
    for i in range(0,len(df[key])):
        a.append(df['degree'][i])
        a.append(df['titleobj'][i])
        a.append(df['email'][i])
        d[df[key][i]] = a
        a=[]
    return d

df['noinitial'] = df['name']
for i in range(len(df['name'])):
    match_obj = re.match(r'(.*?) (.*\s)?(.*)',df['name'][i])
    if '.' in match_obj.group(1):
        df['noinitial'][i] = (match_obj.group(2),match_obj.group(3))
    else:
        df['noinitial'][i] = (match_obj.group(1),match_obj.group(3))

d = dictionary_build_unique('noinitial')
# three_keys = {k:d[k] for k in sorted(d.keys(), key = lambda x: x[0])[:3]}
three_keys = sorted(d.keys(), key = lambda x: x[0])[:3]

def print_keys(three_keys):
    for i in range(len(three_keys)):
        print 'Key:',three_keys[i],'Value:',d[three_keys[i]],'<br/>'

print_keys(three_keys)

###Question 8
three_keys = sorted(d.keys(), key = lambda x: x[1])[:3]
print_keys(three_keys)
