import requests


def checkResponseStatusCode(response_status_code):
    if response_status_code == 401:
        return False  # 'Invalid Token'

    elif response_status_code == 404:
        return False  # 'Resource Not Found'

    elif response_status_code == 200:
        return True  # 'Valid Token'

    else:
        return False


def verifyUserBearerToken(response_status_code: int, API_URL: any):
    while True:
        status = checkResponseStatusCode(response_status_code)
        USER_BEARER_TOKEN = yield status

        new_headers = {
            "Authorization": f"Bearer {USER_BEARER_TOKEN}"
        }

        respone = requests.get(API_URL, headers=new_headers)
        response_status_code = respone.status_code
