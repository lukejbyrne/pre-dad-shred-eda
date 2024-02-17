# TL;DR
In this analysis of a 12-week weight management journey documented through MyFitnessPal and Apple Numbers, we employed Exploratory Data Analysis (EDA) techniques to dissect daily and weekly data sets on calorie intake, expenditure, and physical activity. 

The study reveals a strong positive correlation (r=0.89) between steps taken and calories expended daily, underscoring the significant impact of walking on calorie burn. Weekly analysis echoed this pattern, showing a consistent relationship between physical activity levels and caloric output. Additionally, a notable finding was the strong correlation between daily calorie intake and net caloric difference (r=0.77), suggesting that higher food consumption did not deter a caloric deficit, likely due to an increase in non-exercise activity thermogenesis (NEAT). However, gym sessions showed only a weak to moderate correlation with both calorie expenditure and intake, hinting at their lesser role in overall weight management compared to daily walking. 

The analysis, enriched with visual aids like heatmaps and scatter plots, not only offers insights into effective weight management strategies but also enhances my coding and data science skills. This journey through data underscores the pivotal role of consistent, moderate activity—like walking—in achieving a caloric deficit and managing weight effectively.

# Quickstart
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
Before the birth of my son I sought to lose some weight under the knowledge that weight management would be at the back of my mind during his first few months of his life. I meticulously documented this 12 week 'shred' across MyFitnessPal and an Apple Numbers workbook, noting key values in relation to calorie intake and expenditure.

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

In analyzing the scatterplots, certain plots were more indicative of potential correlations, especially when considering the hue variable, which adds a dimension of categorization to the analysis. Below are the key findings from the plots that warranted further inspection.

#### Noteworthy Scatterplots:

- **Weight vs. Kcals in/out (Hue: Gym Sessions)**: These plots showed a clustering of data points that varied with the number of gym sessions. This suggests that gym activity may interact with the relationship between caloric intake/outtake and weight, potentially highlighting the role of exercise in weight management.

- **Kcals out vs. Cardio (kcals from Fitbit) (Hue: Net Diff (kcals))**: There was a visible trend where individuals with higher net calorie deficits tended to have higher calories burned according to Fitbit data. This could indicate an effective tracking of increased physical activity leading to larger calorie deficits.

- **Steps vs. Cardio (kcals from Fitbit) (Hue: Kcals in)**: The plot indicated a moderate correlation between steps and calories burned during cardio, differentiated by daily calorie intake. It suggests that those with higher caloric intake might also be more active, which could be related to higher energy availability.

#### Omitted Scatterplots and Reasons:

- **Scatterplots with no discernible patterns**: Some plots showed a random dispersion of points without any apparent correlation or interaction effect with the hue variable. These plots were omitted from detailed analysis as they are less likely to yield actionable insights without further statistical testing.

- **Scatterplots with sparse data**: In cases where the data points were too sparse, it was challenging to draw any conclusions about correlations or the effect of the hue variable. These were also omitted as they do not provide a reliable basis for analysis.

- **Overplotted Scatterplots**: Some scatterplots had significant overplotting, making it difficult to visually assess the distribution of data points and any potential correlation. These require further analysis with techniques such as transparency adjustment, jittering, or alternative visualization methods to properly interpret the data.

#### Recommendations for Further Investigation:

- **Statistical Testing**: For scatterplots indicating potential correlations, it is advisable to conduct statistical tests, such as Pearson or Spearman correlation coefficients, to quantify the strength and direction of the relationships.

- **Regression Analysis**: Including the hue variable as a factor in regression models could provide insights into how it moderates the relationships between the primary variables.

- **Subgroup Analysis**: For variables where the hue indicated meaningful differences, subgroup analysis could further explore the characteristics and behaviors of these distinct groups.

The scatterplots suggest interesting relationships between daily activities, caloric balance, and weight, especially when considering additional factors such as gym sessions. However, these visual analyses should be augmented with rigorous statistical methods to confirm the findings and understand the underlying dynamics.

### Weekly Trends
The scatterplot analysis for weekly data reflects the aggregation of daily activities into longer-term patterns. The following are key observations from the plots that showed potential correlations or were particularly influenced by the hue variable.

#### Noteworthy Scatterplots:

- **Weekly Cardio (kcals) vs. Weekly Steps (Hue: Weight)**: There was a more pronounced correlation in the weekly data for cardio activity and steps compared to the daily data. The inclusion of weight as a hue variable revealed a stratification where individuals with higher body weight had a different pattern of activity, suggesting a relationship between weight and exercise habits.

- **Mean Weight vs. Weekly Average (kcals) (Hue: Net Diff (kcals))**: This plot showed a clearer trend on a weekly scale, with mean weight appearing to correlate with weekly calorie intake, especially when considering net calorie difference. It suggests that weekly dietary habits might have a more direct impact on weight fluctuations compared to daily variations.

