import vgazer.version.utils as utils

def CheckGitlab(auth, host, projectId):
    tags = auth.GetJson(
     "https://" + host + "/api/v4/projects/" + projectId + "/repository/tags")

    return utils.GetVersionFromTag(tags[0]["name"])
