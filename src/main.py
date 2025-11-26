# from extract import *
from config_loader import *
from extract_sql_server import *
from transform import *
from load import load_data

def main():
    # connect to sharepoint and load data, then transform to dataframe
    establish_conn()
    # print the extracted dataframe
    raw_data=extract_data('select * from sharepoint_project_metadata')
    print(raw_data)

    # perform transformations
    transformed_df=transform(raw_data)

    # print transformed dataframe
    print(transformed_df.info())

    # Load the transformed dataframe into destination
    load_data(transformed_df,'clean_sharepoint_project_metadata')
    # close conn
    close_conn()

    pass

if __name__=="__main__":
    main()
