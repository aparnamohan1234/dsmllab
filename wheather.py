wheather=['Sunny','Sunny','Overcast','Rainy','Rainy','Rainy','Overcast','Sunny','Sunny','Raniy','Sunny','overcast','overcast','Rainy']
temp=['Hot','Hot','Hot','Mild','Cool','Cool','Cool','Mild','Cool','Mild','Mild','Mild','Hot','Mild']
play=['No','No','Yes','Yes','Yes','No','Yes','No','Yes','Yes','Yes','Yes','Yes','No']
from sklearn import preprocessing
le = preprocessing.LabelEncoder()
wheather_encoded=le.fit_transform(wheather)
print(wheather_encoded)
temp_encoded=le.fit_transform(temp)
label=le.fit_transform(play)
print ("temp:",temp_encoded)
print ("Play:",label)
features=list(zip(wheather_encoded,temp_encoded))
print(features)
from sklearn.naive_bayes import GaussianNB
model = GaussianNB()
model.fit(features,label)
print ("sunny-3 overcast-0 Raniy-1")
print ("hot-1 mild-2 cool-0")
a=int(input("enter the value for wheather"))
b=int(input("enter the temp"))
predicted=model.predict([[a,b]]) 
print ("Predicted Value:", Predicted)
if predicted==1:
    print("there will be a play today")
else:    
    print("there will be no today")