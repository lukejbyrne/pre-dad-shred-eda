# To Run
Run eda.py in python3 to give the below main menu:
``` Please enter: 
1  - Understand Data
2a - Clean (daily)
2b - Clean Data (weekly)
3  - Relationship Analysis - Heatmap
4  - Relationship Analysis - Pairplot
5  - Relationship Analysis - Scatterplot
6  - Relationship Analysis - Histogram
7  - Relationship Analysis - Catplot
r  - Reset data
q  - Quit
```
From this menu, to get the Heatmap for daily enter 2a to remove all non-daily columns, after which any of 3 -> 7 may be performed by entering the number when prompted. It does not matter in which order these are run as they do not interfere with one another.

To then run weekly analysis, enter r to reset the columns, then 2b for the weekly data. 

The resultant from each step is output into there associated folders, e.g. Daily/Heatmap (which are created if they do not already exist).

# Introduction
Before the birth of my son I sought to lose some weight under the knowledge that weight management would be at the back of my mind during his first few months of life. I meticulously documented this 12 week 'shred' across MyFitnessPal and an Apple Numbers workbook, noting key values in relation to calorie intake and expenditure.

## Motivation
Now having this data I thought it an informative exercise to
1) Learn from my mistakes for future 'cuts' / 'shreds'
2) Find key measurements that interrupt the sustainability of the diet
3) Learn some Data Science along the way
4) Brush up on coding skills

# Methodology
This analysis covers a variety of analytical tools under the guise of Exploratory Data Analysis. In the vein of novel exploration, I opted to derive patterns and correlations from combinations of all data as opposed to seeking correlations between specific sets. Within the repo you will find the python file/s utilised for the data analysation preperations, as well as the resulting files which are analysed in the next chapter.

The resulting files I mention are under 5 data analysation methods each for 2 sets of data. My original data had a combination of daily and weekly values. This I opted to seperate to look distinctly at Daily and then Weekly. Within each of these I analysed:

1) Heatmap
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.corr.html#pandas-dataframe-corr

    By default utilises Pearson's correlation coefficient
Each square shows the correlation between the variables on each axis. Correlation ranges from -1 to +1. Values closer to zero means there is no linear trend between the two variables. The close to 1 the correlation is the more positively correlated they are; that is as one increases so does the other and the closer to 1 the stronger this relationship is. A correlation closer to -1 is similar, but instead of both increasing one variable will decrease as the other increases.
2) Pair Plot
3) Scatter Plot
4) Histogram
5) Cat Plot

# Data Analysis
## Heatmap
### Daily Trends
![Image Alt text](/Daily/Heatmap/Figure1.png "Daily Heatmap")
#### Exploratory

example analysis: whereas theres a positive correlation with steps, how does this actually affect expenditure? well I seem to eat more with the negative correlation...


| Variable | Variable | Correlation |
|---|---|---|
| Steps | Kcals out | 0.890501 |
| Kcals in | Net Diff (kcals) | 0.766737 |
| Cardio (kcals from Fitbit) | Steps | 0.620473 |
| Cardio (kcals from Fitbit) | Kcals out | 0.559458 |
| Cardio (kcals from Fitbit) | Kcals in | 0.405526 |
| Gym Sessions | Steps | 0.396649 |
| Kcals out | Kcals in | 0.360828 |
| Gym Sessions | Kcals out | 0.355770 |
| Gym Sessions | Kcals in | 0.354038 |
| Cardio (kcals from Fitbit) | Weight | 0.317056 |
| Steps | Kcals in | 0.234515 |
| Steps | Weight | 0.132588 |
| Kcals out | Weight | 0.108954 |
| Cardio (kcals from Fitbit) | Net Diff (kcals) | -0.011243 |
| Gym Sessions | Cardio (kcals from Fitbit) | -0.027156 |
| Gym Sessions | Weight | -0.044626 |
| Kcals in | Weight | -0.067921 |
| Net Diff (kcals) | Weight | -0.074647 |
| Gym Sessions | Net Diff (kcals) | -0.130072 |
| Kcals out | Net Diff (kcals) | -0.359683 |
| Steps | Net Diff (kcals) | -0.438042 |

##### Positive Correlations
Number of steps correlates very highly with calories out (0.89), implying that it is by far the greatest means of expending calories, versus specific gym sessions or cardio. Regarding gym sessions it would be interesting if the number of sessions weekly correlates and if this correlation would hold up on the weekly average timescale.

