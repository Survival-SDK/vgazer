from vgazer.exceptions import CompatibleProjectNotFound

def PrintVersion(gazer, software):
    try:
        print(software + ":", gazer.CheckVersion(software))
    except CompatibleProjectNotFound:
        print(software + ":", "N/A")
