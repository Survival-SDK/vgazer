def CheckPypi(auth, project):
    projectInfo = auth.GetJson("https://pypi.org/pypi/" + project + "/json")

    return projectInfo["info"]["version"]
