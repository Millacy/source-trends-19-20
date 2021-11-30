# Marketing - Source Trends January 2019 - December 2020

## Data & Analysis

### Data Import
Import Numpy, Pandas, and MatPlotLib <p/>
orders = pd.read_csv('Orders.csv') <p/>
sessions = pd.read_csv('Sessions.csv')
"""

#Import Numpy, Pandas, and MatPlotLib
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt

"""### Data Exploration"""

#Set the Orders and Sessions CSVs as new dataframes
orders = pd.read_csv('Orders.csv')
sessions = pd.read_csv('Sessions.csv')

"""Taking a quick look at the .head( ) and .info( ) of each Orders and Sessions dataframes we notice a few things to clean up before diving in.
- For both, the first column is unnamed and should be renamed to "Date" for ease.
- For both, the date should be converted to datetime from object and set as index of the tables for easier grouping.
- Facebook is misspelled as Facbeook, which might cause confusion and errors if not careful.
- For both, the Xs between source and webpages are inconsistent (X vs x) which may throw some errors if not careful.
- For Orders, the counts for Retail Pages are outliers. I will include in this analysis but it certainly raises a red flag.

#### Orders
"""

orders.head()

orders.info()

"""#### Sessions"""

sessions.head()

sessions.info()

"""#### Orders
Taking a quick look at the decription of the Orders dataframe (.describe( )) we notice a few things to attend to: 
- Google seems to have the highest max orders consistently
- The Retails Location Page Orders seem to have the least orders by far
- Snapchat and Direct seem to have the highest standard deviations and therefore variability

"""

orders.describe()

"""#### Sessions 
Taking a quick look at the decription of the Sessions dataframe (.describe( )) we notice a few more things to attend to: 
- Google seems to have the highest max sessions consistently, while Snapchat seems to have the lowest max sessions
- Snapchat also has negative integers consistently across their min sessions and that shouldn't be possible if this is a count
- Retail Locations webpage has cosistently high variability from their standard deviations 
"""

sessions.describe()

"""### <b/> Cleaning Process </b>
- Renaming
- Updating Column Type
- Index Setting 
#### Orders
orders.rename(columns={"Unnamed: 0": "Date"}, inplace = True) <p/>
orders['Date'] = pd.to_datetime(orders['Date']) <p/>
orders.set_index('Date', inplace=True) <p/>
orders.info()
"""

#Rename Order dataframe's unnamed column to "Date"
orders.rename(columns={"Unnamed: 0": "Date"}, inplace = True)

#Change the Orders dataframe's Date column type from
#object to datetime and set the column as the index
orders['Date'] = pd.to_datetime(orders['Date'])
orders.set_index('Date', inplace=True)
orders.info()

"""#### Sessions
sessions.rename(columns={"Unnamed: 0": "Date"}, inplace = True) <p/>
sessions['Date'] = pd.to_datetime(sessions['Date']) <p/>
sessions.set_index('Date', inplace=True) <p/>
sessions.info()
"""

#Rename Sessions dataframe's unnamed column to "Date"
sessions.rename(columns={"Unnamed: 0": "Date"}, inplace = True)

#Change the Sessions dataframe's Date column type from
#object to datetime and set the column as the index
sessions['Date'] = pd.to_datetime(sessions['Date'])
sessions.set_index('Date', inplace=True)
sessions.info()

"""### Aggregating Orders by Marketing Source

#### Orders

Using the following code to combine into new columns: <p/>
(repeated for each source)
- orders['Organic Orders'] = 
- orders['Organic X Bedding Page Orders'] + 
- orders['Organic X Homepage Orders'] + 
- orders['Organic X Mattress Page Orders'] + 
- orders['Organic X Retail Locations Page Orders']  <p/>

** With more time, this code above could be updated with functions to iterate more efficiently and prevent copy+paste errors.
"""

