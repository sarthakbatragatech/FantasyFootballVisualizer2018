from bs4 import BeautifulSoup
import requests
import os


def collect(position):

	# Dictionary mapping every position to its correct 'NFLURL' value 
	position_Dict = {'QB': 1, 'RB': 2, 'WR': 3, 'TE': 4, 'K': 7, 'DEF': 8}
	
	# Url for fantasy points each NFL team allows to each position
	url = "https://fantasy.nfl.com/research/pointsagainst?leagueId=0&position=" + str(position_Dict[position]) + "&sort=pointsAgainst_pts&statCategory=pointsAgainst&statSeason=2018&statType=seasonPointsAgainst"
	html_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
	r = requests.get(url, html_headers)
	print("Request Sent...")
	print("Request Status is %d \n" %r.status_code)

	cwd = os.getcwd()

	## Writing request content as a txt file
	# textfile = cwd + "/stats.txt"
	# outfile = open(textfile, "w")
	# outfile.write(str(r.text.encode('utf-8')))

	soup = BeautifulSoup(r.content, "html.parser")

	# Write 'prettified' html content to a text file
	textfile = cwd + "/" + position + "urlrawhtml.txt"
	outfile = open(textfile, "w")
	outfile.write(str(soup.prettify()))
	print("Writing raw html to output text file...\n")


	# Column names for the csv file

	## Option 1: Grab all column headers from the table on the website
	# csv_headers = ''
	# webtable_rows = soup.find("tr", {"class":"last"})
	# webtable_headers = webtable_rows.find_all("th")
	# for header in webtable_headers:
	#     csv_headers = csv_headers + header.get_text() + ','
	# print(csv_headers)

	# Option 2: Use custom headers for better readability
	csv_headers = "Team,Opposition,AvgPtsAllowed,Rank,PassingComp,PassingAtt,PassingYds,PassingInt,PassingTD,RushingAtt,RushingYds,RushingTD,RZTouch,RZG2G\n"

	filename = position + "pointsAgainst.csv"
	f = open(filename, "w", encoding='utf-8')
	f.write(csv_headers)
	print("Setting up csv and writing headers...\n")


	# Grab values for each column for all 32 teams
	# "team-31 odd first"
	wasted_permute = 0
	for i in range(1, 33):
		csv_row_data = ''
		team_row_data_permut1 = soup.find("tr", {"class":"team-"+str(i)+ " odd first"})
		team_row_data_permut2 = soup.find("tr", {"class":"team-"+str(i)+ " even first"})
		team_row_data_permut3 = soup.find("tr", {"class":"team-"+str(i)+ " odd last"})
		team_row_data_permut4 = soup.find("tr", {"class":"team-"+str(i)+ " even last"})
		team_row_data_permut5 = soup.find("tr", {"class":"team-"+str(i)+ " odd"})
		team_row_data_permut6 = soup.find("tr", {"class":"team-"+str(i)+ " even"})
    
		all_permuts = [team_row_data_permut1, team_row_data_permut2, team_row_data_permut3, team_row_data_permut4, team_row_data_permut5, team_row_data_permut6]

		# fix vs QB, vs RB before writing to csv, not done yet!!!!, currently being fixed in clean data portion
		# Only one permut is nonempty and contains the data, retain that
		for item in all_permuts:
			if item is not None:
				team_row_data = item
    
		team_row_data = team_row_data.find_all("td")
		for item in team_row_data:
				csv_row_data = csv_row_data + item.get_text() + ','

		# Hacky fix to get rid of a comma at the end
		csv_row_data = csv_row_data[:-1] 

		# print((csv_row_data))
		f.write(csv_row_data)
		f.write("\n")

	print("Data for the " + position + " position written to csv...\n")
