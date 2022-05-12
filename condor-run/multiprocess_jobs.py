# Script to submit jobs to condor
# author Marko Stamenkovic

 
import glob
import os
from multiprocessing import Pool, cpu_count

submits = glob.glob("job_GF*.sh")
submits = [os.path.basename(s) for s in submits]

outputs = glob.glob('../genproductions/bin/MadGraph5_aMCatNLO/*.xz')
outputs = [os.path.basename(o) for o in outputs]
outputs = [o.replace('_slc7_amd64_gcc700_CMSSW_10_6_19_tarball.tar.xz','') for o in outputs]

print(len(submits))
for s in submits:
    for o in outputs:
        if o in s:
            submits.remove(s)
            print("Removing %s"%s)

print(len(submits))
cmd = 'sh %s'

def process(submit):
    print(cmd%submit)
    os.system(cmd%submit)

print("Launching remaining jobs")
p = Pool(2)
p.map(process,submits)
p.close()

#for s in submits:
#    process(s)