#Combine Bedding, Homepage, Mattresses, and Retails Locations pages into their respective Order Sources 
orders['Organic Orders'] = orders['Organic X Bedding Page Orders'] + orders['Organic X Homepage Orders'] + orders['Organic X Mattress Page Orders'] + orders['Organic X Retail Locations Page Orders']
orders['Direct Orders'] = orders['Direct X Bedding Page Orders'] + orders['Direct X Homepage Orders'] + orders['Direct X Mattress Page Orders'] + orders['Direct X Retail Locations Page Orders']
orders['Google Orders'] = orders['Google Search X Bedding Page Orders'] + orders['Google Search X Homepage Orders'] + orders['Google Search X Mattress Page Orders'] + orders['Google Search X Retail Locations Page Orders']
orders['YouTube Orders'] = orders['YouTube x Bedding Page Orders'] + orders['YouTube x Homepage Orders'] + orders['YouTube x Mattress Page Orders'] + orders['YouTube x Retail Locations Page Orders']
orders['Facebook Orders'] = orders['Facbeook x Bedding Page Orders'] + orders['Facbeook x Homepage Orders'] + orders['Facbeook x Mattress Page Orders'] + orders['Facbeook x Retail Locations Page Orders']
orders['Snapchat Orders'] = orders['Snapchat X Bedding Page Orders'] + orders['Snapchat X Homepage Orders'] + orders['Snapchat X Mattress Page Orders'] + orders['Snapchat X Retail Locations Page Orders']

"""Quick view of the table shows a much more digestible version of the data:"""

#Quick view of the table shows a much more digestible version of the data
orders[["Organic Orders", "Direct Orders", "Google Orders", "YouTube Orders", "Facebook Orders", "Snapchat Orders"]]

#Placed the table into a new variable to work with during visualization and further data manipulation
orders_agg = orders[["Organic Orders", "Direct Orders", "Google Orders", "YouTube Orders", "Facebook Orders", "Snapchat Orders"]]

"""### Aggregating Sessions by Marketing Source

#### First investigating the negative Snapchat session counts

- snap_sessions = sessions[[
    - 'Snapchat X Bedding Page Sessions', 
    - 'Snapchat X Homepage Sessions', 
    - 'Snapchat X Mattress Page Sessions', 
    - 'Snapchat X Retail Locations Page Sessions']]
<p/>

-  snap_sessions.describe()
"""

#Created a new dataframe to look at description of only Snapchat Sessions
snap_sessions = sessions[['Snapchat X Bedding Page Sessions', 'Snapchat X Homepage Sessions', 'Snapchat X Mattress Page Sessions', 'Snapchat X Retail Locations Page Sessions']]
snap_sessions.describe()

#Created new variables to find the frequency of negative counts per webpage
snap_bedding_sessions = sessions[['Snapchat X Bedding Page Sessions']]
snap_homepage_sessions = sessions[['Snapchat X Homepage Sessions']]
snap_mattress_sessions = sessions[['Snapchat X Mattress Page Sessions']]
snap_retail_sessions = sessions[['Snapchat X Retail Locations Page Sessions']]

"""#### We notice from the investigation:
- 14 total instances of negative session counts 
- 10 instances occurred on the Mattress page!
"""

#One instance for Bedding
neg_snap_bedding_sessions = snap_bedding_sessions[snap_bedding_sessions['Snapchat X Bedding Page Sessions'] < 0]
print(neg_snap_bedding_sessions)

#One instance for Homepage
neg_snap_homepage_sessions = snap_homepage_sessions[snap_homepage_sessions['Snapchat X Homepage Sessions'] < 0]
print(neg_snap_homepage_sessions)

#Ten instances for Mattress!
neg_snap_mattress_sessions = snap_mattress_sessions[snap_mattress_sessions['Snapchat X Mattress Page Sessions'] < 0]
print(neg_snap_mattress_sessions)

#Two instances for Retail Locations
neg_snap_retail_sessions = snap_retail_sessions[snap_retail_sessions['Snapchat X Retail Locations Page Sessions'] < 0]
print(neg_snap_retail_sessions)

"""#### Assumption
Based on the numbers we found, we can make an assumption that the negative numbers could reasonably be explained as positive counts that encountered a glitch and were counted in reverse. Therefore we can use their absolute value to work with only positive numbers. <p/>
From here I would <b/> urgently recommend engaging the Dev & Engineering team </b> to look into this issue to have a more concrete solution for current data aggregation as well as look into a fix to prevent this going forward as well as double checking the numbers of the other sessions to ensure the accuracy and integrity of the data collection.

With the absolute values, we now have a new variable that houses a table of Snapchat sessions that are all positive integers.
- snap_sessions_abs = snap_sessions.abs()
- snap_sessions_abs.describe()
"""

#Placing the absolute value of the Snapchat Sessions into a new variable, maintaining the 
#original data, but working with this dataframe for now until we hear back from the developers and engineers
snap_sessions_abs = snap_sessions.abs()
snap_sessions_abs.describe()

"""#### Sessions

Using the following code to combine into new columns: <p/>
(repeated for each source)
- sessions['Organic Sessions'] = 
- sessions['Organic X Bedding Page Sessions'] + 
- sessions['Organic X Homepage Sessions'] + 
- sessions['Organic X Mattress Page Sessions'] + 
- sessions['Organic X Retail Locations Page Sessions']  <p/>

** For Snapchat, the absolute value 'snap_sessions_abs' table was substituted for the aggregation calculation.
"""

