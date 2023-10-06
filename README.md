# GCP Project ID Retrieval Script

This Python script demonstrates how to retrieve and print the Project ID of a Google Cloud Platform (GCP) project using the GCP API. Follow the steps below to set up and run the script.

## Prerequisites

Before running the script, make sure you have the following prerequisites in place:

1. A Google Cloud Platform (GCP) account.
2. A GCP project created and configured.

## Step 1: Set Up a Google Cloud Project and Enable APIs

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).

2. Create a new GCP project or select an existing one.

3. Enable the following APIs for your project:

   - Cloud Resource Manager API
   - Identity and Access Management (IAM) API

## Step 2: Create a Service Account

1. In the Google Cloud Console, navigate to "IAM & Admin" > "Service accounts."

2. Create a new service account or use an existing one.

3. Assign the "Project Editor" role to the service account.

4. Download the service account key JSON file.

## Step 3: Install Required Python Libraries

You need to install the necessary Python libraries using `pip`. Open a terminal and run the following command:

```bash
pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

## Step 4: Running the Python Script
  
```python
python get_project_id.py
```
The script will authenticate using the service account credentials and print the Project ID of your GCP project.

