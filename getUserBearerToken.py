def getUserBearerToken():
    user_name = input("NAME: ")

    USER_BEARER_TOKEN = input("TOKEN: ")
    API_URL = (
        "https://troy.instructure.com/api/v1/announcements?context_codes[]=course_87909"
    )

    return user_name, API_URL, USER_BEARER_TOKEN
