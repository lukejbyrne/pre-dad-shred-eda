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

#### Weight Correlations
| Variable | Variable | Correlation |
|---|---|---|
| Cardio (kcals from Fitbit) | Weight | 0.317056 |
| Steps | Weight | 0.132588 |
| Kcals out | Weight | 0.108954 |
| Gym Sessions | Weight | -0.044626 |
| Kcals in | Weight | -0.067921 |
| Net Diff (kcals) | Weight | -0.074647 |

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
| Mean Weight | Median Weight | 0.999273 |
| Weekly average (kcals) | Weekly Mean difference (kcals) | 0.868265 |
| Weekly Cardio (kcals) | Weekly Steps | 0.749254 |

##### Moderate Positive Correlations


##### Weak Positive Correlations
| Weekly Steps | Median Weight | 0.321766 |
| Weekly Steps | Mean Weight | 0.313640 |
| Weekly Cardio (kcals) | Weekly average (kcals) | 0.310491 |

##### Moderate Negative Correlations
| Weekly Cardio (kcals) | Weekly Mean difference (kcals) | -0.257348 |
| Weekly Steps | Weekly Mean difference (kcals) | -0.426789 |

#### Weight Correlations
| Variable | Variable | Correlation |
|---|---|---|
| Mean Weight | Median Weight | 0.999273 |
| Weekly Steps | Median Weight | 0.321766 |
| Weekly Steps | Mean Weight | 0.313640 |
| Weekly Cardio (kcals) | Median Weight | 0.264878 |
| Weekly Cardio (kcals) | Mean Weight | 0.244940 |
| Weekly average (kcals) | Median Weight | 0.013942 |
| Weekly average (kcals) | Mean Weight | -0.010711 |
| Weekly Mean difference (kcals) | Median Weight | -0.080961 |
| Weekly Mean difference (kcals) | Mean Weight | -0.104662 |

### Conclusion

## Pair Plot
### Daily Trends
![Image Alt text](/Daily/Pairplot/Figure136.png "Daily Pair Plot"))
### Weekly Trends
![Image Alt text](/Weekly/Pairplot/Figure2.png "Weekly Pair Plot"))

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