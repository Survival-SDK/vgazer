def GithubCheckApiRateLimitExceeded(responseJson):
    if "message" in responseJson:
        if (responseJson["documentation_url"]
         == "https://developer.github.com/v3/#rate-limiting"):
            return True
    return False
