from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

class AzureBlobStorage:
    def __init__(self, connection_string):
        self.blob_service_client = BlobServiceClient.from_connection_string(connection_string)

    def create_container(self, container_name):
        container_client = self.blob_service_client.get_container_client(container_name)
        container_client.create_container()

    def delete_container(self, container_name):
        container_client = self.blob_service_client.get_container_client(container_name)
        container_client.delete_container()

    def upload_blob(self, container_name, blob_name, data):
        container_client = self.blob_service_client.get_container_client(container_name)
        blob_client = container_client.get_blob_client(blob_name)
        blob_client.upload_blob(data, overwrite=True)

    def download_blob(self, container_name, blob_name):
        container_client = self.blob_service_client.get_container_client(container_name)
        blob_client = container_client.get_blob_client(blob_name)
        blob_data = blob_client.download_blob()
        return blob_data.content_as_bytes()

    def delete_blob(self, container_name, blob_name):
        container_client = self.blob_service_client.get_container_client(container_name)
        blob_client = container_client.get_blob_client(blob_name)
        blob_client.delete_blob()
