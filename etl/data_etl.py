import pandas as pd
import sqlite3

# read csv
df = pd.read_csv('source/game_events.csv')

# create connect
conn = sqlite3.connect('source/jdbc:sqlite:identifier.sqlite')

# Write data into the table
df.to_sql('game_events', conn, if_exists='replace', index=False)

# commit && close connect
conn.commit()
conn.close()

