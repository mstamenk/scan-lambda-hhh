# Script to clean prod repo with multiprocessing

import glob, os
from multiprocessing import Pool, cpu_count

channel = 'GF_HHH_SM'

files = glob.glob('genproductions/bin/MadGraph5_aMCatNLO/%s*'%channel)
files = [f for f in files if 'log' not in f and 'tar.xz' not in f]

outputs = glob.glob('genproductions/bin/MadGraph5_aMCatNLO/*.xz')
outputs = [os.path.basename(o) for o in outputs]
outputs = [o.replace('_slc7_amd64_gcc700_CMSSW_10_6_19_tarball.tar.xz','') for o in outputs]

to_remove = []
print(outputs,files)
for f in files:
    for o in outputs:
        if o in f:
            to_remove.append(f)
            
def clean(f):
    cmd = 'rm -rf %s'%f
    print(cmd)
    os.system(cmd)


p = Pool(3)
p.map(clean,to_remove)
