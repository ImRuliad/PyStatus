import load_env_var


def main():


    CLIENT_ID = load_env_var.get_discord_client_id()
    print(f" Your client ID is: {CLIENT_ID}")



if __name__ == "__main__":
    main()