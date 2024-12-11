import pypresence
from pypresence import Presence


def connect(CLIENT_ID):
    rpc = Presence(CLIENT_ID)
    try:
        if rpc.connect():
            print("Connection Successful!")
        else:
            print("Failed to connect")
    except pypresence.exceptions.InvalidID as e:
        print(f"ERROR: {e}")
        print("The Client ID provided might be incorrect. Please check your '.env' file")
