import json
import os


def writeDataIntoEnvFile(API_URL: str, USER_BEARER_TOKEN: str):
    API_URL_content = f'API_URL="{API_URL}"\n'
    USER_BEARER_TOKEN_content = f'USER_BEARER_TOKEN="{USER_BEARER_TOKEN}"'

    path_to_env_file = "UserData/UserInfo.env"
    with open(path_to_env_file, "w") as envFile:
        envFile.write(API_URL_content)
        envFile.write(USER_BEARER_TOKEN_content)


def writeDataIntoJsonFile(user_name: str, API_URL: str, USER_BEARER_TOKEN: str):
    user_info = {
        "NAME": user_name,
        "API_URL": API_URL,
        "USER_BEARER_TOKEN": USER_BEARER_TOKEN,
    }

    path_to_json_file = "UserData/UserInfo.json"
    with open(path_to_json_file, "w") as userInfoFile:
        json.dump(user_info, userInfoFile)


def write_data_into_file(user_name: str, API_URL: str, USER_BEARER_TOKEN):
    # Make a directory named UserData with all the file in there
    try:
        # Directory to put all the file in there
        directory = "UserData"

        # Parent Directory path
        parent_dir = os.getcwd()

        # Path to the Folder
        path = os.path.join(parent_dir, directory)

        # Create a directory
        os.mkdir(path)
    except OSError:
        # For internal purpose
        writeDataIntoEnvFile(API_URL, USER_BEARER_TOKEN)

        writeDataIntoJsonFile(user_name, API_URL, USER_BEARER_TOKEN)

        # Final Result
        print("Successfully load the data!")
    else:
        # For internal purpose
        writeDataIntoEnvFile(API_URL, USER_BEARER_TOKEN)

        writeDataIntoJsonFile(user_name, API_URL, USER_BEARER_TOKEN)

        # Final Result
        print("Successfully load the data!")

