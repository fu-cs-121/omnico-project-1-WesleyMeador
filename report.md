# Euphoria User Engagement Analysis Report

**Author:** Wesley Meador  
**Date:** March 6th, 2025

---

## Introduction

One major objective of this project was to practice how to read a CSV file using Python. After doing that, the main objective was to utilize data from the CSV file to calculate statistics, making use of dictionaries in the process. This analysis is important because it allows for us to easily summarize and understand the data from the algorithms. Utilizing Python, we can calculate important statistics such as the highest happiness rating much easier than by hand.

## Methodology

The first step to perform this analysis, after receiving the starter file, was to convert session_duration and happiness_rating from strings to integers. This was necessary in order to perform later calculations in the analysis. The next step was to calculate the averages for each algorithm, those being average happiness and average session duration. This step was completed through the usage of for loops, which ensures that the averages are calculated for each of the algorithms. The following step was to determine the max happiness rating. First, variables were initialzied to track the maximum happiness value and its algorithm. Then, a for loop was used to cylce through the average happiness of each algorithm, replacing the initialized variable when a new maximum value was found. For the next step, this process was repeated for average session duration. Finally, print statements were used to properly format the results. For loops were utilized in order to display the results of each algorithm.

## Results

- **Average Happiness Rating per Algorithm**

  - JoyStream: 8.5
  - SerenityFlow: 7.0
  - DeepPulse: 5.0

- **Total Number of Sessions per Algorithm**

  - JoyStream: 4
  - SerenityFlow: 3
  - DeepPulse: 3

- **Average Session Duration per Algorithm**

  - JoyStream: 37.5 minutes
  - SerenityFlow: 30.0 minutes
  - DeepPulse: 45.0 minutes

- **Highest and Lowest Performers**
  - Highest Average Happiness Rating: 8.5 (JoyStream)
  - Longest Average Session Duration: 45.0 minutes (DeepPulse)

## Observations and Insights

One noteworthy finding from this analysis is the relation between happiness and session duration. The algorithm with the highest average happiness rating, JoyStream, is in the middle when it comes to session duration. The algorithm with the lowest average happiness rating, DeepPulse, had the longest session duration. DeepPulse had a considerably lower average happiness score compared to the other algorithms, being 2 points below the next highest, SerenityFlow. One anomaly is that JoyStream was used in one additional session compared to the other algorithms, which may make for a somewhat inaccurate comparison. In addition, a possible ethical concern could stem from changing the content algorithm of the user without properly informing them or giving them an option to opt out of the study. 

## Conclusions and Recommendations

Based on the results of this analysis, it can be concluded that JoyStream was the most effective algorithm for boosting the happiness of users, while DeepPulse was the most effective for extending the length of time a user spends on a session. For future analysis, I would recommend completing a study with a larger sample to see if this conclusion can be applied to a wider population of users. In addition, adjustments should be made with the sampling design to ensure there are no ethical concerns present, such as properly informing users of the study and giving the option for them to not participate.

---

_This report contains confidential information proprietary to OmniCo. Unauthorized use or disclosure is strictly prohibited._
