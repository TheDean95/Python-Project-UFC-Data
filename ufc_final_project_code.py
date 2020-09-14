## Jeffrey Dean
## Python Methodologies Final Project
## UFC Fight Analysis project

## This set of code is the execution of various processes needed to analyse
## historical data on UFC fighters and potential forecasts that can be made
## from this.  The standard and third party packages are shown below with
## accompanying explanation of each set of code is below as well.  Data is full
## inserted, split into three groups of 5 factors that may be correlated to winning potential. 
## Credit to Karmanya Aggarwal from Kaggle.com for access to the data set.  

import numpy as np
import scipy
import statistics 
from scipy.stats import linregress
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.formula.api import ols
import seaborn as sns
import matplotlib.pyplot as plt


##Custom library for profile portion
from Final_Project_Profile_Library import *

## Read in the data

data = pd.read_csv (r'C:\Users\jeffd\Documents\Coding\Python\Python Methodologies\Final Project\data.csv', low_memory = False)
df_group_1 = data[['total_avg_sub_att','total_takedown_accuracy','total_striking_accuracy','total_rounds_fought','significant_strike_accuracy','total_win_decimal']]
df_group_2 = data[['total_win_tko_ko','total_win_unanimous','total_height','total_weight','total_reach','total_win_decimal']]
df_group_3 = data[['Stance','total_winning_streak','total_age','ground_attempts_pct','body_shot_accuracy','total_win_decimal']]

## User Input Directory

print("Hello and welcome to UFC data solutions")
print("Please enter a number and letter combination to conduct research")

print("Directory: ")
print("If looking to examine factor correlations, please input 1.")
print("If looking to examine simple statistics, please input 2.")
print("If looking to examine mean, standard deviation, and confidence intervals, please input 3.")
print( "If looking to examine ols_model_1, please input 4.")
print("If looking to examine ols_model_2, please input 5.")
print("If looking to examine ols_model_3, please input 6.")
print("If looking to examine ols_model_4, please input 7.")
print( "If looking to examine ols_model_5, please input 8.")
print("If looking to examine combined_model, please input 9.")
print("If looking to examine pairplot graphs, please input 10.")
print("If looking to examine factor 1 graph, please input 11.")
print("If looking to examine factor 2 graph, please input 12.")
print("If looking to examine factor 3 graph, please input 13.")
print("If looking to examine factor 4 graph, please input 14.")
print("If looking to examine factor 5 graph, please input 15.")

##Part 1 Key Factors of Interest

## Correlation coefficient is used to determine what factors have the highest
## correlation to winning outcomes in past fights.  Output of each function
## can be printed, results support which factors have strong relationships.  

class correlations:
    def group_corr():
        print("Group 1 Coefficients")
        group_1_output = print(df_group_1.corr())
        print("\n")
        print("Group 2 Coefficients")
        group_2_output = print(df_group_2.corr())
        print("\n")
        print("Group 3 Coefficients")
        group_3_output = print(df_group_3.corr())

##Part 2 5 Factor Deep Dive

## Mean, standard deviation, and confidence interval are being utilized to better
## exaplin factors of interest for a viewer.  ANOVA table and linear regression
## are used to develop potential future predictions and explanation of current
## data.


## Summary Statistics

class simple_statistics:
    def five_factor_coefficients():
        print("Takedown Accuracy Correlation to Winning")
        corr_coefficient_1 = print(np.corrcoef(data['total_takedown_accuracy'], data['total_win_decimal']))
        print("Unanimous Win Correlation to Winning")
        corr_coefficient_2 = print(np.corrcoef(data['total_win_unanimous'], data['total_win_decimal']))
        print("Total Win by KO or TKO Correlation to Winning")
        corr_coefficient_3 = print(np.corrcoef(data['total_win_tko_ko'], data['total_win_decimal']))
        print("Total Win Streak Correlation to Winning")
        corr_coefficient_4 = print(np.corrcoef(data['total_winning_streak'], data['total_win_decimal']))
        print("Ground Attempt Percentage Correlation to Winning")
        corr_coefficient_5 = print(np.corrcoef(data['ground_attempts_pct'], data['total_win_decimal']))

    def mean_std_confidence_interval():
        mean_of_factors = (data[['total_takedown_accuracy', 'total_win_unanimous', 'total_win_tko_ko', 'total_winning_streak', 'ground_attempts_pct']].mean())
        standard_deviation_of_factors = (data[['total_takedown_accuracy', 'total_win_unanimous', 'total_win_tko_ko', 'total_winning_streak', 'ground_attempts_pct']].std())
        n = 3209
        standard_error = standard_deviation_of_factors/np.sqrt(n)
        lower_95_perc_bound = mean_of_factors - 1.96*standard_error
        upper_95_perc_bound = mean_of_factors + 1.96*standard_error
        print("Mean Of Each Factor", "\n")
        print(mean_of_factors, "\n")
        print("Standard Deviation of Each Factor", "\n")
        print(standard_deviation_of_factors, "\n")
        print("95% Confidence Interval Lower and Upper Bound", "\n")
        print(lower_95_perc_bound, "\n")
        print(upper_95_perc_bound)
        
## Linear Regression and ANOVA

