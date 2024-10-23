import requests
from bs4 import BeautifulSoup

#setup req and bs
URL = "https://www.mlb.com/dodgers"

response = requests.get(URL)

print(response)
soup = BeautifulSoup(response.text, 'html.parser')

#top 3 headlines
headline = soup.find_all('a', {'class': 'p-headline-stack__link'}, limit=3) 
#collect most recent teams
teams = soup.find_all('div', {'data-mlb-test': 'teamRecordWrapper'}, limit=2) 
#collect most recent scores
scores = soup.find_all('div', {'data-mlb-test': 'scoreContainer'}, limit=2) 

#Just testing
#for element in headline:
#    print(element.text)
#for team in teams:
#    print(team.text[:3])
#for score in scores:
#    print(score.text)

#print results neatly -> [:3] to avoid LADLAD
if len(scores) == 0:  
    print(f"Upcoming game: \n{teams[0].text[:3]}\n{teams[1].text[:3]}")
else:
    print(f"Result of the most recent dodgers game \n{teams[0].text[:3]}: {scores[0].text}\n{teams[1].text[:3]}: {scores[1].text}")
print(f"\nTeam headlines: \n>{headline[0].text}\n\n>{headline[1].text}\n\n>{headline[2].text}")
