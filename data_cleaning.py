import pandas as pd
import json
import pymongo

#########################   read orignal csv file    ###########################
csv_file = "lib/data/googleplaystore.csv"
df_app = pd.read_csv(csv_file)
columns_to_drop = ['Reviews','Type','Genres','Last Updated','Current Ver']


# #########################   deal with file   #############################
df_app.drop(columns_to_drop, inplace=True, axis=1)
df_app.fillna(0,inplace=True)
df_app['App'] = df_app['App'].apply(lambda x: x.replace(' ','_') )
df_app['App'] = df_app['App'].apply(lambda x:  x.replace('.','_'))
df_app['Size'] = df_app['Size'].apply(lambda x:  int(float(x[:-1])*1000) if 'M' in x  else int(float(x[:-1])) if 'k' in x else -1)
df_app.drop(df_app.loc[df_app['Size']==-1].index, inplace=True)
df_app['Installs'] = df_app['Installs'].apply(lambda x: int(x[:-1].replace(',','')) if int(x[:-1].replace(',',''))>=5000 else -1)
df_app.drop(df_app.loc[df_app['Installs']==-1].index, inplace=True)
df_app['Price'] = df_app['Price'].apply(lambda x: float(x[1:]) if '$' in x else float(x) if x=='0' else -1)
df_app.drop(df_app.loc[df_app['Price']==-1].index, inplace=True)
df_app['Content Rating'] = df_app['Content Rating'].apply(lambda x: 1.0 if x=='Everyone' else 1.5 if x=='Everyone 10+' else 2.0 if x=='Teen' else 3.0 if x=='Mature 17+' else -1)
df_app.drop(df_app.loc[df_app['Content Rating']==-1].index, inplace=True)
df_app['Android Ver'] = df_app['Android Ver'].apply(lambda x: str(x[:-7]) if 'and up' in str(x) else -1)
df_app.drop(df_app.loc[df_app['Android Ver']==-1].index, inplace=True)


#########################   set dataframe   #############################
df_app.set_index('App', inplace=True)
df_app.reset_index(level=0, inplace=True)
df_app.index.name='seq'
df_app.index=df_app.index.map(str)
json_app = df_app.to_dict(orient='index')

################   connect mongodb and store json in it   ##################

client=pymongo.MongoClient('mongodb://Felix:felix123@ds131510.mlab.com:31510/googleapp')
db_app=client.googleapp
if 'google' not in db_app.collection_names(include_system_collections=False):
    db_app['google'].insert(json_app)