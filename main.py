import pypresence.exceptions

import establish_connection
import load_env_var
from pypresence import Presence


def main():
    CLIENT_ID = load_env_var.get_discord_client_id()

    if CLIENT_ID is None:
        print("Cannot proceed without a valid client ID. Check your '.env' file")
    else:
        establish_connection.connect(CLIENT_ID)




if __name__ == "__main__":
    main()