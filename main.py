from dotenv import load_dotenv
import os

def main():
    load_dotenv()

    CLIENT_ID = os.getenv("DISCORD_CLIENT_ID")
    print(f" Your client ID is: {CLIENT_ID}")



if __name__ == "__main__":
    main()