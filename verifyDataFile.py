import os
from dotenv import load_dotenv
from contextlib import contextmanager
import json
from verifyUserBearerToken import verifyUserBearerToken

def verifyJsonFile(filename: any, mode: any):
    try:
      with open(filename, mode) as jsonFile:
        user_data = json.load(jsonFile)
        API_URL = user_data['API_URL']
        USER_BEARER_TOKEN = user_data['USER_BEARER_TOKEN']
        
    except FileNotFoundError:
        return False
        
    except json.JSONDecodeError:
        return False
    
    except KeyError:
        return False
       
    except Exception:
        return False
    
    return True
    

@contextmanager
def readJsonFile(filename: any, mode: any):
    
    userInfoFile = open(filename, mode)
    try:
        user_data = json.load(userInfoFile)
        USER_BEARER_TOKEN = user_data['USER_BEARER_TOKEN']
        yield user_data
               
    except Exception:
        print('Please update your information...')
        # Ask the user to type USER_BEARER_TOKEN
    
    finally:
        userInfoFile.close()

    
def readEnvFile(path_to_env_file):
    load_dotenv(path_to_env_file)

    API_URL = os.getenv('API_URL')
    USER_BEARER_TOKEN = os.getenv('USER_BEARER_TOKEN')
    headers = {
        'Authorization': 'Bearer {USER_BEARER_TOKEN}'.format(USER_BEARER_TOKEN=USER_BEARER_TOKEN),
    }
    return API_URL, headers
