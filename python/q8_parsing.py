#The football.csv file contains the results from the English Premier League.
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of
# goals scored for and against each team in that season (so Arsenal scored 79 goals
# against opponents, and had 36 goals scored against them). Write a program to read the file,
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

# The below skeleton is optional.  You can use it or you can write the script with an approach of your choice.


import csv

def read_data(data):
    csv_file = csv.reader(open(data,'rb'))
    header = csv_file.next()

    array_data = []
    for row in csv_file:
       array_data.append(row)
    return array_data

def get_min_score_difference(parsed_data):
    temp_data = []
    temp_row = []
    for data in parsed_data:
        temp_row.append(data[0])
        temp_row.append(int(data[5])-int(data[6]))
        temp_data.append(temp_row)
        temp_row = []
    return temp_data

def get_team(parsed_data):
    parsed_data = sorted(parsed_data, key = lambda x: abs(x[1]))
    return parsed_data[0][0]

if __name__ == '__main__':
    print get_team(get_min_score_difference(read_data('football.csv'))),"is the team with the smallest difference in 'for' and 'against' goals."
