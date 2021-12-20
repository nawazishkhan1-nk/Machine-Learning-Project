from sklearn import preprocessing

def encode_labels(data):
    le=preprocessing.LabelEncoder()
    le.fit(data['workclass'].unique())
    data['workclass']=le.transform(data['workclass'])
    le.fit(data['occupation'].unique())
    data['occupation']=le.transform(data['occupation'])
    le.fit(data['education'].unique())
    data['education']=le.transform(data['education'])
    le.fit(data['marital.status'].unique())
    data['marital.status']=le.transform(data['marital.status'])
    le.fit(data['relationship'].unique())
    data['relationship']=le.transform(data['relationship'])
    le.fit(data['race'].unique())
    data['race']=le.transform(data['race'])
    le.fit(data['sex'].unique())
    data['sex']=le.transform(data['sex'])
    le.fit(data['native.country'].unique())
    data['native.country']=le.transform(data['native.country'])
    return data