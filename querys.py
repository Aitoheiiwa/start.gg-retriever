from graphqlclient import GraphQLClient
import json
import os
from dotenv import load_dotenv
load_dotenv()
token = os.getenv('STARTGGTOKEN')
apiVersion = "alpha"
client = GraphQLClient('https://api.start.gg/gql/' + apiVersion)
client.inject_token('Bearer ' + token)

def  getID(slug):
    
    result = client.execute(""" 
query EventId($eventSlug :String!) {
  event(slug: $eventSlug) {
    slug
    id
    name
    }
}""" , 
{
    "eventSlug" : slug
}
                        )
    
    return json.loads(result)['data']['event']['id']

def getTeams(id):
    result = client.execute("""
query EventEntrants($eventID : ID!) {
    event(id : $eventID) {
        id
        name
        entrants( query: { } )
            {   pageInfo{
                        total
            }
                nodes {
                        name
                        id
                        participants {
                            id
                            gamerTag
                        }
                }
            }
    }
}                      
                            """,
{
    'eventID' : id
}                            
                            )
    
    return json.loads(result)['data']['event']['entrants']