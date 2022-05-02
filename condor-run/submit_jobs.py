# Script to submit jobs to condor
# author Marko Stamenkovic

 
import glob
import os

submits = glob.glob("submit_*")
submits = [os.path.basename(s) for s in submits]
 

cmd = 'condor_submit %s'

for s in submits:
    print(cmd%s)
    os.system(cmd%s)

