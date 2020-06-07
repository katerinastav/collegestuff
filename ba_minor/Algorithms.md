[Intro Data Mining] (https://www.sciencedirect.com/science/article/pii/B9780128028810000019)

# Supervised Learning
> the target is known (which class an instance belongs to) and a model is trained to
predict that target.

> Input data is called training data and has a known label or result such as spam/not-spam or a stock price at a time.
A model is prepared through a training process in which it is required to make predictions and is corrected when those predictions are wrong. The training process continues until the model achieves a desired level of accuracy on the training data. Example problems are classification and regression.

## Classification: classify data set in one or more predefined classes
> To predict the outcome of a given sample where the output variable is in the form of categories. Examples include labels such as male and female, sick and healthy.

## Regression: predictive technique (associate data set to a quantitative variable and predict the value of that variable)
> To predict the outcome of a given sample where the output variable is in the form of real values. Examples include real-valued labels denoting the amount of rainfall, the height of a person.

#### Simple Linear Regression 
++ Easy simple implementation
++ Fast training
-- applicable only if solution is linear (real life mostly not) 
! Comparison Desicion tree:
  -- supports non linearity
  -- In general, DT better average accuracy
  ++ When there are large number of features with less data-sets (low noise) LR may outperform DT
  -- For categorical independent variables DT are better than LR
! Comparison with KNN
  ++ KNN is slower
  
  source: https://towardsdatascience.com/comparative-study-on-classic-machine-learning-algorithms-24f9ff6ab222
  [source] (https://medium.com/@dannymvarghese/comparative-study-on-classic-machine-learning-algorithms-part-2-5ab58b683ec0)

#### Multiple Linear Regression

#### Logistic Regression
> Logistic regression returns a probability. You can use the returned probability "as is" (for example, the probability that the user will click on this ad is 0.00023) or convert the returned probability to a binary value (for example, this email is spam).
* In order to map a logistic regression value to a binary category, you must define a classification threshold (also called the decision threshold). A value above that threshold indicates "spam"; a value below indicates "not spam." It is tempting to assume that the classification threshold should always be 0.5, but thresholds are problem-dependent, and are therefore values that you must tune.

++ Easy simple classification method
++ Fast training
-- applicable only if solution is linear (real life mostly not) 
! Comparison Desicion tree:
  -- supports non linearity
  ++ DT cannot derive the significance of features, but LR does
 
! Comparison with KNN
  ++ KNN is slower
  -- KNN supports non-linear solutions
  ++ LR can derive confidence level (about its prediction), whereas KNN can only output the labels.
  
! Comparison with Naive Bayes
  ++ Naive bayes works well with small datasets, whereas LR+regularization can achieve similar performance.
  ++ LR performs better than naive bayes upon colinearity, as naive bayes expects all features to be independent.

[source] (https://developers.google.com/machine-learning/crash-course/classification/thresholding)


#### Naïve Bayes
> Naive bayes is a generative probability model used for classification problems. It is the prime model used for text classifications, where featureset is very large. It is extensively used for sentiment analysis, spam filtering etc.

* Naive bayes is preferred when the features are mutually independent and have limited training data.
* Naive bayes is highly used in text classification, spam filtering, recommender systems etc.

++ works well with less training data.
++ If NB conditional independence is satisfied, it converges faster than other discriminative models.
++ Handles irrelevant features.
++ Supports binary and multi-class classification problems.
-- expects the features to be strictly independent to each other, which is not applicable in real life scenarios.
-- While training sample of a large population, and if we have a feature with P(X=feature|Y) as zero, the posterior probability will become zero. This happens when the sample is not representing the population properly.
-- continuous variables are binned to extract discrete values from features. This task should be carefully done to avoid data loss.

#### KNN
* finds a group of k objects in the training set that are closest to the test object, and bases the assignment of a label on the predominance of a particular class in this neighborhood. 

++ easy simple learning model
-- k should be wisely selected
-- large computation cost if sample large
-- proper scaling should be provided for fait treatment among features

! Comparison with Naive Bayes
  -- KNN slower because of real-time execution
  
! Comparison with Linear regression:
  ++ KNN Better when data have high SNR

#### Desicion Tree 
* Decision trees are the most developed methods for partitioning sets of items into classes.
> Decision tree is a tree based algorithm used to solve regression and classification problems.

++ No preprocessing needed on data
++ No assumptions on distribution of data.
++ Handles colinearity efficiently.
++ Decision trees can provide understandable explanation over the prediction.
-- Chances for overfitting the model if we keep on building the tree to achieve high purity. decision tree pruning can be used to solve this issue.
-- Prone to outliers.
-- Tree may grow to be very complex while training complicated datasets.
-- Looses valuable information while handling continuous variables.

! Comparison KNN
  ++ DT supports automatic feature interaction
  ++ faster
  
! Comparison Naive Bayes
  ++ Decision tree is a discriminative model, whereas Naive bayes is a generative model.
  ++ Decision trees are more flexible and easy.
  -- Decision tree pruning may neglect some key values in training data, which can lead the accuracy for a toss.
  
#### Random Forest 
> Random Forest is an ensemble model where, multiple decision trees are combined to get a stronger model. The derived model will be more robust, accurate and handles overfitting better than constituent models.

++ Accurate and powerful model.
++ handles overfitting efficiently.
++ Supports implicit feature selection and derives feature importance.
-- computationally complex and slower when forest becomes large.
-- Not a well descriptive model over the prediction.

! Comparison with Naive Bayes
  * Random Forest is a complex and large model whereas Naive Bayes is a relatively smaller model.
  * Naive Bayes performs better with small training data, whereas RF needs larger set of training data.

# Unsupervised Learning
> the target is unknown (unknown class or even if any class structure exists) and the
model seeks to uncover some hidden classification or structure.

> Input data is not labeled and does not have a known result. A model is prepared by deducing structures present in the input data. This may be to extract general rules. It may be through a mathematical process to systematically reduce redundancy, or it may be to organize data by similarity. Example problems are clustering, dimensionality reduction and association rule learning.

## Clustering: like classification but the classes are not known yet, just looking for patterns
> To group samples such that objects within the same cluster are more similar to each other than to the objects from another cluster.

## Association Rules: finding sets of items that occur together in records of a data set and the relationships among those items in order to derive multiple correlations that meet the specified thresholds.
> To discover the probability of the co-occurrence of items in a collection. It is extensively used in market-basket analysis. Example: If a customer purchases bread, he is 80% likely to also purchase eggs.

#### Association Rules

#### Clustering
* separates data items into a number of groups or clusters such that items in the same cluster are more similar to each other and items in different clusters tend to be dissimilar, according to some measure of similarity or proximity. Differently from supervised learning, where training examples are associated with a class label that expresses the membership of every example to a class, clustering assumes no information about the distribution of the items, and it has the task to both discover the classes present in the data set and to assign items among such classes in the best way.

#### K-means
* K-means is one of the most used clustering algorithms based on a partitional strategy. K-means is an algorithm that minimizes the squared error of values from their respective cluster means. In this way K-means implements hard clustering, where each item is assigned to only one cluster 

#### Bayesian Classification 
* The Bayesian approach to unsupervised learning provides a probabilistic method to inductive inference. In Bayesian classification class membership is expressed probabilistically that is an item is not assigned to a unique class, instead it has a probability of belonging to each of the possible classes. The classes provide probabilities for all attribute values of each item. Class membership probabilities are then determined by combining all these probabilities. Class membership probabilities of each item must sum to 1, thus there are not precise boundaries for classes: every item must be a member of some class, even though we do not know which one. When every item has a probability of no more than 0.5 in any class, the classification is not well defined because it means that classes are abundantly overlapped. On the contrary, when the probability of each instance is about 0.99 in its most probable class, the classes are well separated.


# Other Terms

#### Skewness:
> is a quantifiable measure of how distorted a data sample is from the normal distribution.

[Source] (https://deepai.org/machine-learning-glossary-and-terms/skewness)
