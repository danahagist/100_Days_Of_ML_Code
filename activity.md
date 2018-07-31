# 100 Days Of ML Code - Activity Log

### Day 0: July 29th, 2018


**Today's Progress**:

Learned about hyperparameter tuning, which entails changing the parameters of a machine learning model, as opposed to making changes to the underlying data.  In this case, was looking at the k-value in a KNN model (see next line).

Worked through exercises to optimize hyperparamters, specifically in a k-nearest-neighbors model (optimizing the k-value by using grid search).

Next, learned about using holdout validation, a process involving splitting your dataset into a 50% train and 50% test set, generating predictions, calculating errors, switching the train and test set, repeating earlier steps, and then averaging your errors.

**Thoughts:** 

The hyperparameter tuning using grid search is pretty quick, easy, and efficient.  I enjoyed learning about it.  However, throughout the exercises, I had to revisit a couple concepts including looping through dictionaries and using the Python built-in function 'enumerate'.

This was my first exposure to holdout validation, which is a pretty handy concept.  I'm looking forward to learning more about this and applying to some other "price prediction" datasets.

**Link to work:** https://github.com/danahagist/100_Days_Of_ML_Code/blob/master/day0_knn.py

### Day 1: July 30th, 2018


**Today's Progress**:

Learned about the modules KFold and cross_val_score, both from Python's Scikit-Learn library.  

Worked on completing the Dataquest Machine Learning Fundamentals course by spending an hour on the guided project, Predicting Car Prices.  I will post the completed project once I make it all the way through.  One thing I try to do with most of these guided projects is to create a template that can be used for other similar efforts.

I also signed up for the following Kaggle competition : https://www.kaggle.com/c/new-york-city-taxi-fare-prediction/discussion/62146
And.... the associated Google Cloud ML Course on Coursera: https://www.coursera.org/specializations/machine-learning-tensorflow-gcp?utm_source=googlecloud&utm_medium=institutions&utm_campaign=kaggle_competition_email

Lastly, I worked through Day 9 of HackerRank's '30 Days of Code' challenge.  Today entailed using a simple recursive function to calculate a factorial of an integer.  Powerful technique, simple implementation in Python.  Link is provided below.  

It's going to be a lottttttt to keep up with all of these things over the next 100 days, but I couldn't be more excited to learn and grind.

**Thoughts:** 

One thing I'm consistently reminded of as I go through various exercises and guided projects is how important knowing how to clean your data is.  Data is inherently "unclean" from an analytics perspective, and it takes significant effort to get your dataframe into a format where you COULD apply a machine learning algorithm to it.  I imagine it's a topic I'm going to have to come back to again and again.

**Link to work:** https://github.com/danahagist/100_Days_Of_ML_Code/blob/master/day1_factorial.py

### Day 2: July 31st, 2018

**Today's Progress**:

Worked through HackerRank's Day 10 Challenge, counting the maximum number of 1's in a binary representation of some int.  This was a good little challenge, and I took the longer route to ensure I understood every step.  You can see the link to my work below

**Thoughts:** 

One of the first things I did today was decided to make a change to my approach in terms of studying.  Although I'm generally putting between 3-4 hours a day, I want to be sure I'm hitting certain things daily.  As such, I'm going to always start my day with a single HackerRank challenge.  That will ensure I always have something that I can share and that I'm getting the coding synapses firing.  After HackerRank, I'll ensure I get at least 1% of my Dataquest Data Scientist Path completed.  Lastly, I'll spend the rest of my time doing the Google Cloud Machine Learning Course and Kaggle Taxi Fare Prediction Competition.

**Link to work:** 
https://github.com/danahagist/100_Days_Of_ML_Code/blob/master/day2_binary.py
