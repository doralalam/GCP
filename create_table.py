from google.cloud import bigquery
SERVICE_ACCOUNT_JSON = r'<provide path for json credentials file here'
#create a bigquery client object to retrieve the credentials from the file
#from_service_account_json method is used to rerieve the client credentials while creating the client object
#client object acts as an interface to manage using the bigquery api
client = bigquery.Client.from_service_account_json(SERVICE_ACCOUNT_JSON)
table_name = "bigquery-practice-449511.dataset_from_py.table_from_py"
# project_name.dataste_name.table_name
job_config = bigquery.LoadJobConfig(
    # schema representation
    schema=[
        bigquery.SchemaField("name", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("gender", "STRIING", mode="NULLABLE"),
        bigquery.SchemaField("count", "INTEGER", mode="NULLABLE")
    ],
    # source file is in CSV format and consists of header rows (or) first row with names
    source_format=bigquery.SourceFormat.CSV, skip_leading_rows = 1
    # if the source is JSON, then SourceFormat.NEWLINEDELIMITEDJSON
)
file_path =r'<source file path here'
# to open the source file in read binary mode
source_file = open(file_path, "rb")
# to load source file, create a job
job = client.load_table_from_file(source_file, table_name, job_config = job_config)
# to wait until the job gets finished
job.result()
# table will be created by now and to check
# follow the next statements
table = client.get_table(table_name)
# to display a message
print("Loaded {} rows from {}".format(table.num_rows, table_name))