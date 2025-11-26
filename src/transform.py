import pandas as pd
import numpy as np

def transform(dataframe):
    dataframe['Proj_Name']=dataframe['Proj_Name'].astype(str).str.strip()
    dataframe['Owner_Name']=dataframe['Owner_Name'].astype(str).str.strip()
    dataframe['Priority_Level']=dataframe['Priority_Level'].astype(str).str.strip().str.title()
    dataframe['Budget']=pd.to_numeric(dataframe['Budget'],errors='coerce')
    dataframe['Status']=dataframe['Status'].astype(str).str.strip().str.title()
    dataframe['Start']=dataframe['Start'].astype(str)
    dataframe['End']=dataframe['End'].astype(str)
    dataframe['Start']=pd.to_datetime(dataframe['Start'],format='mixed',errors='coerce')
    dataframe['End']=pd.to_datetime(dataframe['End'],format='mixed',errors='coerce')
    dataframe['Budget'] = dataframe['Budget'].fillna(0)
    # dataframe['Start']=dataframe['Start'].fillna('Null')
    # dataframe['End']=dataframe['End'].fillna('Null')
    dataframe=dataframe.replace({pd.NaT: None, np.nan: None})
    return dataframe