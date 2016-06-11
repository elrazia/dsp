#The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

# The below skeleton is optional.  You can use it or you can write the script with an approach of your choice.


import pandas as pd
# import csv as dataframe
goals_df = pd.read_csv('football.csv')

# create column for goal differential
goals_df['Goal Diff'] = goals_df['Goals'] - goals_df['Goals Allowed']

# find smallest goal differential in table, and the row it is in
answer = min(abs(goals_df['Goal Diff']))
abs(goals_df['Goal Diff']) == answer

# index dataframe and print team name
print goals_df.ix[7]['Team']
