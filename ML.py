import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.utils import shuffle
import pickle


def print_dataframe(dataframe, print_column=True, print_rows=True):
    if print_column:
        print(",".join([column for column in dataframe]))
    if print_rows:
        for index, row in dataframe.iterrows():
            print(",".join([str(row[column]) for column in dataframe]))


def clean(dataframe):
    category_mapping = {'ART_AND_DESIGN': 1, 
                        'AUTO_AND_VEHICLES': 2,
                        'BEAUTY': 3,
                        'BOOKS_AND_REFERENCE': 4,
                        'BUSINESS': 5,
                        'COMICS': 6,
                        'COMMUNICATION': 7,
                        'DATING': 8,
                        'EDUCATION': 9,
                        'ENTERTAINMENT': 10,
                        'EVENTS': 11,
                        'FINANCE': 12,
                        'FOOD_AND_DRINK': 13,
                        'HEALTH_AND_FITNESS': 14,
                        'HOUSE_AND_HOME': 15,
                        'LIBRARIES_AND_DEMO': 16,
                        'LIFESTYLE': 17,
                        'GAME': 18,
                        'FAMILY': 19,
                        'MEDICAL': 20,
                        'SOCIAL': 21,
                        'SHOPPING': 22,
                        'PHOTOGRAPHY': 23,
                        'SPORTS': 24,
                        'TRAVEL_AND_LOCAL': 25,
                        'TOOLS': 26,
                        'PERSONALIZATION': 27,
                        'PRODUCTIVITY': 28,
                        'PARENTING': 29,
                        'WEATHER': 30,
                        'VIDEO_PLAYERS': 31,
                        'NEWS_AND_MAGAZINES': 32,
                        'MAPS_AND_NAVIGATION': 33}
    rating_mapping = {'Everyone': 0, 
                      'Teen': 13, 
                      'Everyone 10+': 10, 
                      'Mature 17+': 17, 
                      'Adults only 18+': 18, 
                      'Unrated': -1}
    dataframe = dataframe.copy()
    columns_to_drop = ['Type', 'Genres', 'Last Updated', 'Current Ver']
    dataframe.drop(columns_to_drop, inplace=True, axis=1)
    dataframe = dataframe[pd.notnull(dataframe['Rating'])]
    dataframe.reset_index(drop=True, inplace=True)
    dataframe['App'] = dataframe['App'].str.replace( ' ', '_' )
    dataframe['Android Ver'] = dataframe['Android Ver'].str.replace('Varies with device', '0.0')
    dataframe['Android Ver'] = dataframe['Android Ver'].str.replace(' and up', '')
    dataframe['Android Ver'] = dataframe['Android Ver'].str.extract(r'^(\d.\d)', expand=False)
    dataframe['Size'] = dataframe['Size'].str.replace('M', '')
    dataframe['Size'] = dataframe['Size'].str.replace('Varies with device', '0')
    dataframe['Size'] = dataframe['Size'].apply(lambda x: '1' if 'k' in x else x)
    dataframe['Price'] = dataframe['Price'].str.replace('$', '')
    dataframe = dataframe.replace({'Category': category_mapping})
    dataframe = dataframe.replace({'Content Rating': rating_mapping})
    dataframe['Category'] = dataframe['Category'].fillna(0)
    dataframe['Rating'] = dataframe['Rating'].fillna(0)
    dataframe['Reviews'] = dataframe['Reviews'].fillna(0)
    dataframe['Size'] = dataframe['Size'].fillna(0)
    dataframe['Installs'] = dataframe['Installs'].fillna(0)
    dataframe['Price'] = dataframe['Price'].fillna(0)
    dataframe['Content Rating'] = dataframe['Content Rating'].fillna(0)
    dataframe['Android Ver'] = dataframe['Android Ver'].fillna(0) 
    return dataframe


def load_app(dataframe, split_percentage):
    dataframe = shuffle(dataframe)
    app_x = dataframe.drop(['App','Installs'], axis=1).values
    app_y = dataframe['Installs'].values
    split_point = int(len(app_x) * split_percentage)
    app_X_train = app_x[:split_point]
    app_y_train = app_y[:split_point]
    app_X_test = app_x[split_point:]
    app_y_test = app_y[split_point:]
    return app_X_train, app_y_train, app_X_test, app_y_test


def train_and_test(persent = 1):
    csv_file = 'googleplaystore_latest.csv'
    dataframe = pd.read_csv(csv_file)
    dataframe = clean(dataframe)
    print_dataframe(dataframe, True, False)
    dataframe.to_csv('Dataset_1.csv', sep=',', encoding='utf-8')
    app_X_train, app_y_train, app_X_test, app_y_test = load_app(dataframe, split_percentage = persent)
    knn = KNeighborsClassifier()
    knn.fit(app_X_train, app_y_train)
    save_file = 'trained_model.sav'
    pickle.dump(knn, open(save_file, 'wb'))


def prediction(category, rating, reviews, size, price, content_rating,android_ver,save_file = 'trained_model.sav'):
    knn_load = pickle.load(open(save_file, 'rb'))
    pred = knn_load.predict([[category, rating, reviews, size, price, content_rating, android_ver]])
    dataframe=pd.read_csv('Dataset_1.csv')
    relative_app=dataframe.loc[dataframe['Category']==category]
    app_list=relative_app.loc[relative_app['Installs'] == pred[0]].iloc[:]['App'].tolist()
    pred_result={}
    pred_result['result']=set(pred)
    pred_result['relative_app']=set(app_list[:2])
    return pred_result