- **Median Weight vs. Weekly Body Weight Loss % (Hue: Gym Sessions)**: The presence of gym sessions as a hue showed that individuals with more frequent gym sessions had a notable weight loss percentage, which was not as apparent in the daily data. This could indicate that the benefits of regular exercise on weight loss are more observable on a weekly scale.

#### Omitted Scatterplots and Reasons:

- **Scatterplots with Indistinct Patterns**: Several plots did not show any clear correlation or interaction with the hue variable, which made them less informative for this analysis. Without clear trends, these plots do not contribute significantly to understanding the weekly habits and their outcomes.

- **Scatterplots with Sparse Data Points**: As with the daily data, some weekly scatterplots suffered from sparsity, making it difficult to discern any reliable patterns. These were excluded from detailed analysis due to the risk of drawing misleading conclusions from insufficient data.

- **Scatterplots with Overlapping Points**: Overlapping data points in some scatterplots obscured any potential patterns, especially concerning the hue variable. These require more sophisticated visualization techniques to interpret the data accurately.

#### Comparative Insights:

- The weekly data seems to smooth out the daily variability, revealing trends that are less clear when looking at daily behaviors. This is particularly evident in the relationship between caloric intake/outtake and weight metrics.

- The role of exercise, as evidenced by gym sessions, seems more influential on a weekly basis. This might be due to the cumulative effect of exercise over a week being more measurable than day-to-day fluctuations.

- Weekly patterns offer a more stable basis for analyzing lifestyle impacts on weight and activity levels, suggesting that long-term habits are more indicative of health outcomes than daily variations.

The analysis of weekly scatterplots reinforces the importance of examining data over various time scales to capture different aspects of behavior and outcomes. While daily data provides granularity, weekly data offers a broader view, which may be more aligned with long-term goals such as weight management or fitness improvement.

## Histogram
### Daily Trends

Histograms are visual representations of the distribution of a dataset. Below is an analysis of the histograms for various variables of the daily data set:

#### Weight
![Weight Histogram](sandbox:/mnt/data/histograms/Histogram/Weight/Figure406.png)
- The histogram for weight shows a distribution that might be normally distributed or slightly skewed to the right. The central tendency is around the middle of the x-axis, with no apparent outliers. This suggests a healthy variation in the population's weight.

#### Gym Sessions
![Gym Sessions Histogram](sandbox:/mnt/data/histograms/Histogram/Gym Sessions/Figure394.png)
- The distribution of gym sessions is highly positively skewed, with most values clustered at the lower end. This indicates that most individuals have few gym sessions, with a small number attending the gym more frequently.

#### Net Diff (kcals)
![Net Caloric Difference Histogram](sandbox:/mnt/data/histograms/Histogram/Net Diff (kcals)/Figure404.png)
- This histogram appears to be somewhat symmetrical around the zero mark. A substantial number of individuals have a net caloric difference close to zero, suggesting a balance between caloric intake and expenditure.

#### Date
![Date Histogram](sandbox:/mnt/data/histograms/Histogram/Date/Figure390.png)
- It is unusual to have a histogram for dates, as they are not typically a variable that is distributed. This histogram might be indicating the frequency of data entries over time.

#### Steps
![Steps Histogram](sandbox:/mnt/data/histograms/Histogram/Steps/Figure398.png)
- The histogram for steps taken is positively skewed, showing that most people take a moderate number of steps, with a few individuals taking significantly more. This is a common pattern for physical activity data.

#### Gym
![Gym Histogram](sandbox:/mnt/data/histograms/Histogram/Gym/Figure392.png)
- This histogram likely represents the frequency of gym attendance and appears to show a distribution similar to that of gym sessions, which is positively skewed.

#### Kcals out
![Calories Out Histogram](sandbox:/mnt/data/histograms/Histogram/Kcals out/Figure400.png)
- The calories burned histogram is positively skewed, indicating that while most individuals burn a moderate amount of calories, there are a few who burn significantly more.

#### Cardio (kcals from Fitbit)
![Cardio Calories Histogram](sandbox:/mnt/data/histograms/Histogram/Cardio (kcals from Fitbit)/Figure396.png)
- The distribution of calories burned during cardio activities, as recorded by Fitbit devices, is positively skewed. This suggests that most participants are not engaging in high-calorie-burning cardio activities frequently.

#### Kcals in
![Caloric Intake Histogram](sandbox:/mnt/data/histograms/Histogram/Kcals in/Figure402.png)
- Caloric intake is normally distributed, which is typical for dietary data. There are no significant outliers, and the spread of calorie intake is moderate.

