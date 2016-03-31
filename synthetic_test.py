# tests for synthetic graph database

import synthetic as s

#uptown train example
uptown_stations = s.EntrySpace([168, 157, 145, 137, 125, 116, 110, 103, 96, 81, 72, 66, 59, 50, 42])
local_1 = s.Field(uptown_stations)
express_2 = s.Field(uptown_stations)
express_3 = s.Field(uptown_stations)


#print "entryspace entries: " + str(express_3.entrySpace.entries)
#print "how many entries? " + str(express_3.howManyEntries())
print "adding 157..."
express_3.addEntry(157)
print "express_3.entrySpace entries with 157: " + str(express_3.entrySpace.entries)
express_2.addEntry(157)
print "express_2.entrySpace entries with 157: " + str(express_2.entrySpace.entries)
#for entry in express_3.revealEntries():
#	print entry
print "adding canal... "
express_3.addEntry("canal")
print "adding canal again..."
express_3.addEntry("canal")
print "express_3 with canal added twice: " + str(express_3.entrySpace.entries)
print express_3.allEntries2()
express_3.addLink(157,'canal')
print "added canal as neighbor of 157..."
print "who is a neighbor of 157?" + str( express_3.neighbors(157))
print "adding and deleting Simpson Ave"
express_3.addEntry("Simpson Ave")
express_3.killEntry("Simpson Ave")
print express_3.allEntries2()
print express_3.countRelations()

s.audit([express_3])

#update write() and read() to accomodate design



