import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split

###################### Prep Iris Data ######################

def iris_split(df):
    '''
    This function takes in the iris data acquired by get_iris_data,
    performs a split and stratifies species column.
    Returns train, validate, and test dfs.
    '''
    train_validate, test = train_test_split(df, test_size=.2, 
                                        random_state=123, 
                                        stratify=df.species)
    train, validate = train_test_split(train_validate, test_size=.3, 
                                   random_state=123, 
                                   stratify=train_validate.species)
    return train, validate, test



def prep_iris(df):
    '''
    This function takes in the iris df acquired by get_iris_data,
    Drops the species_id column and renames species_name to species, 
    Performs a 3-way split stratified on species, and
    Returns train, validate, and test dataframes.
    '''
    # drop and rename columns
    df = df.drop(columns='species_id').rename(columns={'species_name': 'species'})
    
    # split dataframe into train, validate, and test
    train, validate, test = iris_split(df)
    
    return train, validate, test