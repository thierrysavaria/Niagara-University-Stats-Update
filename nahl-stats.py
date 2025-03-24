import requests, os, json, csv

# URL of the web page to fetch
url = input("Please enter the url (wihtout callback and with limit=1000): ")

# Fetch the web page
response = requests.get(url)

file_path = 'nahl-players.csv'

# Remove the file if it exists
if os.path.exists(file_path):
    os.remove(file_path)    
    print(f"Existing file {file_path} has been removed.")

# Check if the request was successful
if response.status_code == 200:
    # Get the HTML content

    players = json.loads(response.text)["skaters"]

    html_content = json.dumps(players)
    with open(file_path, 'w',-1,"utf-8",newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Name', 'Pos', '#', 'Year', 'Team', 'GP','G','A','PTS','PT/G','PPG','PPA','SHG','SHA','GWG','PIM','SHO_PCT'])
        for player in players:
            writer.writerow([
                player["player_name"],
                player["plays"],
                player["jersey"],
                player["birth_year"],
                player["teams"][0]["team_ab"],
                player["games_played"],
                player["goals"],
                player["assists"],
                player["points"],
                player["point_per_game"],
                player["ppg"],
                player["ppa"],
                player["shg"],
                player["sha"],
                player["gwg"],
                player["pims"],
                player["shooting_pct"]
                ])
    
    print("HTML content saved successfully!")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")