Calories in is strongly correlated with a net difference in calories (0.77), implying the more I eat, the larger the net difference in calories. This finding in isolation appears thus that eating more would in turn cause a larger deficit. However, as per discussions in the field this is likely a byproduct of NEAT (Non-exercise Activity Thermogenisis), whereby we unconsciously move more during day to day activities due to the increase in calorie. Under this hypothesis there is likely to be a sweet spot. To conclude this we may look for a bell shaped curve in the Pair plot as more calories in would equal more out until a point at which this net difference would begin to close.

##### Moderate Positive Correlations
| Cardio (kcals from Fitbit) | Steps | 0.620473 |
| Cardio (kcals from Fitbit) | Kcals out | 0.559458 |

Moderately positive correlations are found between calories burned from cardio and steps (0.62) and calories out (0.56). The implications being that the majority of steps would appear to come from cardio and that second to steps in influencing calories out would be cardio. This would make sense as most cardio sessions were in fact varieties of treadmill walking (incline / flat).

##### Weak Positive Correlations
| Cardio (kcals from Fitbit) | Kcals in | 0.405526 |
| Gym Sessions | Steps | 0.396649 |

Whilst cardio is positiviely correlated with calories out (0.56), it is weakly correlated to calories in (0.41). This could be expected as I had a weekly alotment of calories to burn (e.g. 600) and could choose the days on which to do brun them. It would be interesting to see the correlation of cardio vs kcals in of day before, to see if an increase in calories in one day leads to guilt and recouperation of fat loss the following day.

Gym sessions also had a week positive correlation to steps (0.40), which is to be expected as it would be positive correlated due to the walking in the gym between machines / sets / etc. However the correlation is likely to be weak due to the percentage of total daily steps this would cover as most cardio was walking (steps).

##### Moderate Negative Correlations
| Kcals out | Net Diff (kcals) | -0.359683 |
| Steps | Net Diff (kcals) | -0.438042 |

Notable negative corelations existed between net difference in calories and calories out (-0.36) and net difference and steps (-0.44). The former can be ignored as an obvious byproduct of dieting where calories in are controlled by calories out are allowed to fluctuate. The latter is expected as the steps was positively correlated with calories out, if calories in are equated for then net difference gap would increase (as a negative value calculated as calories in - out), therefore creating a larger deficit. Interesitingly however this negative correlation is less than half of the positive between steps and calories in. I believe this to be because steps are correlated slightly positively with calories in (0.23), offsetting the large calorie expenditure by some.

#### Weight Correlations
| Variable | Variable | Correlation |
|---|---|---|
| Cardio (kcals from Fitbit) | Weight | 0.317056 |
| Steps | Weight | 0.132588 |
| Kcals out | Weight | 0.108954 |
| Gym Sessions | Weight | -0.044626 |
| Kcals in | Weight | -0.067921 |
| Net Diff (kcals) | Weight | -0.074647 |

As the purpose of this investigation is ultimately to uncover how to 'shred' better, it would go incomplete if the analysis of variables on weight were missed.

It would appear from the findings that number of gym sessions, calories in, and net difference are negatively (albeit very slightly)

### Weekly Trends
![Image Alt text](/Weekly/Heatmap/Figure1.png "Weekly Heatmap")
#### Exploratory
| Variable | Variable | Correlation |
|---|---|---|
| Mean Weight | Median Weight | 0.999273 |
| Weekly average (kcals) | Weekly Mean difference (kcals) | 0.868265 |
| Weekly Cardio (kcals) | Weekly Steps | 0.749254 |
| Weekly Steps | Median Weight | 0.321766 |
| Weekly Steps | Mean Weight | 0.313640 |
| Weekly Cardio (kcals) | Weekly average (kcals) | 0.310491 |
| Weekly Cardio (kcals) | Median Weight | 0.264878 |
| Weekly Cardio (kcals) | Mean Weight | 0.244940 |
| Weekly average (kcals) | Median Weight | 0.013942 |
| Weekly average (kcals) | Mean Weight | -0.010711 |
| Weekly Steps | Weekly average (kcals) | -0.023569 |
| Weekly Mean difference (kcals) | Median Weight | -0.080961 |
| Weekly Mean difference (kcals) | Mean Weight | -0.104662 |
| Weekly Cardio (kcals) | Weekly Mean difference (kcals) | -0.257348 |
| Weekly Steps | Weekly Mean difference (kcals) | -0.426789 |

##### Positive Correlations
With a correlation of 1.00 for mean and median, it's safe to assume that on a long term scale (e.g. 12 weeks) which of the averages you track is not important for accurate measurement. Often median can be favoured, but in this case the difference is negligable.

