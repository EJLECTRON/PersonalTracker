from pymongo import MongoClient
import certifi
import os
from dotenv import load_dotenv

load_dotenv()

# Create the MongoClient with authentication credentials
client = MongoClient(os.getenv("SECRET_ADMIN_LINK"),
                     tlsCAFile=certifi.where(),
                     username=os.getenv("ADMIN_NAME"),
                     password=os.getenv("ADMIN_PASSWORD"))

# Access the admin database
db = client.admin

# Print the names of all databases
for db_name in client.list_database_names():
    print(db_name)

#db.command("createUser", "user", pwd="password", roles=["read"])
