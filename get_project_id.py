import os
from google.oauth2 import service_account
from googleapiclient.discovery import build

def get_project_id():
    # Path to service account key JSON file.
    service_account_key_path = '../service-account-key.json'
    
    # Set the environment variable for authentication.
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = service_account_key_path

    # Authenticate using the service account credentials.
    credentials = service_account.Credentials.from_service_account_file(
        service_account_key_path,
        scopes=['https://www.googleapis.com/auth/cloud-platform']
    )

    # Create a Cloud Resource Manager client.
    crm_service = build('cloudresourcemanager', 'v1', credentials=credentials)

    # Fetch the project information.
    project_info = crm_service.projects().get(projectId=credentials.project_id).execute()

    # Print the Project ID.
    print(f"Project ID: {project_info['projectId']}")

if __name__ == '__main__':
    get_project_id()
