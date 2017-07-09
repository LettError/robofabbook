# robothon 2009
# edit the nametable
# this seems to work in FontLab 5
# it is broken in FontLab 4.6

from robofab.world import CurrentFont
from robofab.tools.nameTable import NameTable
f = CurrentFont()
nt = NameTable(f)

# bluntly set all copyright records to a string
nt.copyright = "Copyright 2006 RoboFab"

# get a record
print nt.copyright

# set a specific record to a string
nt.setSpecificRecord(pid=1, eid=0, lid=0, nid=0,
	value="You Mac-Roman-English folks should know\\
	that this is Copyright 2004 RoboFab.")

# get a record again to show what happens
# when the records for a NID are not the same
	
print nt.copyright
# look at the code to see what else is possible
f.update() 
