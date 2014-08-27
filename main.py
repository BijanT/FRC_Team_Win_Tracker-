from Team import Team

#trackingTeam will stay true as long as the user wants to look up teams. Will be set to false when the user is done with the program
trackingTeam = True

while trackingTeam:
	#find out which team the user wants to track
	team = ""
	print("Which team to you want to track?")
	teamNumber = raw_input()
	#make sure the input is a valid team number (in this case that means no letters and less than five digits)
	while (not teamNumber.isdigit()) or (len(teamNumber) >= 5):
		#Continue asking for the team number until a valid team number is entered
		print("Invalid input. Try again")
		teamNumber = raw_input()
	print("")#Add a new line to make things look nice
	#Create the instance of the team
	team = Team(teamNumber)
	
	print(team.getNickname())
	print("Rookie Year: " + team.getRookieYear())
	print("Won the Chairman's Award " + team.getNumChairmans() + " time[s]")
	print("Won Engineering Inspiration " + team.getNumEI() + " time[s]")
	print("Winner of an event " + team.getNumWins() + " time[s]")
	print("Finalist of an event " + team.getNumFinals() + " time[s]")
	print("Won " + team.getNumOtherAwards() + " other award[s]")
	
	
	#Ask the user if he/she wants to track another team
	print("\nDo you want to track another team? y/n")
	answer = str(raw_input())
	#if the input was anything other than 'y' or 'Y,' exit the loop
	if (answer != "y") and (answer != "Y"):
		trackingTeam = False
		
print("Goodbye!")
