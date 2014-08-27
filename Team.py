import urllib2

class Team:
	def __init__(self, teamNumber):
		#This is the header required to get data from the blue alliance
		self.header = {"X-TBA-App-Id" : "bijan_taba:FRC_Team_Win_Tracker:v0.1"}
		#The base url for the api
		self._baseURL = "http://www.thebluealliance.com/api/v2/team/"
	
		self.teamKey = "frc"+teamNumber#Add frc to the team number so it can be recognized by TBA
		
		#first request the team information from TBA to find the team's rookie year
		url = self._baseURL + self.teamKey
		print(url)
		#Create a request for the team's information
		request = urllib2.Request(url, None, self.header)
		response = urllib2.urlopen(request)
		self.teamInfo = response.read()
		
	def getTeamInfo(self):
		return self.teamInfo