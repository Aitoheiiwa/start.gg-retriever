import querys
import os
def getSlug():
    if os.getenv('SLUG') == None:
        slug = input("Give slug where slug =  tournament/tournamentName/event/event_name \n")
    return slug
def main():

    id = querys.getID(os.getenv('SLUG'))
    teams = querys.getTeams(id)

    teams_name = ""

    for team in teams['nodes'] :
        teams_name += team['name'] + "\n"

    teams_name = teams_name[0:-1]
    f = open("./Output/Teams.txt", "w", encoding= "utf-8")
    f.write(teams_name)

    print(teams_name)


main()