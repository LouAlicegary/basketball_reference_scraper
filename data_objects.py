class DailyRecord(object):
    

    """
    Takes in an array of game details (date, home/away, scores) and spits out an array of "daily" style records
    """
    def createDailyRecordsFromGameDetails(self, gameDetailsArray):
        
        dailyRecordArray = []

        teamRecordArray = self.__createEmptyRecordDict()

        for game in gameDetailsArray:
            
            winnerLoserDetails = self.__getWinnerAndLoserDetails(game)
            
            if winnerLoserDetails:
                updatedWLRecords = self.__updateWLRecords(teamRecordArray, winnerLoserDetails)
                winnerRecord = self.__createDailyTeamRecord(winnerLoserDetails["date"], winnerLoserDetails["winner"], updatedWLRecords["winnerRecord"])
                loserRecord = self.__createDailyTeamRecord(winnerLoserDetails["date"], winnerLoserDetails["loser"], updatedWLRecords["loserRecord"])
                dailyRecordArray.extend((winnerRecord, loserRecord))

        print teamRecordArray

        return dailyRecordArray


    """
    Creates a dictionary to hold each team's running win/loss record
    """
    def __createEmptyRecordDict(self):
        
        teamArray = [u'Los Angeles Lakers', u'Chicago Bulls', u'San Antonio Spurs', u'Philadelphia 76ers', u'Detroit Pistons', u'Boston Celtics', u'Miami Heat', u'Orlando Magic', u'Portland Trail Blazers', u'Golden State Warriors', u'New York Knicks', u'Washington Wizards', u'Utah Jazz', u'Dallas Mavericks', u'Minnesota Timberwolves', u'Los Angeles Clippers', u'Oklahoma City Thunder', u'Charlotte Hornets', u'Milwaukee Bucks', u'Memphis Grizzlies', u'Toronto Raptors', u'Houston Rockets', u'Phoenix Suns', u'Sacramento Kings', u'New Orleans Pelicans', u'Cleveland Cavaliers', u'Atlanta Hawks', u'Brooklyn Nets', u'Indiana Pacers', u'Denver Nuggets']
        
        recordDict = {}
        
        for team in teamArray:
            recordDict[team] = {"win": 0, "loss": 0}

        return recordDict


    """
    Takes a game details object (date, visitor/home, and scores) and calculates winner and loser
    Discards any games set to occur in the future
    """
    def __getWinnerAndLoserDetails(self, gameDetails):


        if (gameDetails["visitorScore"] == 0 and gameDetails["homeScore"] == 0):
            # print("On", gameDetails["date"], gameDetails["visitor"], "play at", gameDetails["home"])
            return None
        else:
            if (gameDetails["visitorScore"] > gameDetails["homeScore"]):
                winner = gameDetails["visitor"]
                winnerScore = gameDetails["visitorScore"]
                loser = gameDetails["home"]
                loserScore = gameDetails["homeScore"]
            else: 
                winner = gameDetails["home"]
                winnerScore = gameDetails["homeScore"]
                loser = gameDetails["visitor"]
                loserScore = gameDetails["visitorScore"]

            newItems = {
                "winner": winner,
                "winnerScore": winnerScore,
                "loser": loser,
                "loserScore": loserScore
            }

            gameDetails.update(newItems)

            return gameDetails


    """
    Updates the win/loss record dict for the two teams that played
    """
    def __updateWLRecords(self, teamRecordArray, winnerLoserDetails):

        winnerRecord = teamRecordArray[winnerLoserDetails["winner"]]
        loserRecord = teamRecordArray[winnerLoserDetails["loser"]]
        winnerRecord["win"] += 1
        loserRecord["loss"] += 1

        return {
            "winnerRecord": winnerRecord,
            "loserRecord": loserRecord
        }


    """
    Creates two "daily" format records from the game details and updated win/loss stats
    """
    def __createDailyTeamRecord(self, date, team, teamRecord):

        return {
            "date": date,
            "team": team,
            "win": teamRecord["win"],
            "loss": teamRecord["loss"]
        }
