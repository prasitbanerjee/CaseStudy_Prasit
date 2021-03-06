import pandas as pd
import json

# Declaring DataFrame

df = pd.DataFrame

# Reading the CSV file from the Device and loading it to a DataFrame
# The file path for the csv file should be provided by the user (input_file_path)

def read_csv():
    global df
    input_file_path = './input_data.csv'
    df = pd.read_csv(input_file_path, dtype=str)
    return (input_file_path)
read_csv()

# Deleting Blank Rows & Resetting Index

df = df.dropna(how='all')
df = df.reset_index(drop=True)

# Splitting the DataFrame into 2 Parts (df1 & df2)

df1 = df.iloc[:, [0, 1, 2, 3]]
df2 = df.iloc[:, 4:]

# Removing Cells with Null values

df2 = df2.dropna()

# Deleting duplicate records of DataFrame1
df1.drop_duplicates()

childList = []

# Grouping the contents of 1st DataFrame (df1) based on 'Base URL'
group1 = df1.groupby(['Base URL'])

parentDict = {}

# Assigning values to Base parent dictionary

def load_parentDict():
    for key, value in group1:
        k = group1.get_group(key).reset_index(drop=True)
        parentDict['Base URL'] = k.at[0, 'Base URL']
        parentDict['Level 1 - Name'] = k.at[0, 'Level 1 - Name']
        parentDict['Level 1 - ID'] = k.at[0, 'Level 1 - ID']
        parentDict['Level 1 - URL'] = k.at[0, 'Level 1 - URL']
        return parentDict['Level 1 - Name'], parentDict['Level 1 - ID']

load_parentDict()


# Grouping the contents of 2nd DataFrame (df2) based on 'Base URL'
group2 = df2.groupby(['Level 2 - ID'])

# Assigning values to a dictionary for creating subset

def load_childDict():
    for key, value in group2:
        dictionary = {}
        j = group2.get_group(key).reset_index(drop=True)
        dictionary['Level 2 - Name'] = j.at[0, 'Level 2 - Name']
        dictionary['Level 2 - ID'] = j.at[0, 'Level 2 - ID']
        dictionary['Level 2 URL'] = j.at[0, 'Level 2 URL']

        dictList = []
        subDict = {}

        # Creating nested dictionary
        for i in j.index:
            subDict['Level 3 - Name'] = j.at[i, 'Level 3 - Name']
            subDict['Level 3 - ID'] = j.at[i, 'Level 3 - ID']
            subDict['Level 3 URL'] = j.at[i, 'Level 3 URL']

            dictList.append(subDict)

            subDict = {}

        # Making subset to create parent child structure
        dictionary['subset'] = dictList

        childList.append(dictionary)
    return dictionary['Level 2 - Name'], dictionary['Level 2 - ID']

load_childDict()


# Making subset to add the child part with the parent dictionary
parentDict['subset'] = childList


# Creating a json file & writing data on it
# Provide the desired path to store the file along with the desired filename

def load_json():
    out_file_path = './output_sample.json'
    out_file = open(out_file_path, "w")
    json.dump(parentDict, out_file, indent=6)
    out_file.close()
    return out_file_path
load_json()

'''
# Printing the generated json file. Optional can be printed if required

temp_file = open("output_sample.json", "r")
temp_json = json.load(temp_file)
pretty_json = json.dumps(temp_json, indent=6)
temp_file.close()

print(pretty_json)
'''
