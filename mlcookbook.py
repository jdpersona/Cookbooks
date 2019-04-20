


# create a mapping from fruit label value to fruit name to make results easier to interpret
lookup_fruit_name = dict(zip(fruits.fruit_label.unique(), fruits.fruit_name.unique()))   



knn.score(X_test, y_test)

fruit_prediction = knn.predict([[20, 4.3, 5.5]])


lookup_fruit_name[fruit_prediction[0]]
