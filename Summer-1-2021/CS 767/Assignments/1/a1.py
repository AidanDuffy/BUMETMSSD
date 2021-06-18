from matplotlib import pyplot as plt
from sklearn.tree import DecisionTreeClassifier
import os
import pandas as pd
import numpy as np
from graphviz import Source # "Graphical visualization"
from sklearn.tree import export_graphviz
from matplotlib.colors import ListedColormap

here = os.path.abspath(__file__)
CHAPTER_ID = r"decision_trees"
IMAGES_PATH = os.path.abspath(os.path.join(os.pardir,  r"1/images/" + CHAPTER_ID))
LOAN_FILE = os.path.abspath(os.path.join(here, os.pardir + r"/Bank_Personal_Loan_Modelling.xlsx"))

# INTENT: Customer data loaded and decision tree tree_clf constructed for it


# https://www.kaggle.com/itsmesunil/bank-loan-modelling
customers = pd.read_excel(LOAN_FILE,sheet_name=1)

print("========Customers========") # view
print(customers) # all customer data
customers = customers.sample(n=100,random_state=4)
customer_info = customers.columns
# use only Income and credit card average
X_cols = [customer_info[3],customer_info[6]]
X = customers[X_cols]
print("========X========") # view
print(X)

# Whether they have a personal loan
target = [customer_info[9]]
target_vals = ['0','1']
y = customers[target]
print("========y========") # view
print(y)


# https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html
# Use gini measure; tree depth 2
tree_clf = DecisionTreeClassifier(max_depth=2, random_state=42) # definition
# Apply the CART (classification and regression tree) algorithm
tree_clf.fit(X, y) #


export_graphviz(
        tree_clf, # the tree object
        out_file=os.path.join(IMAGES_PATH, "customer_tree.dot"),
        feature_names=X_cols,
        class_names=target_vals,
        rounded=True,
        filled=True
    )

Source.from_file(os.path.join(IMAGES_PATH, "customer_tree.dot"))  # display

# INTENT: Show the customer data as classified by tree_clf

from matplotlib.colors import ListedColormap


def plot_decision_boundary(clf, X, y, axes=[0, 10, 50, 205], iris=True,
                           legend=False, plot_training=True):
    x1s = np.linspace(axes[0], axes[1], 100)
    x2s = np.linspace(axes[2], axes[3], 100)
    x1, x2 = np.meshgrid(x1s, x2s)
    X_new = np.c_[x1.ravel(), x2.ravel()]
    y_pred = clf.predict(X_new).reshape(x1.shape)
    custom_cmap = ListedColormap(['#fafab0', '#9898ff', '#a0faa0'])

    plt.contourf(x1, x2, y_pred, alpha=0.3, cmap=custom_cmap)
    if not iris:
        custom_cmap2 = ListedColormap(['#7d7d58', '#4c4c7f', '#507d50'])
        plt.contour(x1, x2, y_pred, cmap=custom_cmap2, alpha=0.8)
    if plot_training:
        cc = pd.DataFrame(X['CCAvg'])
        inc = pd.DataFrame(X['Income'])
        has_loan = y[y["Personal Loan"] == 1]
        cc = cc.join(has_loan)
        inc=  inc.join(has_loan)
        cc_loan = cc[cc["Personal Loan"] == 1]
        inc_loan = inc[inc["Personal Loan"] == 1]
        cc_no_loan = cc[cc["Personal Loan"] != 1]
        inc_no_loan = inc[inc["Personal Loan"] != 1]
        plt.plot(cc_loan, inc_loan, "rs",
                 label="No personal loan")
        plt.plot(cc_no_loan, inc_no_loan, "g^",
                 label="Has personal loan")
        plt.axis(axes)
    if iris:
        plt.xlabel("Petal length", fontsize=14)
        plt.ylabel("Petal width", fontsize=14)
    else:
        plt.xlabel(r"Education Level", fontsize=18)
        plt.ylabel(r"Income", fontsize=18, rotation=0)
    if legend:
        plt.legend(loc="lower right", fontsize=14)


plt.figure(figsize=(8, 4))
plot_decision_boundary(tree_clf, X, y, iris=False)
# Boundaries from the resulting decision tree above
"""plt.plot([2.45, 2.45], [0, 3], "k-", linewidth=2)
plt.plot([2.45, 7.5], [1.75, 1.75], "k--", linewidth=2)
plt.plot([4.95, 4.95], [0, 1.75], "k:", linewidth=2)
plt.plot([4.85, 4.85], [1.75, 3], "k:", linewidth=2)
plt.text(1.40, 1.0, "Depth=0", fontsize=15)
plt.text(3.2, 1.80, "Depth=1", fontsize=13)
plt.text(4.05, 0.5, "(Depth=2)", fontsize=11)"""

#save_fig("decision_tree_decision_boundaries_plot")
#plt.show()

x1=tree_clf.predict_proba([[10, 900]])
print(x1)