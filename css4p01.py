# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 10:43:17 2024

@author: khkiri
"""

import pandas as pd

df = pd.read_csv("movie_dataset.csv", index_col=0)

print(df.info())


"""
DataFrame without nan
"""

Cleaned_df = df.dropna(axis=0)

print(Cleaned_df.info())


"""
highest_rated_movie
"""

highest_rated_movie = df[df['Rating'] == df['Rating'].max()]

print("highest_rated_movie")

print(highest_rated_movie)

"""
The avearge revenue
"""

avearge_revenue = Cleaned_df['Revenue (Millions)'].mean()

print("avearge_revenue" , avearge_revenue)


"""
the average revenue of movies between 2015 to 2017 in the dataset
"""


filtred_movies = Cleaned_df[(Cleaned_df['Year'] >= 2015) & (Cleaned_df['Year'] <= 2017)]

average_revenue_2015_2017 = filtred_movies['Revenue (Millions)'].mean()

print ("average_revenue_2015_2017 ", average_revenue_2015_2017)

"""

How many movie were released in the year 2016

"""

movies_2016 = df[df['Year'] == 2016]

num_movies_2016 = len(movies_2016)

print ("Number of movies released in 2016:", num_movies_2016)

"""
How many movies were directed by Christopher Nolan

"""

movies_Christopher_Nolan = df[df['Director'] == "Christopher Nolan"]

num_movies_Cristopher_Nolan = len(movies_Christopher_Nolan)

print ("number of movies were directed by Christopher Nolan:", num_movies_Cristopher_Nolan)

"""
number of movies have a rating of at least 8

"""

movies_rated_upper_8 = df[df['Rating'] >= 8.0]

num_movies_rated_upper_8 = len (movies_rated_upper_8)

print ("number of movies have a rating of at least 8:", num_movies_rated_upper_8)


"""
The median rating of movies directed by Christover Nolan

"""


Median_rating_Christover_Nolan = movies_Christopher_Nolan ['Rating'].median()

print ("The median rating of movies directed by Christover Nolan:", Median_rating_Christover_Nolan)



"""

The year with the highest avearage rating

"""

average_rating_by_year = df.groupby('Year')['Rating'].mean()

Year_highest_rating = average_rating_by_year.idxmax()

print ("The year with the highest avearage rating:", Year_highest_rating)


"""
What is the percentage increase in number of movies made between 2006 and 2016

"""


movies_2006 = df[df['Year'] == 2006]

num_movies_2006 = len(movies_2006)

Percentage_increase_2006_2016 = ((num_movies_2016 - num_movies_2006)/num_movies_2006)*100


print ("the percentage increase in number of movies made between 2006 and 2016", Percentage_increase_2006_2016)


"""

Find the most common actor

"""

Actors_df = df['Actors'].str.split(', ', expand=True).stack().reset_index(level=1, drop=True).rename('Actors')


most_common_actor = Actors_df.value_counts().idxmax()

movies_count_most_common_actor = Actors_df[Actors_df == most_common_actor].count()


print ("The most common actor:", most_common_actor)

print("Number of movies of the most common actor:", movies_count_most_common_actor)


"""
Number of unique genres in the data base

"""

Gender_df = df['Genre'].str.split(', ', expand=True).stack().reset_index(level=1, drop=True).rename('Genre')

num_unique_Gender = Gender_df.nunique()

print("Number of unique genres in the data base:", num_unique_Gender)


"""
Correlation of the numerical features
"""

numerical_features = Cleaned_df.select_dtypes(include=['float64', 'int64'])

correlation_matrix = numerical_features.corr()

print("correlation Matrix:")

print(correlation_matrix)














































