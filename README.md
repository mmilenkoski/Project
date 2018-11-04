# The Rise of the Right

# Abstract

The last couple of years have been defined by the dramatically increasing political polarization of the world. The main idea of this project is to investigate the main causes and effects of this massive shift in the political landscape.

By observing the countries which were most affected by the populist movement, we want to identify the main factors that contribute to this trend. Our plan is to analyze the effect of terrorist attacks, immigration waves and similar events on the likelihood of a country’s population to vote for right-leaning parties.

The final idea is to investigate whether the claim of the populists that nationalism would increase the safety and prosperity of the country is justified by comparing the social and economic stability of countries under liberal and conservative governments. For this purpose, we will primarily use the GDELT dataset, enriched with datasets for country-specific statistics. 

# Research questions
1. What are the main factors that contribute to the increase in support of populist parties?
2. What is the impact of the recent terrorist attacks and immigration waves on the political landscape?
3. How does the quality of life in a country correlate to the ideology of its ruling party?

# Dataset
For this project, we plan to use the GDELT dataset enriched with datasets for country-specific statistics. The GDELT dataset provides us information about events between actors. The events are enriched with metadata about the two actors, and the event itself. Using the country codes of actors, and the average tone of the event, we can investigate whether countries governed by conservative parties are more aggressive towards other countries. Additionally, we can observe what is the average tone of events between different ethnicities and religions in countries governed by liberal and conservative parties. We can also investigate the popularity of a government by using the type of actors, the type and class of events, and the Goldstein Scale attribute which estimates the impact of the event on the stability of a country.  In addition, we are interested in the effects of terrorist attacks and similar events on the average tone and Goldstein Scale, popularity of the government, hate speech and similar aspects of news related to the country of interest. 

We plan to enrich this information with other datasets including, but not limited to:

1. **Political Stability And Absence Of Violence/Terrorism**: Estimates likelihood of political instability and politically-motivated violence for each country.  
https://datacatalog.worldbank.org/political-stability-and-absence-violenceterrorism-estimate
  
2. **Worldwide Governance Indicators**: Provides governance indicators in respect to Voice and Accountability, Political Stability and Absence of Violence, Government Effectiveness, Regulatory Quality,Rule of Law and Control of Corruption.  
https://datacatalog.worldbank.org/dataset/worldwide-governance-indicators 

3. **World Development Indicators**: Includes more than 800 estimators covering more than 150 different economies. Provides national, regional, and global estimates.  
https://datacatalog.worldbank.org/dataset/world-development-indicators  

In general, the site https://data.worldbank.org/ provides many datasets for country-specific year-by-year statistics, and we will decide which ones to use depending on the factors by which we want to compare different countries. 

# A list of internal milestones up until project milestone 2
### Milestone 2.1
  • Explore the GDELT dataset in detail, identify the relevant information and perform data wrangling and preprocessing.
  
  • Explore additional literature (papers, articles, similar projects) that might give us interesting insights and additional ideas on creating the data story.
  
  • Explore datasets containing statistics for the safety, economic growth and quality of life in each country.
  
  • Obtain an initial understanding on how to utilize the cluster for the processing of the GDELT dataset.
### Milestone 2.2
  • Combine the GDELT datasets with the extracted relevant statistics from the other datasets in order to draw some preliminary conclusions concerning the research questions.
  
  • Explore different methods for the data visualization.
### Milestone 2.3
  • Add the necessary documentation to the notebook, as well as explanation of the used methods so that it is understandable for examination.
  
  • Provide illustrative visualizations and understandable results.

# Questions for TAa
1. Do you know any other datasets which might be useful for our project?
2. Do you know any previous work on this or similar topic, such as papers or articles, which we might use for inspiration and additional ideas?
