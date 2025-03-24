import requests, os, json, csv

# URL of the web page to fetch
file_name = input("Please enter the name of the league (ex : ajhl): ")
url = input("Please enter the url (wihtout callback and with limit=1000): ")

# Fetch the web page
response = requests.get(url)

file_path = file_name+'-players.csv'

# Remove the file if it exists
if os.path.exists(file_path):
    os.remove(file_path)
    print(f"Existing file {file_path} has been removed.")

# Check if the request was successful
if response.status_code == 200:
    # Get the HTML content

    players = json.loads(response.text[1:-1])[0]["sections"][0]["data"]

    html_content = json.dumps(players)
    with open(file_path, 'w',-1,"utf-8",newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Name', 'Pos', '#', 'Team', 'GP','G','A','PTS','PT/G','PPG','PPA','SHG','GWG','PIM'])
        for player in players:
            writer.writerow([
                player["row"]["name"],
                player["row"]["position"],
                player["row"]["jersey_number"],
                player["row"]["team_code"],
                player["row"]["games_played"],
                player["row"]["goals"],
                player["row"]["assists"],
                player["row"]["points"],
                player["row"]["points_per_game"],
                player["row"]["power_play_goals"],
                player["row"]["power_play_assists"],
                player["row"]["short_handed_goals"],
                player["row"]["game_winning_goals"],
                player["row"]["penalty_minutes"],
                ])
    
    print("HTML content saved successfully!")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")