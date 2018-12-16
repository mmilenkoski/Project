# The Rise of the Right

Link to the data story: <a src="https://mmilenkoski.github.io/">link</a>.

# Abstract

The last couple of years have been defined by the dramatically increasing political polarization of Europe. The main idea of this project is to investigate the main causes and effects of this massive shift in the political landscape.

By observing the countries which were most affected by the populist movement, we want to identify the main factors that contribute to this trend. Our plan is to analyze the effect of terrorist attacks, immigration waves and similar events on the likelihood of a country’s population to vote for right-leaning parties.

The final idea is to investigate whether the claim of the populists that nationalism would increase the safety and prosperity of the country is justified by comparing the social and economic stability of countries under liberal and conservative governments. For this purpose, we will primarily use the GDELT dataset, enriched with datasets for country-specific statistics. 

# Research questions
1. What are the main factors that contribute to the increase in support of populist parties?
2. What is the impact of the recent terrorist attacks and immigration waves on the political landscape?
3. How does the quality of life in a country correlate to the ideology of its ruling party?

# Dataset
For this project, we plan to use the GDELT dataset enriched with datasets for country-specific statistics. The GDELT dataset provides us information about events between actors. We have filtered the GDELT dataset to obtain only the events in which either one of the actors is from a country from EU/EEA or the event itself took place in a country from EU/EEA. We limit our analysis to the European countries for easier and more meaningful analysis. Countries from EU/EEA are all democratic and members of the same association, so comparing them will yield more meaningful analysis than comparing all countries in the world. Furthermore, we are much more informed about the political situation in Europe than in the rest of the world, so we will be able to better interpret the obtained results. The script used for filtering the dataset and a guide for using it can be found in the folder **gdelt_spark_dataset**. The filtered dataset is not uploaded to GitHub due to size constraints. It can be downloaded from the following <a href="https://drive.google.com/drive/u/1/folders/1jKztRsM5SRfR0480caBRsNhl43vYA-6y?fbclid=IwAR08ho5IG64I_rpKQd9LMmEdDIJudT5gYy3TJ1cmwZc5pBlAbZuga5DMa8g">link</a>. The file should be put in folder named **data**.

In addition to the GDELT dataset we have create our own dataset for the election results in the previous two elections for all countries of interest. Details about the creation process and the format of the dataset can be found in the notebook **milestone_3**. The raw data, intermediate results and the final dataset can be found in the folder **wikipedia_datasets**. In the same folder, there are the notebooks used for cleaning the raw data and creating the final dataset. We want to point out that some small incosistencies and mistakes were fixed manually after the creation of the dataset. The final dataset can be found in the file **wikipedia_datasets/country_party_dataset.csv**.

Additionally, we used data from the dataset **World Development Indicators** (https://data.worldbank.org/indicator/). These datasets can be found in the folder **additional_data**. We have used these indicators in order to explain the causes and consequences of the shift in political power. 

Furthermore, we have obtained a Geo JSON map of Europe from here: https://github.com/leakyMirror/map-of-europe. We used this map for creating visualizations of our findings. The map can be found in the folder **additional_data/europe_map**.

## Project Structure
The project is organized as follows:

    .
    ├── aditional_data           # World Bank datasets and map of Europe
    ├── gdelt_spark_dataset      # Script and guide for filtering GDELT dataset
    ├── images_and_maps          # All visualizations used in the final story
    ├── wikipedia_datasets       # Raw, intermediate and final wikipedia dataset, plus notebooks for creation process
    ├── README.md                # README file
    ├── milestone_3.ipynb        # Main notebook for milestone 2
    └── preprocessing_indicators # helper script for plotting scatter plots of the indicators

# A list of internal milestones up until project milestone 3

# Contributions

<b> Martin Milenkoski </b> - Topic idea, writing final data story, analysis and visualisations of Wikipedia dataset

<b> Blagoj Mitrevski </b> - Analysis and visualizations of World Indicators dataset, crawling and preprocessing of datasets

<b> Davor Todorovski </b> - Filtering, analysis and visualizations of the GDELT dataset
