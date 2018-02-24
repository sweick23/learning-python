marker = "AFK"
replacement = "away from keyboard"
line = "I will now go to sleep and be AFK until lunch time tomorrow."

afk = line.find(marker)
rep = line[:afk]
rep_after_afk = line[afk+len(marker):]
replaced =  rep + replacement + rep_after_afk

print replaced
