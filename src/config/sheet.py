import os
import json
import gspread
from google.oauth2.service_account import Credentials

class Sheet:
    def __init__(self):
        self.credential = json.loads(os.getenv("AUTH_GOOGLE"))
        self.scopes = [
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive"
        ]

    def connect(self):
        credentials = Credentials.from_service_account_info(
            self.credential,
            scopes = self.scopes
        )

        client = gspread.authorize(credentials)
        return client