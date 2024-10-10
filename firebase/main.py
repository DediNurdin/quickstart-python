import json
import google.auth
from google.oauth2 import service_account
import google.auth.transport.requests

SERVICE_ACCOUNT_FILE = './dens-prop-firebase-adminsdk-6m7vf-668bde13b9.json'

SCOPE = ['https://www.googleapis.com/auth/firebase.messaging']

credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPE)

request = google.auth.transport.requests.Request()
credentials.refresh(request)

print(credentials.token)