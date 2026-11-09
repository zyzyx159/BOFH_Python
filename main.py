import getLinks
import database
import getEpisode
import getExport

db = database.database()
if db.newLinks() > 0:
    getEpisode()
    getExport()
#need to build a distribution system