#Combine Bedding, Homepage, Mattresses, and Retails Locations pages into their respective Session Sources 
#Specifically using the absolute value Snapchat Sessions dataframe to add together the positive session values
sessions['Organic Sessions'] = sessions['Organic X Bedding Page Sessions'] + sessions['Organic X Homepage Sessions'] + sessions['Organic X Mattress Page Sessions'] + sessions['Organic X Retail Locations Page Sessions']
sessions['Direct Sessions'] = sessions['Direct X Bedding Page Sessions'] + sessions['Direct X Homepage Sessions'] + sessions['Direct X Mattress Page Sessions'] + sessions['Direct X Retail Locations Page Sessions']
sessions['Google Sessions'] = sessions['Google Search X Bedding Page Sessions'] + sessions['Google Search X Homepage Sessions'] + sessions['Google Search X Mattress Page Sessions'] + sessions['Google Search X Retail Locations Page Sessions']
sessions['YouTube Sessions'] = sessions['YouTube x Bedding Page Sessions'] + sessions['YouTube x Homepage Sessions'] + sessions['YouTube x Mattress Page Sessions'] + sessions['YouTube x Retail Locations Page Sessions']
sessions['Facebook Sessions'] = sessions['Facbeook x Bedding Page Sessions'] + sessions['Facbeook x Homepage Sessions'] + sessions['Facbeook x Mattress Page Sessions'] + sessions['Facbeook x Retail Locations Page Sessions']
sessions['Snapchat Sessions'] = snap_sessions_abs['Snapchat X Bedding Page Sessions'] + snap_sessions_abs['Snapchat X Homepage Sessions'] + snap_sessions_abs['Snapchat X Mattress Page Sessions'] + snap_sessions_abs['Snapchat X Retail Locations Page Sessions']

"""Quick view of the table shows a much more digestible version of the data, just like Orders:"""

#Quick view of the table shows a much more digestible version of the data, just like Orders
sessions[["Organic Sessions", "Direct Sessions", "Google Sessions", "YouTube Sessions", "Facebook Sessions", "Snapchat Sessions"]]

#Placed the table into a new variable to work with during visualization and further data manipulation
sessions_agg = sessions[["Organic Sessions", "Direct Sessions", "Google Sessions", "YouTube Sessions", "Facebook Sessions", "Snapchat Sessions"]]

"""### Investigating the Aggregated Orders & Sessions

#### Orders
Taking a look at the summary statistics .describe( ) of the Aggregated Orders we notice:
- Google has the highest max and mean orders with very low variability from the standard deviation
- On the other hand, Snapchat has the lowest max orders with very high variability in its standard deviation
- YouTube and Facebook are close in their statistics, but their mean isn't too far off from Snapchat
- Organic and Direct have similar min, max and mean but Direct has a much higher variability in its standard deviation
"""

orders_agg.describe()

"""#### Sessions
Taking a look at the summary statistics .describe( ) of the Aggregated Sessions we notice:
- Google again has the highest max and mean page sessions with relatively low variability from the standard deviation
- Snapchat again has the lowest stats overall with relatively high variability in its standard deviation
- YouTube and Facebook are close in all their statistics, even the standard deviation
- Organic and Direct have a much clearer distinction with Organic having much higher min, max, mean but both share a similar standard deviation 
"""

sessions_agg.describe()

"""## Visualization

#### Orders

For Orders we can see:
- Google is consistent in its orders, maintaining a high order amount over the 2 year time period.
- Organic and Direct started close buas Organic rose slightly over time, Direct had 2 major downward inflection points in September 2019 and May 2020
- The downward inflection points for Direct are consistent for Facebook, YouTube, and Snapchat
- In the first third of the time period, Snapchat and Facebook were close in counts. 
- In the middle of the time period had Snapchat falling closer with Youtube counts. 
In the final section, since May 2020, Snapchat orders fell consistently below both Facebook and Youtube.
"""

plt.plot("Organic Orders", data = orders_agg, color = "orange")
plt.plot("Direct Orders", data = orders_agg, color = "green")
plt.plot("Google Orders", data = orders_agg, color = "black")
plt.plot("YouTube Orders", data = orders_agg, color = "red")
plt.plot("Facebook Orders", data = orders_agg, color = "blue")
plt.plot("Snapchat Orders", data = orders_agg, color = "yellow")
plt.xlabel("Date")
plt.xticks(rotation = 45)
plt.ylabel("Orders Count")
plt.title("Orders Count per Marketing Source Jan 2019 - Dec 2020")
plt.legend(loc=(1.04,0.5))
plt.show()