class ols_models:
    def ols_1():
        print("OLS Model 1")
        ols_model_1 = ols('total_win_decimal ~ total_takedown_accuracy', data = data).fit()
        aov_table_1 = sm.stats.anova_lm(ols_model_1, typ = 2)
        print(aov_table_1)

    def ols_2():
        print("OLS Model 2")
        ols_model_2 = ols('total_win_decimal ~ total_win_unanimous', data = data).fit()
        aov_table_2 = sm.stats.anova_lm(ols_model_2, typ = 2)
        print(aov_table_2)

    def ols_3():
        print("OLS Model 3")
        ols_model_3 = ols('total_win_decimal ~ total_win_tko_ko', data = data).fit()
        aov_table_3 = sm.stats.anova_lm(ols_model_3, typ = 2)
        print(aov_table_3)
        
    def ols_4():
        print("OLS Model 4")
        ols_model_4 = ols('total_win_decimal ~ total_winning_streak', data = data).fit()
        aov_table_4 = sm.stats.anova_lm(ols_model_4, typ = 2)
        print(aov_table_4)

    def ols_5():
        print("OLS Model 5")
        ols_model_5 = ols('total_win_decimal ~ ground_attempts_pct', data = data).fit()
        aov_table_5 = sm.stats.anova_lm(ols_model_5, typ = 2)
        print(aov_table_5)

    def combined_ols_model():
        print("Combined OLS Model")
        combined_model = ols('total_win_decimal ~ ground_attempts_pct + total_winning_streak + total_win_tko_ko + total_win_unanimous + total_takedown_accuracy ', data = data).fit()
        aov_combined = sm.stats.anova_lm(combined_model, typ = 2)
        print(aov_combined)

## Part 3 Visualize the Data

## Visualization graphs will be used to interpret results found including
## linear regression model plots to better view data.  Pairplot is used to show variable graphs that
## are in standard use by statisticians.  Individual graphs also included.  

class mapping:
    def pairplot_output():
        df_five_factors = data[['total_takedown_accuracy','total_win_unanimous','total_win_tko_ko','total_winning_streak','ground_attempts_pct']]
        sns.pairplot(df_five_factors, kind = "scatter")
        plt.title('Scatter_Pairplot')
        plt.show()
        
    def factor_1_graph():
        plt.scatter(data['total_takedown_accuracy'], data['total_win_decimal'])
        plt.title('Factor_1')
        plt.xlabel('total_takedown_accuracy')
        plt.ylabel('total_win_decimal')
        plt.show()

    def factor_2_graph():
        plt.scatter(data['total_takedown_accuracy'], data['total_win_decimal'])
        plt.title('Factor_2')
        plt.xlabel('total_takedown_accuracy')
        plt.ylabel('total_win_decimal')
        plt.show()

    def factor_3_graph():
        plt.scatter(data['total_win_tko_ko'], data['total_win_decimal'])
        plt.title('Factor_3')
        plt.xlabel('total_win_tko_ko')
        plt.ylabel('total_win_decimal')
        plt.show()

    def factor_4_graph():
        plt.scatter(data['total_winning_streak'], data['total_win_decimal'])
        plt.title('Factor_4')
        plt.xlabel('total_winning_streak')
        plt.ylabel('total_win_decimal')
        plt.show()

    def factor_5_graph():
        plt.scatter(data['ground_attempts_pct'], data['total_win_decimal'])
        plt.title('Factor_5')
        plt.xlabel('ground_attempts_pct')
        plt.ylabel('total_win_decimal')
        plt.show()

## User input codes

def user_inputs():
    value = input("Please enter your directory code: ")
    if value == 1:
        correlations.group_corr()
    if value == 2:
        simple_statistics.five_factor_coefficients()
    if value == 3:
        simple_statistics.mean_std_confidence_interval()
    if value == 4:
        ols_models.ols_1()
    if value == 5:
        ols_models.ols_2()
    if value == 6:
        ols_models.ols_3()
    if value == 7:
        ols_models.ols_4()
    if value == 8:
        ols_models.ols_5()
    if value == 9:
        ols_models.combined_ols_model()
    if value == 10:
        mapping.pairplot_output()
    if value == 11:
        mapping.factor_1_graph()
    if value == 12:
        mapping.factor_2_graph()
    if value == 13:
        mapping.factor_3_graph()
    if value == 14:
        mapping.factor_4_graph()
    if value == 15:
        mapping.factor_5_graph()

user_inputs()
## Part 4 Profile of a Fighter

## Using class and inheritance to build a full profile of fighter statistics
## given input data.  This lets users input specific details of fighter
## for future record keeping and searching.  Can be combined with databases to
## update information on active fighters.  Custom library is used to grab "Basic"
## and "Performance" information.  

class Fighter(Basic, Performance):
    def getProfile(self):
        print("Name: ", self.name)
        print("Gender: ", self.gender)
        print("Age: ", self.age)
        print("Height :", self.height)
        print("Weight: ", self.weight)
        print("Stance: ", self.stance)
        print("Wins: ", self.wins)
        print("Losses: ", self.losses)
        print("Ties: ", self.ties)
        print("Win Record: ", self.wins_record)
        print("Division: ", self.division)
        
    def isFighter(self):
        if self.name == name:
            return TRUE
        else:
            return FALSE

## Since information on UFC fighters can be divided by weight class, gender and
## time period, it is important to search as quickly and efficiently as
## possible.  For this, a binary tree can be carried out.  Data can be added
## to the below to have a set of data that can searched quickly.  Example sends
## output to a text file for convienent record keeping when running the program.
## Works for quantitative statistics that can be sorted.  

class fighter_tree:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert_fight_data(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = fighter_tree(data)
                else:
                    self.left.insert_fight_data(data)
            elif data > self.data:
                if self.right is None:
                    self.right = fighter_tree(data)
                else:
                    self.right.insert_fight_data(data)
        else:
            self.data = data

    def get_fighter_tree(self):
        if self.left:
            self.left.get_fighter_tree()
        with open ('ufc_output.txt', 'w') as file:
            print(self.data)
        if self.right:
            self.right.get_fighter_tree()
        