These histograms provide a snapshot of the daily behaviors and outcomes of the individuals in the dataset. Notably, the skewness in the physical activity-related histograms (gym sessions, steps, kcals out) highlights the variation in activity levels among individuals, while the symmetry in the net calorie difference suggests a balance in caloric intake and expenditure for most individuals.

### Weekly Trends

Histograms for weekly data allow us to see the aggregated behavior over a longer period than daily histograms. Here's an analysis of the weekly histograms, with references to the daily data where relevant:

#### Weekly Mean difference (kcals)
![Weekly Mean Difference Histogram](sandbox:/mnt/data/histograms/Histogram/Weekly Mean difference (kcals)/Figure115.png)
- The histogram for the weekly mean difference in kcal shows a normal distribution centered around zero, similar to the daily net difference. This suggests that over a week, individuals tend to balance their caloric intake and expenditure.

#### Weekly Body Weight loss %
![Weekly Body Weight Loss Percentage Histogram](sandbox:/mnt/data/histograms/Histogram/Weekly Body Weight loss %/Figure121.png)
- This histogram is skewed to the right, indicating that most individuals have a small percentage of weight loss per week, with a few experiencing higher percentages. This pattern is less evident in the daily weight histogram, which is more symmetric.

#### Weekly average (kcals)
![Weekly Average Caloric Intake Histogram](sandbox:/mnt/data/histograms/Histogram/Weekly average (kcals)/Figure113.png)
- The weekly average kcal intake appears to be normally distributed, suggesting consistent eating habits when viewed on a weekly basis compared to the daily kcal intake histogram, which also showed a normal distribution.

#### Weekly Steps
![Weekly Steps Histogram](sandbox:/mnt/data/histograms/Histogram/Weekly Steps/Figure111.png)
- The distribution of weekly steps is positively skewed, much like the daily steps histogram. It indicates that while most people have a moderate level of activity, there are a few who are much more active.

#### Weekly Cardio (kcals)
![Weekly Cardio Calories Histogram](sandbox:/mnt/data/histograms/Histogram/Weekly Cardio (kcals)/Figure109.png)
- Calories burned through cardio activities on a weekly basis are also positively skewed. This suggests that most people do not burn a high number of calories through cardio weekly, which is in line with the daily cardio calories histogram.

In comparing the daily and weekly histograms, it's evident that the weekly data smooth out some of the daily variations but maintain the same overall patterns in behavior. The weekly perspective can be particularly useful for identifying long-term trends and ensuring that daily fluctuations do not obscure overall habits and outcomes.

## Cat Plot
### Daily Trend

Catplots are useful for examining the distribution of a numerical variable across the levels of a categorical variable. Here's an analysis of the daily data catplots:

#### Weight
![Weight Catplot](sandbox:/mnt/data/catplots/Catplot/Weight/Figure424.png)
- The catplot for weight likely shows variations across different categories, such as demographic groups or time periods. This visualization helps identify outliers or specific trends within subgroups.

#### Gym Sessions
![Gym Sessions Catplot](sandbox:/mnt/data/catplots/Catplot/Gym Sessions/Figure412.png)
- The distribution of gym sessions can be seen across various categories with this catplot. It would be particularly useful for comparing the frequency of gym visits among different cohorts or across different days of the week.

#### Net Diff (kcals)
![Net Caloric Difference Catplot](sandbox:/mnt/data/catplots/Catplot/Net Diff (kcals)/Figure422.png)
- This catplot may illustrate daily net caloric difference across categories such as meal types or activity levels. It can help in identifying dietary patterns that lead to a caloric surplus or deficit.

#### Date
![Date Catplot](sandbox:/mnt/data/catplots/Catplot/Date/Figure408.png)
- A catplot for dates might show the frequency or distribution of another variable by date, which can be useful for tracking changes over time or identifying seasonal trends.

#### Steps
![Steps Catplot](sandbox:/mnt/data/catplots/Catplot/Steps/Figure416.png)
- The catplot for daily steps allows us to compare activity levels across different groups or conditions. This can highlight variations in physical activity based on factors like work schedule or weather conditions.

#### Gym
![Gym Catplot](sandbox:/mnt/data/catplots/Catplot/Gym/Figure410.png)
- Similar to the gym sessions catplot, this could reflect the number of individuals attending the gym across different categories, showing how gym attendance varies among different segments of the population.

#### Kcals out
![Calories Out Catplot](sandbox:/mnt/data/catplots/Catplot/Kcals out/Figure418.png)
- This catplot for daily calories burned is useful for examining variations in energy expenditure across different categories, which could be influenced by varying levels of physical activity or exercise routines.

