import pandas as pd
from pandasql import sqldf


df = pd.read_csv('movies.csv')

print(sqldf("select * from df where genres like '%test'; DROP TABLE movies; --%'"))