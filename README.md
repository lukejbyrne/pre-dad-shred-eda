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
![Image Alt text](/Daily/Heatmap/Figure1.png "Daily Heatmap"))
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
![Image Alt text](/Weekly/Heatmap/Figure1.png "Weekly Heatmap"))
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
![Image Alt text](/Daily/Pairplot/Figure136.png "Daily Pair Plot"))
| Variable 1 | Variable 2 | Correlation | Comments |
|------------|------------|-------------|----------|
| Gym Sessions | Cardio Calories from Fitbit | None | No clear correlation, suggesting gym sessions may not strongly relate to calories burned during cardio activities as per Fitbit. |
| Gym Sessions | Steps | None | No correlation observed between gym sessions and the number of steps taken. |
| Gym Sessions | Kcal (presumably calorie intake) | None | The plot indicates no discernible pattern, implying gym sessions may not be directly related to calorie intake. |
| Gym Sessions | Kcals in (calories ingested) | None | Similar to the previous, no apparent correlation is observed. |
| Gym Sessions | Net Kcals (calories burned vs. ingested) | None | Lack of a clear trend suggests gym sessions may not consistently affect net calories. |
| Gym Sessions | Weight | None | No clear correlation, implying gym session frequency alone may not predict weight changes effectively. |
| Cardio Calories from Fitbit | Steps | Slight positive | Suggests a slight positive correlation; as steps increase, cardio calories recorded by Fitbit also tend to increase. |
| Cardio Calories from Fitbit | Kcal | None | No clear correlation found, indicating calories burned during cardio may not directly relate to overall calorie intake. |
| Cardio Calories from Fitbit | Kcals in (calories ingested) | None | Lack of a clear pattern suggests a straightforward relationship between calories burned during cardio and calories ingested is not present. |
| Cardio Calories from Fitbit | Net Kcals | Negative | Indicates a negative correlation; as net calories decrease (more burned than ingested), cardio calories from Fitbit tend to increase. |
| Cardio Calories from Fitbit | Weight | None | No evident correlation observed, suggesting cardio calories from Fitbit may not directly impact weight changes. |
| Steps | Kcal | None | No correlation between the number of steps and calorie intake. |
| Steps | Kcals in (calories ingested) | None | Steps taken are not strongly related to calories ingested. |
| Steps | Net Kcals | Slight negative | A slight negative correlation might be present; an increase in steps could possibly correspond to a decrease in net calories. |
| Steps | Weight | None | Number of steps alone is not a direct predictor of weight changes. |
| Kcal | Kcals in (calories ingested) | Positive | Likely a strong positive correlation as both variables are likely related, dealing with calorie intake. |
| Kcal | Net Kcals | Negative | A negative correlation might be present; an increase in calorie intake could lead to an increase in net calorie surplus. |
| Kcal | Weight | None | Calorie intake alone does not predict weight changes effectively. |
| Kcals in (calories ingested) | Net Kcals | Negative | Likely a negative correlation; higher calorie ingestion might increase the net calorie surplus. |
| Kcals in (calories ingested) | Weight | None | No clear pattern found, suggesting calorie ingestion doesn't straightforwardly relate to weight changes. |
| Net Kcals (calories burned vs. ingested) | Weight | Slight negative | A slight negative correlation might exist; as net calories decrease (indicating a deficit), weight might also decrease. |


In my analysis, I found that gym sessions alone didn't significantly impact cardio calorie burn or step count. However, increasing daily steps showed a slight positive correlation with higher cardio calorie expenditure, suggesting a focus on incorporating more physical activity throughout the day. Furthermore, increased expenditure correlated with slightly higher caloric intake, highlighting the importance of maintaining a balanced approach to diet and exercise. While no direct correlation was observed between caloric intake and weight changes, creating a moderate calorie deficit led to slight weight loss. This deficit, in turn, may have been influenced by a combination of increased physical activity and mindful dietary habits. Thus, managing net calories effectively becomes paramount for achieving sustained weight loss success.

### Weekly Trends
![Image Alt text](/Weekly/Pairplot/Figure2.png "Weekly Pair Plot"))
| Variable 1 | Variable 2 | Correlation | Comments |
|------------|------------|-------------|----------|
| Weekly Cardio (kcal) | Weekly Steps | Positive | More steps may correlate with higher energy expenditure in calories. |
| Weekly Cardio (kcal) | Weekly Average (kcal) | Positive | Higher cardio in kcal correlates with a higher weekly average caloric intake. |
| Weekly Cardio (kcal) | Weekly Difference (kcal) | Negative | Higher cardio leads to a larger calorie deficit as weekly cardio increases. |
| Weekly Cardio (kcal) | Mean Weight | None | No correlation between weekly cardio and mean weight, suggesting other factors affect weight. |
| Weekly Cardio (kcal) | Median Weight | None | No clear trend between weekly cardio and median weight. |
| Weekly Steps | Weekly Average (kcal) | None | No direct relationship between weekly steps and average caloric intake. |
| Weekly Steps | Weekly Difference (kcal) | Negative | Increased steps may be associated with a calorie deficit. |
| Weekly Steps | Mean Weight | None | Weekly steps do not show a direct correlation with mean weight. |
| Weekly Steps | Median Weight | None | No clear correlation between weekly steps and median weight. |
| Weekly Average (kcal) | Weekly Difference (kcal) | Negative | Higher caloric intake correlates with a reduced calorie deficit. |
| Weekly Average (kcal) | Mean Weight | None | No clear correlation between average caloric intake and mean weight. |
| Weekly Average (kcal) | Median Weight | None | No pattern between weekly average caloric intake and median weight. |
| Weekly Difference (kcal) | Mean Weight | Positive | A calorie surplus is associated with a higher mean weight. |
| Weekly Difference (kcal) | Median Weight | Positive | A calorie surplus correlates with a higher median weight. |
| Mean Weight | Median Weight | Positive | Strong correlation as both are measures of central tendency from the same weight data. |

This analysis suggests that while there is a positive correlation between cardio activity and steps with energy expenditure, these factors are not directly correlated with weight. Caloric intake and net calories are more directly related to weight changes, highlighting the need to balance diet and exercise in weight management.

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