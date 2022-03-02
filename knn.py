from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
IrisData=load_iris() 
x=IrisData.data
y=IrisData.target
x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=42)
Knn=KNeighborsClassifier(n_neighbors=7)
Knn.fit(x_train,y_train)
print(Knn.predict(x_test))