"""#### Behind the code
Colors were intentionally picked to represent brands for easier recognition (Snapchat as yellow, Facebook as blue, etc).
- plt.plot("Organic Orders", data = orders_agg, color = "orange")
- plt.plot("Direct Orders", data = orders_agg, color = "green")
- plt.plot("Google Orders", data = orders_agg, color = "black")
- plt.plot("YouTube Orders", data = orders_agg, color = "red")
- plt.plot("Facebook Orders", data = orders_agg, color = "blue")
- plt.plot("Snapchat Orders", data = orders_agg, color = "yellow")
<p/>
 
Rotation was chosen to ease reading of the dates and the Legend location was adjusted so that it wouldn't overlap with the graph.
- plt.xlabel("Date")
- plt.xticks(rotation = 45)
- plt.ylabel("Orders Count")
- plt.title("Orders Count per Marketing Source Jan 2019 - Dec 2020")
- plt.legend(loc=(1.04,0.5))
- plt.show()

#### Sessions
For Sessions we can see: 
- Clear lines straight across each Marketing Source
- Google at the top, with Organic not far behind
- Direct in the middle of the pack
- Facebook and YouTube overlapping entirely
- Snapchat hovering consistently below the rest
"""

plt.plot("Organic Sessions", data = sessions_agg, color = "orange")
plt.plot("Direct Sessions", data = sessions_agg, color = "green")
plt.plot("Google Sessions", data = sessions_agg, color = "black")
plt.plot("YouTube Sessions", data = sessions_agg, color = "red")
plt.plot("Facebook Sessions", data = sessions_agg, color = "blue")
plt.plot("Snapchat Sessions", data = sessions_agg, color = "yellow")
plt.xlabel("Date")
plt.xticks(rotation = 45)
plt.ylabel("Website Visit Count")
plt.title("Website Visit Count per Marketing Source Jan 2019 - Dec 2020")
plt.legend(loc=(1.04,0.5))
plt.show()

"""### Grouping By Month"""

#Experimented with Quarterly values and it was too bare, no trends
quarterly_sessions = sessions_agg.resample('QS').sum()
quarterly_orders = orders_agg.resample('QS').sum()

#Tried again with Monthly values and Goldilocks!! ("Just Right!")
monthly_sessions = sessions_agg.resample('MS').sum()
monthly_orders = orders_agg.resample('MS').sum()

"""#### Monthly Orders

- monthly_orders = orders_agg.resample('MS').sum()
"""

monthly_orders

"""Plotting Monthly Order sums makes it much easier to see the trends changing over time:
- The dips in September 2019 and May 2020 for Direct, YouTube, Facebook, and Snapchat.
- Dips in Feb 2019 and Feb 2020 are pronounced for Organic, Direct and Google Sources.
"""

plt.plot("Organic Orders", data = monthly_orders, color = "orange")
plt.plot("Direct Orders", data = monthly_orders, color = "green")
plt.plot("Google Orders", data = monthly_orders, color = "black")
plt.plot("YouTube Orders", data = monthly_orders, color = "red")
plt.plot("Facebook Orders", data = monthly_orders, color = "blue")
plt.plot("Snapchat Orders", data = monthly_orders, color = "yellow")
plt.xlabel("Months")
plt.xticks(rotation = 45)
plt.ylabel("Orders Count")
plt.title("Monthly Orders Count per Marketing Source Jan 2019 - Dec 2020")
plt.legend(loc=(1.04,0.5))
plt.show()

"""#### Monthly Sessions

- monthly_sessions = sessions_agg.resample('MS').sum()
"""

monthly_sessions

"""Plotting Monthly Session sums introduced more interesting findings:
- While the daily graph looked consistently straight, we can see clear dips in session activity for February 2019 and February 2020 that were not discernable before. 
"""

plt.plot("Organic Sessions", data = monthly_sessions, color = "orange")
plt.plot("Direct Sessions", data = monthly_sessions, color = "green")
plt.plot("Google Sessions", data = monthly_sessions, color = "black")
plt.plot("YouTube Sessions", data = monthly_sessions, color = "red")
plt.plot("Facebook Sessions", data = monthly_sessions, color = "blue")
plt.plot("Snapchat Sessions", data = monthly_sessions, color = "yellow")
plt.xlabel("Months")
plt.xticks(rotation = 45)
plt.ylabel("Website Visit Count")
plt.title("Monthly Website Visit Count per Marketing Source Jan 2019 - Dec 2020")
ax = plt.gca()
ax.get_yaxis().get_major_formatter().set_scientific(False)
plt.legend(loc=(1.04,0.5))
plt.show()

