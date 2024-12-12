
from dotenv import load_dotenv
import os


def get_discord_client_id():
    load_dotenv()
    CLIENT_ID = os.getenv("DISCORD_CLIENT_ID")

    if CLIENT_ID is None:
        print("+++ WARNING: Client ID is NON-EXISTENT, check your .env file! +++")
        return None

    return CLIENT_ID

    #error checking could be better here.

