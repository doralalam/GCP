
# This is the basic skeleton to run any kind of query using python
# just edit query field as per the requirement and run the command "py create_query.py" in the terminal



from google.cloud import bigquery
SERVICE_ACCOUNT_JSON = r'<path for json service account credentials file'
client = bigquery.Client.from_service_account_json(SERVICE_ACCOUNT_JSON)

# We can edit any query here as per our needs and can run
query_to_run = "select * from bigquery-practice-449511.dataset_from_py.table_from_py"
# run the job or query
query_job = client.query(query_to_run)

# to see the result job 
print(query_job)
# to display the rows in table
for row in query_job:
    print(str(row[0])+","+str(row[1])+","+str(row[2]))
