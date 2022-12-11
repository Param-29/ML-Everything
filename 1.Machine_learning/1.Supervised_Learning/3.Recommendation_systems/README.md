# Recommendation Systems

## Prerequisites
* BASIC ML 
* Linear Algebra Understanding 
* Tensorflow and Pandas 

## Why and What?? 



Recommendation Systems: ML based suggestion systems which suggest next items. 

Example: 
* Amazon recommending similar items to buy 
* Spotify recommending music 
* List of movies u'd like by netflix etc. 

Two kinds of recommendations are commonly used:

* home page recommendations
  * Suggesting user items based on user history 
* related item recommendations
  * Suggesting similar items once user has selected an item

Why recommendatoin systems? 

    40% of app installs on Google Play come from recommendations.
    60% of watch time on YouTube comes from recommendations.

**Terminologies**

* Item: thing you are trying to predicit (y in ML)
* Query: given data item for which you are trying to predict item. 

## Recommendation Systems Overview

One common architecture for recommendation systems consists of the following components:

    1. candidate generation
    2. scoring
    3. re-ranking

![](https://developers.google.com/machine-learning/recommendation/images/Process.svg)

Candidate Generation
* System starts from a potentially huge corpus and generates a much smaller subset of candidates.

Scoring 
* Evaluating and ranking probable items and scoring them based on user and item information available 

Re-ranking 
* the system must take into account additional constraints for the final ranking. 
  * removes items that the user explicitly disliked or boosts the score of fresher content. 
  * helps ensure diversity, freshness, and fairness.

## Candidate Generation

_Given a query, the system generates a set of relevant candidates._

Two common candidate generation approaches
* Content based filtering
  * Suggesting items to a user based on previous feedback of same user on different items.
  * i.e Item related data (or embedding/ profile) is only used
* collaborative filtering
  * Suggesting items to a user based on previous feedback of all users on different items.
  * i.e Item & User related data (or embedding/ profile) is used


**Key difference**
1. Content based filtering does not use user-profile data (i.e data related to other users)
2. collaborative filtering uses other user profiles to make predictions
   * If user A is similar to user B, and user B likes video 1, then the system can recommend video 1 to user A (even if user A hasn’t seen any videos similar to video 1).

### Similarity Measures 

It is a function takes a pair of embeddings and returns a scalar measuring their similarity.

To determine the degree of similarity, most recommendation systems rely on one or more of the following:

* cosine
  * This is simply the cosine of the angle between the two vectors, 
* dot product
  * the cosine of the angle multiplied by the product of their scalar value (aka length of representation in graphs)
* Euclidean distance
  * Simply put (1 - dot (v1, v2))

## Content based filtering 

_Content-based filtering **uses item features to recommend other items** similar to what the user likes, based on their previous actions or explicit feedback._

Example: 

The following figure shows a feature matrix where each row represents an app and each column represents a feature. Features could include categories (such as Education, Casual, Health), the publisher of the app, and many others.

You also represent the user in the same feature space.

![Content based filtering](https://developers.google.com/machine-learning/recommendation/images/Matrix1.svg)


**Advantages & disadvantages**

Adv: 
* The model doesn't need any data about other users; This makes it easier to scale to a large number of users.
* The model can capture the specific interests of a user, and can recommend niche items that very few other users are interested in.

Dis-adv:
* The model can only make recommendations based on existing interests of the user. In other words, the model has limited ability to expand on the users' existing interests.




## Collaborative filtering

To address some of the limitations of content-based filtering, collaborative filtering uses similarities between users and items simultaneously to provide recommendations.

_Example: This helps taking into consideration and humans are sometimes similar to each other and movies sometimes are similar to each other_


### A Movie Recommendation Example

Consider a movie recommendation system in which the training data consists of a feedback matrix in which:

    Each row represents a user.
    Each column represents an item (a movie).

The feedback about movies falls into one of two categories:

    Explicit— users specify how much they liked a particular movie by providing a numerical rating.
    Implicit— if a user watches a movie, the system infers that the user is interested.

To simplify, we will assume that the feedback matrix is binary; that is, a value of 1 indicates interest in the movie.

When a user visits the homepage, the system should recommend movies based on both:

    1. similarity to movies the user has liked in the past
    2. movies that similar users liked



![](https://developers.google.com/machine-learning/recommendation/images/2Dmatrix.svg)

    Note: We represented both items and users in the same embedding space. 
    This may seem surprising. After all, users and items are two different entities. 
    However, you can think of the embedding space as an abstract representation common to both items and users, 
    in which we can measure similarity or relevance using a similarity metric.

Collaborative filtering approach can be to train a model to optimize any 1 of below by fixing remaining
* Embedding (generally tuned)
* User profile 
* Item profile

### Matrix Factorization

Factorization: Big thing represented as 2 or more small things 

```
example; 24: 4 * 6
```

Similarly Matrix Factorization is maxtrix representation of a space (A) into 2 smaller maxtrix (u) and (i)
* i.e representing big matrix as product of 2 small matrixes. (using some kind of features)





Here: 
    A: feedback matrix
    U: User Matrix 
    i: item Matrix

![](https://developers.google.com/machine-learning/recommendation/images/Matrixfactor.svg)



### How to find matrix fact: ML

#### Objective Function (Error function)

Sum of square of all entries 

```
sum(y_ob - y_ac)^2

y_ob: observed 
y_ac: Actual
```

Solution to this problem can be found by **Singular Value Decomposition (SVD)** of the matrix. 
but this is time consuming; hence we try and find and minimize this error by approximation 

#### Minimizing the Objective Function

Common algorithms to minimize the objective function include:

    Stochastic gradient descent (SGD) is a generic method to minimize loss functions.

    Weighted Alternating Least Squares (WALS) is specialized to this particular objective.

WALS works by initializing the embeddings randomly, then alternating between:

* Fixing U and solving for V.
* Fixing V and solving for U.


[ADV & DISADV of each algorithm](https://developers.google.com/machine-learning/recommendation/collaborative/matrix#sgd-vs.-wals)

**Advantages & disadvantages of collaborative filtering**

Adv: 
* Great starting time
* Good approximation algorithms ready
Dis-adv:
* Cannot work well with fresh items/queries (cold-start problem.)
  * [Solution 1] After a few interactions; using U * V is A, we use U is A / V to get item/user embeddings to make predictions better
  * [Solution 2] Heuristics (like average of similar items) to generate embeddings of fresh items.
* Hard to include side features for query/item
  *  For movie recommendations, the side features might include country or age.
  *  [Solution] To be handled in re-ranking
## Resources

### Courses 
* [Google Recommendation Systems](https://developers.google.com/machine-learning/recommendation)


### Videos 
* [Matrix Factorization for Collaborative Filtering](https://www.youtube.com/watch?v=ZspR5PZemcs)
### Blogs 

### Books