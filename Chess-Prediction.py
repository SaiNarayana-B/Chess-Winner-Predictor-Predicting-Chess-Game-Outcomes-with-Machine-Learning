import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import GradientBoostingClassifier as GBC, VotingClassifier
from sklearn.metrics import accuracy_score

data=pd.read_csv('chess train.csv')

num_cols=['turns','white_rating','black_rating','opening_ply']
cat_cols=['rated','victory_status','increment_code','opening_eco']

label_encoders={}
for col in cat_cols:
    label_encoders[col]=LabelEncoder()
    data[col]=label_encoders[col].fit_transform(data[col])

X=data[num_cols+cat_cols]
y=data['winner']

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

params1={'learning_rate':0.2,'max_depth':4,'n_estimators':250}
params2={'learning_rate':0.2,'max_depth':4,'n_estimators':200}
clf1=GBC(**params1)
clf2=GBC(**params2)
clf3=GBC(learning_rate=0.2,max_depth=3,n_estimators=200)
voting_clf=VotingClassifier(estimators=[('clf1',clf1),('clf2',clf2),('clf3',clf3)],voting='hard')
voting_clf.fit(X_train,y_train)
y_pred=voting_clf.predict(X_test)

accuracy=accuracy_score(y_test,y_pred)
print(f"Accuracy: {accuracy*100}%")