Weekly calorie intake is highly correlateed with weekly mean difference of calories in - out (0.87). Therefore as intake increases the mean difference increases. This does not mean that more food = larger difference, quite the opposite, as the mean difference is from the reference of calorie intake (in - out), therefore an increase in difference actually means a smaller difference. Which is as expected for a larger calorie intake.

Finally there is a correlation between weekly cardio and stepss (0.75) as expected, for the same reasons as the daily trends.

##### Moderate Positive Correlations
There are no moderate positive correlations with the weekly data.

##### Weak Positive Correlations
There is a weak positive correlation between weekly steps and median (0.32) and mean (0.31) weights. Further demostrating the negligable difference between both weight measurements.

As with the daily trend analysis, cardio is also correlated with calorie intake (0.31).

##### Moderate Negative Correlations
| Weekly Cardio (kcals) | Weekly Mean difference (kcals) | -0.257348 |
| Weekly Steps | Weekly Mean difference (kcals) | -0.426789 |

There is a moderate negative correlation between weekly steps and difference in calories (-0.42), displaying that as increase in steps causes a decrease in difference. As explained previously a decrease in weekly mean difference means a larger value as the value is negative. This could be expected as steps are correlated with higher calorie expenditure on the daily data, and are a source of expenditure. Again, it would be interesting to find how this would affect surrounding days. Does more cardio lead to more food the next day? Or does more food for the day/s prior lead to more cardio?

#### Weight Correlations
| Variable | Median Weight Correlation | Mean Weight Correlation |
|---|---|---|
| Weekly Steps | 0.321766 | 0.313640 |
| Weekly Cardio (kcals) | 0.264878 | 0.244940 |
| Weekly average (kcals) | 0.013942 | -0.010711 |
| Weekly Mean difference (kcals) | -0.080961 | -0.104662 |

The weights in this table are formatted differently to the daily trends data as more insight appears to be able to be drawn when a third variable is added (i.e. allowing us to compare median and mean weights).

Previously I had mentioned that it does not matter which average is use; mean and median. However upon inspection of the weight correlation results it would apear that each variable is more positively correlated with median weight than with mean. For example weekly average calorie intake is positive for median whilst negative for mean. Why?

Additionally, if we analyse the data it would appear that there are no strong correlations between any variables and weight change. This would appear then to display that neither steps, cardio, calorie intake, nor calorie deficit have any correlation to a reduction in weight. However, it is important to realise that we are measuring correlation between variables. That is to say that we are measuring how the change in one affects another. Therefore if we maintain a calorie deficit of 2200kcal across time whilst our weight slowly decreases at say 1lb per week across the 12 week but the ['correlation between these variables would be 0'](refs/Weekly-Weight-Loss.txt), despite losing 12lbs.

### Conclusion

## Pair Plot
### Daily Trends
![Image Alt text](/Daily/Pairplot/Figure136.png "Daily Pair Plot")

#### Observations

- **Gym Sessions and Cardio Calories from Fitbit**: There seems to be little to no correlation between the number of gym sessions and the calories burned during cardio as reported by a Fitbit device. The gym sessions histogram indicates that the data is skewed towards fewer sessions, suggesting that most participants do not frequent the gym often.

- **Steps**: The distribution of steps taken is somewhat positively skewed, indicating that while most participants fall within a moderate range of steps, there are a few with very high step counts. There does not appear to be a strong linear relationship between steps and any other variables.

- **Kcal vs. Cardio Calories and Steps**: The distribution of Kcal intake is roughly normal but shows some outliers or extreme values. The scatterplots do not suggest a clear correlation between Kcal intake and the calories burned during cardio or the number of steps taken.

- **Weight**: Weight distribution appears to be slightly positively skewed, with a concentration of values in the middle of the range. There’s a potential positive correlation between weight and net Kcal, which would be biologically plausible as higher net calorie intake might be associated with higher body weight.

- **Net Kcal (Kcals)**: The histogram of net Kcal shows a normal distribution with a slight negative skew. The negative values in net Kcal suggest that some individuals are in a calorie deficit. There is a visible positive correlation with weight, which is to be expected as typically a sustained calorie surplus would result in weight gain.

#### Concerns

- The presence of outliers, especially in the Kcal intake and net Kcal variables, could affect the correlations. It would be prudent to investigate these outliers to ensure they are not data entry errors.

