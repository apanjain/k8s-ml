import os
import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression
from pyArango.connection import *

DB_CONN_URL = os.environ.get('DB_CONN_URL', '')
DB_CONN_PORT = os.environ.get('DB_CONN_PORT', '')
DB_DATABASE = os.environ.get('DB_DATABASE', 'db_name')
DB_COLLECTION = os.environ.get('DB_COLLECTION', 'collection_name')
DB_USER = os.environ.get('DB_USER', 'username')
DB_PASS = os.environ.get('DB_PASS', 'password')

# Connect to ArangoDB
conn = Connection(arangoURL="{}:{}".format(DB_CONN_URL, DB_CONN_PORT),
                  username=DB_USER, password=DB_PASS, verify=False)
db = conn[DB_DATABASE]
testCol = db.collections[DB_COLLECTION].fetchAll(rawResults=True)
df = pd.DataFrame(testCol)

newobj = df[["YearsExperience", "Salary"]]

# separate feature and target
x = newobj['YearsExperience'].values.reshape(30, 1)
y = newobj['Salary']


# train the model
model = LinearRegression()
model.fit(x, y)

joblib.dump(model,  '/mnt/c/trained_model')
