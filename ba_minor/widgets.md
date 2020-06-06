# Widgets, for what and why they are used

:bulb: Very useful documentation: 
[Orange Documentation](https://orange.biolab.si/docs/)

:bulb: Comparison of algorithms:
[towardsscience. com] (https://towardsdatascience.com/comparative-study-on-classic-machine-learning-algorithms-24f9ff6ab222) 

## Data Sampler

## Box Plot

 * Identify Outliers

## Test and Score
* Test on train data uses the whole dataset for training and then for testing. This method practically always gives wrong results.
* Test on test data: the above methods use the data from Data signal only. 

### Classification Columns:

#### CLassification Accuracy (CA)
* You have to compare accuarcy with chance. If CA is better at predicting something correct than chance would, then it is a good model.
* CA = #correct predictions/ #total predictions ( (TP + TN)/ TP + TN + FP + FN )
* Great source to understand how to judge an algorithm based on the test and score results: https://developers.google.com/machine-learning/crash-course/classification/accuracy

#### Precision 
* percentage of items flagged as positive, taht were correctly classified
* What proportion of positive identifications was actually correct? ( TP / (TP + FP) ) 
* A model that produces no false positives has a precision of 1.0.

#### Recall 
* percntage of actual positives, that were correctly classified
* What proportion of actual positives was identified correctly? ( TP / ( TP + FN) )
* A model that produces no false negatives has a recall of 1.0.

:warning: improving precision typically reduces recall and vice versa. Generally (But not with certainty) : 
* Increasing CT (classification threshold) => precision increases, recall decreases
* Decreasing CT => precision decreases, recall increases
:bulb: In general, a model that outperforms another model on both precision and recall is likely the better model. Obviously, we'll need to make sure that comparison is being done at a precision / recall point that is useful in practice for this to be meaningful. For example, suppose our spam detection model needs to have at least 90% precision to be useful and avoid unnecessary false alarms. In this case, comparing one model at {20% precision, 99% recall} to another at {15% precision, 98% recall} is not particularly instructive, as neither model meets the 90% precision requirement. But with that caveat in mind, this is a good way to think about comparing models when using precision and recall.

#### AUC (Area Under the ROC Curve)

###### ROC curve :
> is a graph showing the performance of a classification model at all classification thresholds. This curve plots two parameters: True Positive Rate, False Positive Rate

* AUC measures the entire two-dimensional area underneath the entire ROC curve (think integral calculus) from (0,0) to (1,1).
* the probability that the model ranks a random positive example more highly than a random negative example. 
* predictions are 100% correct has an AUC of 1.0

### Regression Columns:

#### MSE

#### RMSE

