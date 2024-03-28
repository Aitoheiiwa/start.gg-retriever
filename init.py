import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def initToken():
    token = input("Give start.gg token \n")
    slug = input("Give slug where slug =  tournament/tournamentName/event/event_name \n")
    variables = "STARTGGTOKEN = \"" +  token + "\"\n" + "SLUG = \"" + slug + "\""
    
    f = open(".env", "w")
    f.write(variables)
    f.close()

def init():
    install("graphqlclient")
    install("python-dotenv")
    initToken()

init()