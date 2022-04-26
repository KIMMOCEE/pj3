import pandas as pd

csvfiles = ['data.csv', 'data_w_genres.csv', 'data_by_year.csv', 'data_by_genres.csv', 'data_by_artist.csv']

df1=pd.read_csv('../pj3/data/data.csv')
df1.columns = [c.lower() for c in df1.columns]

df2=pd.read_csv('../pj3/data/data_w_genres.csv')
df2.columns = [c.lower() for c in df2.columns]

df3=pd.read_csv('../pj3/data/data_by_year.csv')
df3.columns = [c.lower() for c in df3.columns]

df4=pd.read_csv('../pj3/data/data_by_genres.csv')
df4.columns = [c.lower() for c in df4.columns]

df5=pd.read_csv('../pj3/data/data_by_artist.csv')
df5.columns = [c.lower() for c in df5.columns]


from sqlalchemy import create_engine
engine = create_engine('postgresql://efmracyk:1hYnXxAk8VZGELKywxKh342B1QeW2aUD@arjuna.db.elephantsql.com/efmracyk')

df1.to_sql("data", engine)
df2.to_sql("data_w_genres", engine)
df3.to_sql("data_by_year", engine)
df4.to_sql("data_by_genres", engine)
df5.to_sql("data_by_artist", engine)