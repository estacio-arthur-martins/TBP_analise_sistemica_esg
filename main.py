from pkg.blob_storage import AzureBlobStorage
from pkg.postgresql import AzurePostgreSQL

import os

try:
    datalake = AzureBlobStorage(os.environ.get('CONNECTION_AZURE_BLOB_STORAGE_DATA_LAKE', 'default_value'))
    database = AzurePostgreSQL(os.environ.get('CONNECTION_AZURE_POSTGRESQL_DATABASE', 'default_value'))
except:
    print("except")
finally:
    print("finally")
