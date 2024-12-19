import episode
import export
import os
import database

# epi = episode.episode("https://www.theregister.com/2000/05/09/wanted_bastard_operators_to_man/")
# epi.DBInit()

# out = export.export(epi)
# out.writeFile()

bofhDB = database.database()
for link in bofhDB.getLinks():
    epi = episode.episode(link[0])
    epi.DBInit()
    out = export.export(epi)
    out.writeFile()