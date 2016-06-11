import pandas as pd

# create dataframe from list
email_df = pd.DataFrame(emails)

# write dataframe into csv
email_df.to_csv('emails.csv', index=False)
