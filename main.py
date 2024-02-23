import requests
import os
import pandas as pd


api_url = "paste-api-url-here"
username = "user_name"
password = "pass-word"

output_file = "path_to_the_file"
file_exists = os.path.exists(output_file)

def getOffset(path):
    if not file_exists:
        return None, 0
    
    df = pd.read_csv(path)
    return df, df.shape[0]

#  offset and limit
df, offset = getOffset(output_file)
limit = 5000 # Here Limit depends on capacity of API how mamny records it can fetch in one call

# additional parameters Here one can provide different parameters : Depends on what one wanna fetch can also add more parameters
additional_params = {"sysparm_exclude_reference_link": "true", "sysparm_query": "put-additional -query"}

# list to store all records
all_records = []

def save_file(df, data):
    
    new_df = pd.json_normalize(data)
    
    if df is None:
        df = new_df
    else:        
        df = pd.concat([df, new_df], ignore_index=True)
    
    df.to_csv(output_file, index=False)
    
    return df
    
while True:
    params = {
        "sysparm_limit": limit,
        "sysparm_offset": offset,
        **additional_params,
    }

    response = requests.get(api_url, auth=(username, password), params=params)

    if response.status_code == 200:
        new_records = response.json().get("result", [])
        all_records.extend(new_records)
        records_fetched = len(response.json().get("result", []))
        
        # Check if there are more records to fetch
        if records_fetched == 0:
            print(f"Fetched {records_fetched} records.")
            print("All records fetched!")
            break
        else:
            
            print(f"Fetched from {offset} to {records_fetched+offset} records.")
            offset += records_fetched
            df = save_file(df, new_records)
            

    else:
        print(f"Error in API request: {response.status_code}")
        break


