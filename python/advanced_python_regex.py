import pandas as pd
import numpy as np
import re


### QUESTION 1:
def list_degrees(data):
    data_f = data['degree'].str.replace('.','')
    data_f = data_f.str.split()
    data_l = data_f.tolist()
    final_list = []
    for i in data_l:
        for j in i:
            final_list.append(j)

    return final_list

def num_degrees(degree_list):
    return len(set(degree_list))

def count_degrees(degree_list):
    return {x:degree_list.count(x) for x in set(degree_list)}



df = pd.read_csv('faculty.csv', header=0)
df.rename(columns=lambda x:x.strip(),inplace=True)

degree_list = list_degrees(df)
print 'The number of unique degrees including no degree is', num_degrees(degree_list)
print count_degrees(degree_list)

#df['PhD'] = df['degree'].map(lambda x: re.search(r'Ph\.?[d,D]',x)).astype(bool)

###Question 2:
df['titleobj'] = df['title'].map(lambda x: re.match(r'(.*?)? (of|is) Biostatistics',x).group(1))
print 'The number of unique titles is', len(set(df['titleobj']))
print df['titleobj'].value_counts()

###Question 3:
print df['email'].tolist()

###Question 4:
df['domains'] = df['email'].map(lambda x: re.match(r'.*?@(.*)',x).group(1))
print 'The number of unique email domains is', len(set(df['domains']))
print df['domains'].value_counts()
