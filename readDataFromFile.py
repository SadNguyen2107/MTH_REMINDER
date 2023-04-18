from verifyDataFile import readEnvFile, readJsonFile, verifyJsonFile
from getUserBearerToken import getUserBearerToken
import os
import json

def retrieveDataFromFile():
    # Read data from UserInfo.env file
    path_to_env_file = os.path.abspath('UserData/UserInfo.env')
    API_URL, headers = readEnvFile(path_to_env_file)
    
    if API_URL is not None and headers['Authorization'] != 'Bearer None':
        return API_URL, headers
    
    # Then read data from .json file
    path_to_json_file = os.path.abspath('UserData/UserInfo.json')
    
    # IF fail retrieve
    if verifyJsonFile(path_to_json_file, 'r') == False:
        
        print('Please update your information...')
        # Ask the user to type USER_BEAER_TOKEN
        user_name, API_URL, USER_BEARER_TOKEN = getUserBearerToken()
        headers = {
            'Authorization': f'Bearer {USER_BEARER_TOKEN}',
        }
        return API_URL, headers
            
    # For success retreive
    with readJsonFile(path_to_json_file, 'r') as user_data:
        
        API_URL = user_data['API_URL']
        USER_BEARER_TOKEN = user_data['USER_BEARER_TOKEN']
        headers = {
            f'Authorization': 'Bearer {USER_BEARER_TOKEN}',
        }
        return API_URL, headers