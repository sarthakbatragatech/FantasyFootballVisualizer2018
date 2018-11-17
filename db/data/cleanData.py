import pandas as pd
import numpy as np

def clean(position):

    print("Beginning Cleaning...\n")

    df = pd.read_csv(position+'pointsAgainst.csv')

    print("Reading file...\n")

    # On the URL from which data is collected, NFL lists all teams alphabetically except Arizona Cardinals
    # If abbreviation column already exists, do nothing....
    if 'Abbr' in df:
        return(print("Already Cleaned"))
    
    abbreviations = ['ATL','BAL','BUF','CAR','CHI','CIN','CLE','DAL',
    'DEN','DET','GB','TEN','HOU','IND','JAX','KC',
    'LA','OAK','MIA','MIN','NE','NO','NYG','NYJ',
    'PHI','ARI','PIT','LAC','SF','SEA','TB','WAS']

    df['Abbr'] = pd.DataFrame(abbreviations)

    # Sort the data by rank
    df = df.sort_values(by='Rank')
    print("Adding abbreviations and sorting data...\n")

    # Clean text
    # For defenses, the extra text appended after scraping is handled differently
    if position=='DEF':
        cleanTeams = pd.Series(df['Team']).str.replace("vs " + position, "")
    else:
        cleanTeams = pd.Series(df['Team']).str.replace(" Defensevs " + position, "")

    df['Team'] = cleanTeams

    # Drop column experiment
    df.drop(df.columns[0],axis=1)

    df.to_csv(position+'pointsAgainst.csv', index=False)
    print("Clean and re-write for " + position + " position complete...\n")

    print(df.head())

    # If an entire column is empty, remove it, or better yet, collect each position, 
    # see which columns are empty and based on value passed to function, remove those columns from csv
