import urllib2

class Team:
	def __init__(self, teamNumber):
		#This is the header required to get data from the blue alliance
		self.header = {"X-TBA-App-Id" : "bijan_taba:FRC_Team_Win_Tracker:v0.2"}
		#The base url for the api
		self.baseURL = "http://www.thebluealliance.com/api/v2/team/"
		
		self.teamKey = "frc"+teamNumber#Add frc to the team number so it can be recognized by TBA
		self.events = []
		self.yearsParticipated = []
		#first request the team information from TBA to find the team's rookie year
		url = self.baseURL + self.teamKey
		
		#Create a request for the team's information
		request = urllib2.Request(url, None, self.header)
		response = urllib2.urlopen(request)
		self.teamInfo = response.read()
		
		#Search for the team's nickname
		locOfNickname = self.teamInfo.find("nickname")#finds the index location of "nickname"
		self.nickname = self.teamInfo[(locOfNickname+12):(len(self.teamInfo)-2)]#the nickname starts 12 chars away from the index of "nickname" and ends 2 chars from the end of the string
		
		#search teamInfo to find the team's rookie year
		locOfRookieYear = self.teamInfo.find("rookie_year")#find the index location of the "rookie_year"
		self.rookieYear = self.teamInfo[(locOfRookieYear+14):(locOfRookieYear+18)]#The first number of the rookie year is 14 chars away from the index of "rookie_year" and the last is 18 chars away
		
	def getYearsParticipated(self):
		#if the years participated list is already filled, just return it
		if self.yearsParticipated:
			return self.yearsParticipated
			
		#get the years that the team has participated in
		url = self.baseURL + self.teamKey + "/years_participated"
		request = urllib2.Request(url, None, self.header)
		response = urllib2.urlopen(request)
		rawYears = response.read()
		
		#Separate the raw response into individual years
		for i in range(1, len(rawYears), 6):#The years start at the index 1 and the years are 6 characters apart from each other
			self.yearsParticipated.append(rawYears[i:i+4])
			
		return self.yearsParticipated
		
	def getEvents(self):
		#If the events list is already filled, just return it
		if self.events:
			return self.events
		
		eventText = ""
		
		#Get all the events the team attended since its rookie year 
	
	def getNickname(self):
		return self.nickname
		
	def getRookieYear(self):
		return self.rookieYear