- The variables 'Cardio Calories from Fitbit' and 'Steps' have some data points that seem to lie on a straight line at certain intervals, which may indicate measurement or data entry artifacts that could warrant further investigation.

#### Recommendations for Further Analysis

- **Correlation Coefficients**: Calculate Pearson or Spearman correlation coefficients to quantify the strength and direction of the relationships between variables.

- **Regression Analysis**: For variables that show potential correlations, perform regression analysis to understand the nature of their relationships better.

- **Outlier Analysis**: Conduct an outlier analysis to identify and potentially remove or adjust for extreme values that could be influencing the results.

- **Time Series Analysis**: If this data is time-series (daily data), analyzing it for trends, seasonality, or cycles could provide additional insights.

- **Cluster Analysis**: To identify distinct patterns or groups within the data, a cluster analysis might be useful, especially if there are subgroups within the population that behave differently.

- **Data Transformation**: For skewed distributions, consider transforming the data (e.g., log transformation) to meet the assumptions of parametric tests if they will be applied.

Overall, while some expected biological patterns are observed, such as the relationship between net calorie intake and weight, other variables do not show strong linear relationships. Caution should be used when interpreting these plots due to potential outliers and artifacts.

### Weekly Trends
![Image Alt text](/Weekly/Pairplot/Figure2.png "Weekly Pair Plot")

This weekly pair plot extends the previous analysis of daily data to a weekly timeframe, providing insights into longer-term trends and patterns.

#### Observations

- **Weekly Cardio (kcal)**: The histogram for weekly cardio calories burned is positively skewed, indicating that most participants burn fewer calories per week, with a few outliers burning significantly more. This weekly pattern is consistent with the daily data, which also showed a positive skew.

- **Weekly Steps**: Similar to the daily data, the weekly steps histogram is positively skewed. The scatterplots do not suggest a strong linear relationship between weekly steps and other variables, just like in the daily data.

- **Weekly Average (kcal)**: The weekly average kcal intake shows a distribution that is less normal compared to the daily data, with a noticeable positive skew. This could suggest variability in eating habits on a weekly basis or reporting inconsistencies.

- **Weekly Kcal Difference**: There's a noticeable range of differences in weekly kcal intake, with a histogram that is fairly symmetrical around zero, indicating that over a week, participants are as likely to be in a caloric surplus as they are to be in a deficit. This differs from the daily data, which showed a slight negative skew, suggesting more frequent daily deficits.

- **Mean vs. Median Weight**: Both mean and median weight distributions are slightly positively skewed, similar to the daily weight observations. However, the weekly mean weight suggests a greater variance compared to the median weight, which could indicate the presence of outliers affecting the mean more than the median.

#### Comparisons to Daily Data

- The weekly data trends appear to follow the daily data trends closely, with similar distributions and patterns. This consistency suggests that the daily habits of individuals are aggregating into similar weekly patterns.

- Weekly caloric difference being symmetrical suggests that day-to-day fluctuations in calorie intake and expenditure might balance out over the course of the week.

- The absence of a strong linear relationship in the weekly data between variables such as steps and kcal intake is also observed in the daily data, suggesting that participants’ physical activity levels may not be closely linked to their caloric intake on both a daily and weekly basis.

#### Recommendations for Further Analysis

- **Compare Averages**: Conduct analysis comparing daily averages to weekly totals to understand how daily habits accumulate over the week.

- **Longitudinal Analysis**: Perform a longitudinal analysis to see if there are consistent weekly patterns over time.

- **Test for Differences**: Use statistical tests such as t-tests or ANOVAs to determine if there are significant differences between daily and weekly values.

- **Correlation Analysis**: Calculate correlation coefficients for weekly data to confirm the lack of strong relationships seen in the scatterplots.

- **Regression Models**: Develop regression models to predict weekly outcomes based on daily habits.

- **Time Series Decomposition**: If this data spans a long time period, decompose the time series to identify and understand seasonal effects or long-term trends.

In summary, the weekly data provides a broader view of participants’ behaviors, showing trends consistent with the daily data. It underscores the absence of strong relationships between activity levels and caloric intake/output, as well as the presence of outliers and variability in weekly patterns.

## Scatter Plot
### Daily Trends
### Weekly Trends

## Histogram
### Daily Trends
### Weekly Trends

## Cat Plot
### Daily Trends
### Weekly Trends

# Conclusion

## TODO: Improvements
- Absoluted negative values? | -x | == x
- Add a column for number of gym sessions
- Name better columns, e.g. deficit instead of weekly diff