#### Cardio (kcals from Fitbit)
![Cardio Calories Catplot](sandbox:/mnt/data/catplots/Catplot/Cardio (kcals from Fitbit)/Figure414.png)
- The calories burned during cardio as recorded by Fitbit devices can be compared across different user groups or timeframes to assess the impact of cardio activities on overall calorie expenditure.

#### Kcals in
![Caloric Intake Catplot](sandbox:/mnt/data/catplots/Catplot/Kcals in/Figure420.png)
- This catplot visualizes daily caloric intake across different categories, which can be insightful for nutritional studies or to track the effectiveness of dietary interventions.

These catplots offer a granular view of daily behaviors and can be used to detect patterns that might be specific to certain groups or time periods. When compared to the weekly data, they provide a more detailed snapshot, which can be essential for understanding day-to-day variability within the context of broader trends.

### Weekly Trends

The weekly catplots allow for an examination of patterns and distributions over a longer time scale compared to daily catplots. Here's the analysis:

#### Weekly Mean difference (kcals)
![Weekly Mean Difference Catplot](sandbox:/mnt/data/catplots/Catplot/Weekly Mean difference (kcals)/Figure129.png)
- This catplot may show the weekly mean difference in kcals across different categories, such as participant groups or weeks in a study. It can help identify which groups or time periods have higher or lower mean caloric differences compared to the daily analysis, which might show more variability.

#### Weekly Body Weight loss %
![Weekly Body Weight Loss Percentage Catplot](sandbox:/mnt/data/catplots/Catplot/Weekly Body Weight loss %/Figure135.png)
- The catplot for weekly body weight loss percentage likely displays the distribution of weight loss across various categories. Comparing to daily data, this weekly aggregation could reveal more consistent trends in weight loss that are not as apparent in daily fluctuations.

#### Weekly average (kcals)
![Weekly Average Caloric Intake Catplot](sandbox:/mnt/data/catplots/Catplot/Weekly average (kcals)/Figure127.png)
- This visualization provides insight into the average caloric intake on a weekly basis. Unlike daily caloric intake, which may be subject to day-to-day changes, the weekly view could present a more stable pattern of dietary behavior.

#### Weekly Steps
![Weekly Steps Catplot](sandbox:/mnt/data/catplots/Catplot/Weekly Steps/Figure125.png)
- Weekly steps can be compared across categories to assess activity levels. While daily steps might be influenced by immediate factors like weather or schedule, weekly steps can smooth out these effects to show a clearer pattern of physical activity.

#### Weekly Cardio (kcals)
![Weekly Cardio Calories Catplot](sandbox:/mnt/data/catplots/Catplot/Weekly Cardio (kcals)/Figure123.png)
- This catplot shows the calories burned from cardio activities on a weekly basis. The comparison to daily data might indicate whether individuals are consistently engaging in cardio activities throughout the week or if there's a tendency to concentrate activity on certain days.

These catplots provide a more aggregated perspective on the participants' behaviors and trends. When compared to daily catplots, they can offer insights into the consistency of behaviors and outcomes over time, smoothing out daily variations to reveal broader patterns.

# Conclusion
In summarizing the extensive 12-week weight management journey, this analysis through Exploratory Data Analysis (EDA) techniques has illuminated the substantial impact of daily physical activities, particularly walking, on caloric expenditure and weight management. The daily and weekly analyses consistently showcased a strong positive correlation between the number of steps taken and calories burned, reinforcing the importance of consistent, moderate activity in achieving a caloric deficit. Interestingly, while gym sessions contribute to overall fitness, their correlation with calorie expenditure and intake was relatively weak to moderate, suggesting that daily walking plays a more pivotal role in weight management.

The notable correlation between increased calorie intake and a net caloric difference highlights the complex dynamics of eating more and its potential to not adversely affect, and possibly even support, a caloric deficit, likely through mechanisms such as NEAT. This insight challenges conventional wisdom and suggests a nuanced approach to dieting where caloric intake can be strategically managed to support weight loss efforts.

Moreover, the analysis has not only offered valuable insights into effective weight management strategies but has also served as a learning journey in data science and coding skills enhancement. It underscores the importance of leveraging data to inform health and fitness strategies, providing a data-driven approach to understanding personal health and fitness behaviors.

Future directions could involve refining data collection and analysis methods, such as incorporating more granular data on diet composition and exploring the impact of specific types of physical activity beyond walking and gym sessions. Additionally, further investigations could examine the psychological and behavioral aspects of diet and exercise to provide a more holistic view of weight management. This journey through data underscores the power of consistent, moderate activity and a balanced approach to diet in managing weight effectively, providing a foundation for future exploration and learning in the realms of health, fitness, and data science.

## TODO: Improvements
- Absoluted negative values? | -x | == x
- Add a column for number of gym sessions
- Name better columns, e.g. deficit instead of weekly diff