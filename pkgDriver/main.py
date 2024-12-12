from pkgBackend import establish_connection, load_env_var, update_status
from pkgFrontEnd import menu


#update status need to be encapsulated in a while statement to work.

def main():
    CLIENT_ID = load_env_var.get_discord_client_id()

    menu.init_menu()







'''
    if CLIENT_ID is None:
        print("+++ Cannot proceed without a valid client ID +++")
    else:
        rpc = establish_connection.connect(CLIENT_ID)
        update_status.set_status(rpc)
'''


if __name__ == "__main__":
    main()