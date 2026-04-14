1. Once the data is extracted and stored into data lake of databricks, the following are the best practice steps:
    1. First analyze the file (eg csv file) about how data looks, what si the format, is there a header, what does data types look like? are there nulls etc
    2. Create a DDL to store data(eg in a table) accordingly with whatever data types you want in destination table.
    3. Then use spark dataframe reader api, whihc reads the file from data like as a data frame.
    4. Then perform various transformation before loading the file to table like data type casting, dups removal, column renaming etc
    5. use spark dataframe write api to save the dataframe as table.
