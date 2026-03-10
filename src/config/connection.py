from dotenv import load_dotenv
from mysql import connector
import os


class Connection:
    def __init__(self):
        load_dotenv()
        self.dbName = os.getenv("DBNAME")
        self.user = os.getenv("DBUSER")
        self.host = os.getenv("HOST")
        self.port = os.getenv("PORT")
        self.password = os.getenv("PASSWORD")

    def data(self):
       return {
           "dbName": self.dbName,
           "user": self.user,
           "host": self.host,
           "port": self.port,
           "password": self.password
       }

    def viewData(self):
        print(f"{self.dbName}\n{self.user}\n{self.host}\n{self.port}\n{self.password}")

    def connect(self):
        try:

            database = connector.connect(
                host=self.host,
                user=self.user,
                port=self.port,
                password=self.password,
                database=self.dbName
            )
            return database
        except connector.Error as e:
            print(e)
