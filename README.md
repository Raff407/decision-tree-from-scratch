# Decision Tree From Scratch

A decision tree classifier written by hand in Python with NumPy, to understand how it actually works.

## The idea

A decision tree is a flowchart of yes or no questions such as "is petal length < 2.5?". It is built by repeatedly picking the question that best separates the classes.

1. **Impurity**: score how mixed the classes in a group are (Gini impurity: 0 means all one class).
2. **Best split**: try every feature and every threshold, and keep the one that reduces impurity the most.
3. **Recurse**: split each side again, until a group is pure or the tree hits a maximum depth.
4. **Predict**: walk a new point down the tree to a leaf and return that leaf's majority class.

## Plan

- [ ] Gini impurity, checked by hand on a tiny example
- [ ] Best-split search, the recursive build and prediction, on the Iris dataset
- [ ] Print the tree as text so you can read the questions it learned
- [ ] Plot train and test accuracy against maximum depth to see overfitting happen
- [ ] Check accuracy against `sklearn.tree.DecisionTreeClassifier`
- [ ] *Optional:* a random forest (many trees on random samples of the data, majority vote)

## Data

Iris to start. Titanic survival from Kaggle is a good second dataset.

## Running

```bash
pip install -r requirements.txt
python tree.py
```

## Status

Not started.
