import pprint

from basketball_reference import Scraper
from data_objects import DailyRecord


"""
Do the thing.
"""
def main():

    gameDetailsArray = Scraper().getAllGameDetails()
    #pp.pprint(gameDetailsArray)
    
    dailyRecordArray = DailyRecord().createDailyRecordsFromGameDetails(gameDetailsArray)
    #pp.pprint(dailyRecordArray)


if __name__ == "__main__":
   pp = pprint.PrettyPrinter(indent=4)
   main()