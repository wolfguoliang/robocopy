import os
source=raw_input("pls input source documnet:")
des=raw_input ("pls input destination document:")
cop=("robocopy %s %s /e /copyall /mot:1 /mon:2")%(source,des)
robo=os.system(cop)
if robo == 0:
    print "backup successful"
else:
    print  "soory"