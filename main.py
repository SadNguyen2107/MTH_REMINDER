import requests
from openWebBrowser import openWebBrowser
import readDataFromFile
from createShortcut import createShortcut
import sys
from verifyUserBearerToken import verifyUserBearerToken
from getUserBearerToken import getUserBearerToken
from writeDataToFile import write_data_into_file
from writeHTMLResponse import createDirectoryHTMLfile

# * Get API, headers, USER_BEARER_TOKEN
API_URL, headers = readDataFromFile.retrieveDataFromFile()

try:
    # * SEND a GET Request
    response = requests.get(API_URL, headers=headers)

except requests.exceptions.ConnectionError:  # If the wifi connection is unstable
    print("Wifi Error!")

else:
    

    # * CHECK USER_BEARER_TOKEN valid or not
    check_tokens = verifyUserBearerToken(response.status_code, API_URL)
    while valid_token := next(check_tokens) == False:
        user_name, API_URL, USER_BEARER_TOKEN = getUserBearerToken()

        valid_token = check_tokens.send(USER_BEARER_TOKEN)

        # * IF changed then write data to the file
        # * and Change the respone
        if valid_token: 
            write_data_into_file(user_name, API_URL, USER_BEARER_TOKEN)
            headers = {
                "Authorization": f"Bearer {USER_BEARER_TOKEN}",
            }
            response = requests.get(API_URL, headers=headers)
            break

    
    # * then WRITE response
    data = response.json()

    if data == []:
        openWebBrowser(blank=True)

        # * Will get rid of this in the future
        print("Cannot retrieve the data currently")
        sys.exit()

    createDirectoryHTMLfile(data_response=data)
    
    # Open a webrowser
    openWebBrowser(blank=False)


finally:
    # Create a shortcut
    createShortcut()