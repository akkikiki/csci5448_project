# TODO
- [x] Implement a simple system to keep track of user
- [x] Implement a simple menu for CUI
- [ ] Implement the ``TextClassifier'' class (which is planned to be a wrapper of one method in [scikit-learn](http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html))
- [ ] Implement the ``Corpus'' class (which is the class that shows basic information of the training data)

# TODO for the TextClassifier class
- [ ] Implement a method that tweaks a specified parameter/weight by increasing or decreasing by a specified float number.
- [ ] Use Momento design pattern to keep track of the ``tweaked'' parameter states

# TODO for the Corpus class
- [ ] Implement a method that shows some sampled texts in the training data.
- [ ] Use Factory design pattern to handle different types of copora (i.e., training data to train a model), (1) Raw .txt file, or (2) .xml file. 
