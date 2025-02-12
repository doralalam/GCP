#import bigquery python library from google.cloud
from google.cloud import bigquery
#create a variable to hold the path of the credentials file downloaded after creating the service account
SERVICE_ACCOUNT_JSON = r"<provide_path_for_json_credentials_file_here>"
#create a bigquery client object to retrieve the credentials from the file
#from_service_account_json method is used to rerieve the client credentials while creating the client object
#client object acts as an interface to manage using the bigquery api
client = bigquery.Client.from_service_account_json(SERVICE_ACCOUNT_JSON)
'''define the dataset name variable
in this format <bigquery_project_name.dataset_name>'''
dataset_id = "bigquery-practice-449511.dataset_from_py"
#construct a full dataset object to send to the api
dataset=bigquery.Dataset(dataset_from_py)
#to set dataset location attribute
dataset.location = "US"
#to set dataset description attribute
dataset.description = "dataset from python"
# in the same way, we can set different attributes whatever required
# to create a dataset with an api request using explicit time out
dataset_ref=client.create_dataset(dataset, timeout = 30)
#to check the status whether the dataset got created successfully or not
print("Created dataset {}.{}".format(client.project, dataset_ref.dataset_id))



'''To run this code, go to the terminal and run the following command
py create_dataset.py
if the dataset has been created successfully,
we will get a message on the terminal as Created dataset with project_name.dataset_id'''

