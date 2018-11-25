# The Rise of the Right

# Abstract

The last couple of years have been defined by the dramatically increasing political polarization of Europe. The main idea of this project is to investigate the main causes and effects of this massive shift in the political landscape.

By observing the countries which were most affected by the populist movement, we want to identify the main factors that contribute to this trend. Our plan is to analyze the effect of terrorist attacks, immigration waves and similar events on the likelihood of a country’s population to vote for right-leaning parties.

The final idea is to investigate whether the claim of the populists that nationalism would increase the safety and prosperity of the country is justified by comparing the social and economic stability of countries under liberal and conservative governments. For this purpose, we will primarily use the GDELT dataset, enriched with datasets for country-specific statistics. 

# Research questions
1. What are the main factors that contribute to the increase in support of populist parties?
2. What is the impact of the recent terrorist attacks and immigration waves on the political landscape?
3. How does the quality of life in a country correlate to the ideology of its ruling party?

# Dataset
For this project, we plan to use the GDELT dataset enriched with datasets for country-specific statistics. The GDELT dataset provides us information about events between actors. Details about the format and basic statistics about the dataset can be found in the notebook **milestone_2**. We have filtered the GDELT dataset to obtain only the events in which either one of the actors is from a country from EU/EEA or the event itself took place in a country from EU/EEA. We limit our analysis to the European countries for easier and more meaningful analysis. Countries from EU/EEA are all democratic and members of the same association, so comparing them will yield more meaningful analysis than comparing all countries in the world. Furthermore, we are much more informed about the political situation in Europe than in the rest of the world, so we will be able to better interpret the obtained results. The script used for filtering the dataset and a guide for using it can be found in the folder **gdelt_spark_dataset**.

In addition to the GDELT dataset we have create our own dataset for the election results in the previous two elections for all countries of interest. Details about the creation process and the format of the dataset can be found in the notebook **milestone_2**. The raw data, intermediate results and the final dataset can be found in the folder **wikipedia_datasets**. In the same folder, there are the notebooks used for cleaning the raw data and creating the final dataset. We want to point out that some small incosistencies and mistakes were fixed manually after the creation of the dataset. The final dataset can be found in the file **wikipedia_datasets/country_party_dataset.csv**.

Additionally, we plan to use some data from World Bank. In the current milestone we have presented the following two datasets:

1. **Political Stability And Absence Of Violence/Terrorism**: Estimates likelihood of political instability and politically-motivated violence for each country.  
https://datacatalog.worldbank.org/political-stability-and-absence-violenceterrorism-estimate

2. **Refugee population by country or territory of asylum**: Includes the number of refugees which were grandet Asylum in each country. 
https://data.worldbank.org/indicator/SM.POP.REFG?fbclid=IwAR3zh3W9eXYD8s09Th_CwKK4Uh-TtmTBOEpPOuJh-RYh3tfVyMEWbXfe_Zo 

These datasets can be found in the folders **additional_data/political_stability** and **additional_data/refugees**. However, the World Bank data is provided in the same format, and we have presented in this Milestone the pipeline for extracting only the countries and period of interest for us from the provided format. In this way, we can make use of additional data from World Bank in our analysis for the final project. Specifically, we plan to use some of the over 800 indicators provided in the dataset **World Development Indicators** (https://data.worldbank.org/indicator/). Some indicators of interest are Unemployment Rate, GDP per capita, Percent of Urban Population etc.

We noticed at the end of our analysis that we might need the years of the previous two elections in each country, but we did not have time to create the dataset for this milestone. We plan to create such dataset for the next milestone using Wikipedia. 

## Project Structure
The project is organized as follows:

    .
    ├── aditional_data           # World Bank datasets and map of Europe
    ├── gdelt_spark_dataset      # Script and guide for filtering GDELT dataset
    ├── report                   # Latex files provided by TAs
    ├── wikipedia_datasets       # Raw, intermediate and final wikipedia dataset, plus notebooks for creation process
    ├── README.md                # README file
    ├── EU_map_[123].html        # Folium maps in HTML
    └── milestone_2.ipynb        # Main notebook for mileston 2

# A list of internal milestones up until project milestone 3

### Milestone 3.1 - Create dataset with years of elections

### Mileston 3.2 - Analyze Wikipedia dataset

- Identify the countries with biggest shift in political power / popularity between the last two elections. 
- Identify which countries have moved to the left and which countries have moved to the right.

### Mileston 3.3 - Compare GDELT and Wikipedia datasets

- Explore the relationship between the election results and the average tone of GDELT events. 
- Explore the relationship between the election results and the Goldstein Scale of GDELT events.
- Explore the relationship between the election results and the frequency of some types of GDELT events.
- Can some characteristics of the GDELT events related to a country predict a major shift in political power?
- Does a shift in political power cause change in the average tone, Goldstein Scale and frequency of some types of GDELT events. 
- Explore each of the above mentioned relationships in respect to internal events between actors from same country, and external events toward neighbouring or other countries in general.
- Explore what are the major differences in the characteristics of GDELT events related to countries with nationalist and liberal governments, and between countries which have moved to the right
and to the left recently.

### Milestone 3.4 - Compare World Bank and Wikipedia datasets

- Explore the relationships between indicators from the World Bank data and the election results. We plan to repeat the same analysis listed for the characteristics of the GDELT events with the
indicators from the World Bank. Does change in some indicators cause political shift, and does political shift cause a change in some indicators. Some of the indicators we plan to use are number of refugees, political stability, education, urban population, economic growth etc.

### Milestone 3.5 - Compare World Bank and GDELT dataset

- Explore the relationship between characteristics of GDELT events and some World Bank indicators
- For example, does a decrease in stability / rise in number of refugees lead to decrease in AvgTone / Goldstein Scale of events. 

### Milestone 3.6 - Create visuzalizations

- Visualize the shift in political power of each country on the map of Europe. 
- Visualize the ruling political position of each country. 
- Visualization with pins which upon clicked show some interesting information about the country in regards to the GDELT events, election results or development indicators. 
- Map with dropdown menu in which a user can select a country and observe the interaction of a country with the other EEA countries through the average tone, Goldstein Scale and frequency of certain types of events between the country and all others.

### Milestone 3.7 - Create data story

- Combine the most interesting findings and visualizations in a final data story. 