"""#### What about Performance?
Now that we have seen the counts over time, my next question is:
<b/> What percentage of Sessions per Source resulted in an Order? </b>

### Calculating Conversion Rates

To do this we can divide the orders by the sessions for each Source and this results in the following table: <p/>
(repeated for each source)

- monthly_orders['Organic Conversion'] = 
- monthly_orders['Organic Orders'] / monthly_sessions['Organic Sessions']
"""

#Combine Bedding, Homepage, Mattresses, and Retails Locations pages again, this time dividing order count by session count
monthly_orders['Organic Conversion'] = monthly_orders['Organic Orders'] / monthly_sessions['Organic Sessions']
monthly_orders['Direct Conversion'] = monthly_orders['Direct Orders'] / monthly_sessions['Direct Sessions']
monthly_orders['Google Conversion'] = monthly_orders['Google Orders'] / monthly_sessions['Google Sessions']
monthly_orders['YouTube Conversion'] = monthly_orders['YouTube Orders'] / monthly_sessions['YouTube Sessions']
monthly_orders['Facebook Conversion'] = monthly_orders['Facebook Orders'] / monthly_sessions['Facebook Sessions']
monthly_orders['Snapchat Conversion'] = monthly_orders['Snapchat Orders'] / monthly_sessions['Snapchat Sessions']

#Placed the table into a new variable to work with during visualization
monthly_percent_performance = monthly_orders[['Organic Conversion', 'Direct Conversion', 'Google Conversion', 'YouTube Conversion', 'Facebook Conversion', 'Snapchat Conversion']]

monthly_percent_performance

"""#### Monthly Conversion Rate
Plotting the Monthly Conversion Rates we see more interesting findings: 
- From January 2019 to April 2020, even though Snapchat had the lowest counts, they were actually performing pretty well in terms of percentage conversion. 
- From April 2020 to December 2020 Snapchat is still converting to orders at a higher rate than YouTube, though it looks like YouTube may overtake Snapchat if the trend continues.
- YouTube, Facebook and Direct have been consistenly falling in their conversion rates with inflection points at September 2019 and May 2020.
- Each has been similarly affected by what seems like a larger event. With additional data and resources, causal inference algorithms could be used to help determine what the event was and predictive models could be used to calculate the future impact of such events.
- Both Google and Organic sources have maintained consistent conversion rates, with no seasonality and no impact from the events that impacted the other sources. 
"""

plt.plot("Organic Conversion", data = monthly_percent_performance, color = "orange")
plt.plot("Direct Conversion", data = monthly_percent_performance, color = "green")
plt.plot("Google Conversion", data = monthly_percent_performance, color = "black")
plt.plot("YouTube Conversion", data = monthly_percent_performance, color = "red")
plt.plot("Facebook Conversion", data = monthly_percent_performance, color = "blue")
plt.plot("Snapchat Conversion", data = monthly_percent_performance, color = "yellow")
plt.xlabel("Months")
plt.xticks(rotation = 45)
plt.ylabel("Conversion Percentage")
plt.title("Monthly Conversion Rate per Marketing Source Jan 2019 - Dec 2020")
plt.legend(loc=(1.04,0.5))
plt.show()

"""## Final Notes for Marketing Team
#### Immediate Next Steps:
- Webpage Negative Session Counts
    - Engage Dev + Engineering Team ASAP
- February Seasonality
    - Investigate Past & Anticipate Future
- September 2019 & May 2020 
    - Determine Inference & Impact
#### Which Sources to prioritize: 
### Google & Organic
- Most Orders
    - Google & Organic
- Most Sessions
    - Google & Organic
- Most Consistent
    - Google & Organic
- Higest Conversion
    - Google & Direct
#### Which Sources to de-prioritize:
### Snapchat & Youtube
- Least Orders
    - Snapchat & Youtube 
- Least Sessions
    - Snapchat
- Least Consistent
    - Snapchat
- Lowest Conversion
    - YouTube

### Future Analysis Potential
- Sources each compared by page for deeper drilldown
- Aggregation Calculations designed into functions for accuracy 
- Engaging Finance Team to incorporate financial ROI metrics 
- Colloborate with Product Managers to better understand customer insights
- Brainstorm with Dev & Engineering for better data structure & integrity
"""