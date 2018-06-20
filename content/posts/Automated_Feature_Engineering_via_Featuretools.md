 Title: Automated Feature Engineering via Featuretools
Date: 2018-06-20 10:26
Modified: 2018-06-20 11:32
Status: published
Category: data science
Tags: python, featuretools, feature engineering, data science
Slug: featuretools
Authors: Al Krinker
Summary: How to automatically create machine learning features via Featuretools


# Take aways
- Feature engineering, also known as feature creation, is the process of constructing new features from existing data to train a machine learning model.
- Feature engineering means building additional features out of existing data which is often spread across multiple related tables. Feature engineering requires extracting the relevant information from the data and getting it into a single table which can then be used to train a machine learning model.
- We can group the operations of feature creation into two categories: transformations and aggregations. A transformation acts on a single table by creating new features out of one or more of the existing columns. An aggregations are performed across tables, and use a one-to-many relationship to group observations and then calculate statistics.
- Aggregation operations are not difficult by themselves, but if we have hundreds of variables spread across dozens of tables, this process is not feasible to do by hand.
- Fortunately, featuretools is exactly the solution we are looking for. This open-source Python library will automatically create many features from a set of related tables.

{% notebook ../notebooks/Automated_Feature_Engineering.ipynb %}