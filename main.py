import getLinks
import database
import getEpisode
import getExport

#run get links
getLinks()
#test if there are new links
if database.database.newLinks() > 0:
    getEpisode()
    getExport()
#need to build a distribution system