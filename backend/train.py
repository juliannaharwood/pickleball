import pandas as pd

def load_data():
    # Load data from CSV file into a DataFrame
    pickle_raw = pd.read_csv('backend/data/Pickleball - Sheet1.csv', header = None)
    return(pickle_raw)

def clean_data(pickle_raw):
    # clean header
    header = pickle_raw.iloc[1]
    pickle_clean = pickle_raw.iloc[2:]
    pickle_clean.columns = header

    # Define datetime columns
    pickle_clean['Court Time'] = pd.to_datetime(pickle_clean['Court Time'])
    pickle_clean['Game End Times'] = pd.to_datetime(pickle_clean['Game End Times'])
    return(pickle_clean)

def feature_engineer(pickle_clean):
    # Create game length variable
    pickle_clean['Game Length'] = pickle_clean.groupby(['Date'])['Game End Times'].diff().fillna(pickle_clean['Game End Times'] - pickle_clean['Court Time'])
    return(pickle_clean)

def get_data(pickle_clean, ind):
    return(pickle_clean.iloc[ind])


