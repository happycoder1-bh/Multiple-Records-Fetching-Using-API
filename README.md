
# Multiple Records Fetching script using API


This script is used to fetch multiple records all at once irrespective of limits of API calls , once script is executed all the records is fetched and saved in a CSV File .





## Running the Script

To run this script run

```bash
  pip install -r requirments.txt
```
Once requirements are installed then 

Here you need to add api url and username and password for BasicAuth

```bash
api_url = "paste-api-url-here"
username = "user_name"
password = "pass-word"
```
Once you configured this : Specify Path to file here:

```bash
output_file = "path_to_the_file"

```
You can specify limit over here , limit depends on how many records one API Call can fetch .
```bash
  limit = 10000
```
You can also specify additional parameters here :
```bash
additional_params = {"sysparm_exclude_reference_link": "true", "sysparm_query": "put-additional -query"}

```

Once Everything has been setup then you can run the below command :

```bash
  python run main.py
```



