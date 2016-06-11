import pandas as pd
prof_df = pd.read_csv('faculty.csv')


# Question 6

# break dataframe into lists for names, surnames, degrees, titles, and emails.
faculty_dict = {}
names = []
for i in prof_df['name']:
    names.append(i.split())
surnames = [x[-1] for x in names]
degrees = [i for i in prof_df[' degree']]
titles = [i for i in prof_df[' title']]
emails = [i for i in prof_df[' email']]

# create stats variable which will correspond to values of the dictionary (degree, title, email)
stats = [list(x) for x in zip(degrees, titles, emails)]

# create dictionary by iteration using surname:stats as key:value format
for i in xrange(len(surnames)):
    if surnames[i] in faculty_dict:
        faculty_dict[surnames[i]] += [stats[i]]
    else:
        faculty_dict[surnames[i]] = [stats[i]]


# Question 7

# create list of tuples with (first name, last name) format and empty professor dict
first_last = [(x[0], x[-1]) for x in names]
professor_dict = {}

# create dictionary by iteration using first_last:stats as key:value format
for i in xrange(len(first_last)):
    if first_last[i] in professor_dict:
        professor_dict[first_last[i]] += [stats[i]]
    else:
        professor_dict[first_last[i]] = [stats[i]]


# Question 8

sorted(professor_dict.items(),key=lambda x: x[0][1])
