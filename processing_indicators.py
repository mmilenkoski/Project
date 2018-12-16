import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
import seaborn as sns

def read_eveything(indicator_path, indicator=True):
    parties = pd.read_csv("data/country_party_dataset.csv", index_col=0)
    positions = pd.read_csv("data/positions_scale.csv")

    positions_sorted = ['far-left', 'left-wing to far-left', 'left-wing', 'centre-left to left-wing', 'centre-left', \
                        'centre to centre-left', 'centre', 'syncretic', 'big tent', 'centre to centre-right', \
                        'centre-right', 'centre-right to right-wing', 'right-wing', 'right-wing to far-right', \
                        'far-right']

    parties = pd.merge(parties, positions, left_on=["Political_position"], right_on=["Position"])

    parties["weighted_seats_last"] = (parties["Seats %_last"]/100)*parties["Scale"]
    parties["weighted_seats_previous"] = (parties["Seats %_previous"]/100)*parties["Scale"]

    parties["weighted_votes_last"] = (parties["Votes %_last"]/100)*parties["Scale"]
    parties["weighted_votes_previous"] = (parties["Votes %_previous"]/100)*parties["Scale"]

    parties = parties.groupby("Country").sum()

    parties["difference_seats"] = parties["weighted_seats_last"] - parties["weighted_seats_previous"]
    parties["difference_votes"] = parties["weighted_votes_last"] - parties["weighted_votes_previous"]

    parties = parties.reset_index()
    
    
    election_years = pd.read_csv('data/election_years.csv')
    # because the indicators don't contain data for 2018
    election_years["prev_el_year"] = election_years["prev_el_year"].apply(lambda x: x-1 if x == 2018 else x)
    election_years["last_el_year"] = election_years["last_el_year"].apply(lambda x: x-1 if x == 2018 else x)
    
    
    # load datasets
    #indicator = pd.read_csv("additional_data/refugees/refugee_population.csv", header=2, sep=',')
    #indicator = pd.read_csv("additional_data/social_freedom/income_share_held_by_highest_10.csv", header=2, sep=',')
    #indicator = pd.read_csv("additional_data/social_freedom/government_effectiveness.csv", sep=',')
    #indicator["2007"] = indicator["2008"]
    
    if indicator:
        indicator = pd.read_csv(indicator_path, header=2, sep=',')
    else:
        indicator = pd.read_csv(indicator_path, sep=',')
        # The indicators don't contain data for 2007, but we don't need it
        indicator["2007"] = indicator["2008"]

    indicator["Country Name"] = indicator["Country Name"].replace("Slovak Republic", "Slovakia")

    # countries and features of interest
    countries = ['Austria','Belgium','Bulgaria','Croatia','Cyprus','Czech Republic','Denmark',
                 'Estonia','Finland','France','Germany','Greece','Hungary','Ireland','Italy','Latvia','Lithuania',
                 'Luxembourg','Malta','Netherlands','Poland','Portugal','Romania','Slovakia','Slovenia','Spain',
                 'Sweden','United Kingdom','Norway','Iceland','Switzerland']
    columns = ['Country Name','Country Code','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017']

    # extract only countries of interest
    indicator = indicator.loc[indicator['Country Name'].isin(countries)]

    # reset index
    indicator.reset_index(inplace=True)

    # extract only features of interest
    indicator = indicator[columns]

    indicator = indicator.drop(['Country Code'], axis=1)

    indicator = pd.melt(indicator, id_vars=['Country Name'])

    indicator["variable"] = indicator["variable"].astype(int)
    indicator["value"] = indicator["value"].astype(float)
    
    
    elections_indicator = pd.merge(election_years, indicator, left_on=['Country', 'prev_el_year'], right_on=['Country Name', 'variable'])
    elections_indicator = elections_indicator.rename(columns={"value": "value_previous"})
    elections_indicator = pd.merge(elections_indicator, indicator, left_on=['Country', 'last_el_year'], right_on=['Country Name', 'variable'])
    elections_indicator = elections_indicator.rename(columns={"value": "value_last"})
    elections_indicator = elections_indicator.drop(["variable_x", "variable_y", "Country Name_x", "Country Name_y"], axis=1)
    elections_indicator["difference_value"] = elections_indicator['value_last'] - elections_indicator['value_previous']
    
    
    return elections_indicator, parties

def plot_everything(elections_indicator, parties, column_x, column_y, hide_germany=False, only_right=False, params={}):
    plt.style.use('seaborn-poster')
    merged = pd.merge(elections_indicator, parties)
    if hide_germany:
        merged = merged[merged['Country'] != 'Germany']
    #merged = merged[merged['Country'] != 'France']
    if only_right:
        merged = merged[merged[column_x] > 0]
    # plt.scatter(x=merged[column_x], y=merged[column_y])
    # if "x_label" in params.keys():
    #    plt.xlabel(params["x_label"])
    # if "y_label" in params.keys():
    #    plt.ylabel(params["y_label"])
    # if "title" in params.keys():
    #    plt.title(params["title"])
    # if "save_1" in params.keys():
    #     plt.savefig(params["save_1"], bbox_inches="tight", dpi=200)
    # plt.show()
    
    plt.subplots(figsize=(10,6)) 
    sns.regplot(x=column_x, y=column_y, data=merged)
    if "x_label" in params.keys():
        plt.xlabel(params["x_label"])
    if "y_label" in params.keys():
        plt.ylabel(params["y_label"])
    if "title" in params.keys():
        plt.title(params["title"])
    if "save_2" in params.keys():
        plt.savefig(params["save_2"], bbox_inches="tight", dpi=200)
    plt.show()
    
    merged = merged[[column_x, column_y]]
    print(merged.corr('spearman'))
    print("\nData for %s countires" % merged.dropna().shape[0])
