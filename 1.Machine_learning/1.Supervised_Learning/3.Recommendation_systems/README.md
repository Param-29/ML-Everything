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

    candidate generation
    scoring
    re-ranking

![](https://developers.google.com/machine-learning/recommendation/images/Process.svg)

Candidate Generation
* System starts from a potentially huge corpus and generates a much smaller subset of candidates.

Scoring 
* Evaluating and ranking probable items and scoring them based on user and item information available 

Re-ranking 
* the system must take into account additional constraints for the final ranking. 
  * removes items that the user explicitly disliked or boosts the score of fresher content. 
  * helps ensure diversity, freshness, and fairness.

## Resources

### Courses 
* [Google Recommendation Systems](https://developers.google.com/machine-learning/recommendation)


### Videos 

### Blogs 

### Books