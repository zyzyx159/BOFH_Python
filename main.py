import getLinks
import database
import getEpisode
import getExport

#run get links
# getLinks() #I have this commented out, and yet it still runs
#test if there are new links
db = database.database()
if db.newLinks() > 0:
    getEpisode()
    getExport()
#need to build a distribution system