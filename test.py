import episode
import export

epi = episode.episode("https://www.theregister.com/2024/11/22/bofh_2024_episode_22/")
epi.DBInit()

out = export.export(epi)