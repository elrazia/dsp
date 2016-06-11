import pandas as pd
prof_df = pd.read_csv('faculty.csv')

# Question 1

uniques = {}
deg = []
for i in prof_df[' degree']:
    deg.append(i.split())

for i in deg:
    for j in i:
        j = j.replace('.','')
        if j in uniques:
            uniques[j] += 1
        else:
            uniques[j] = 1
print uniques

# Question 2

titles = {}
for i in prof_df[' title']:
    i = i.replace(' is ',' of ')
    if i in titles:
        titles[i] += 1
    else:
        titles[i] = 1
print titles

# Question 3

emails = []
for i in prof_df[' email']:
    emails.append(i)
print emails

# Question 4

domains = []
for email in emails:
    index = email.find('@')
    domains.append(email[index+1:])
print list(set(domains))
