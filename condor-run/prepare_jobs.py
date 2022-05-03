# Script to prepare jobs to be submitted on condor
# author Marko Stamenkovic

# import 
import os
import glob

# inputs

channel = 'GF_HHH_SM'

files = glob.glob('../%s/*'%channel)
files = [os.path.basename(f) for f in files]


with open('job.sh', 'r') as f:
    job_script = f.read()

with open('submit', 'r') as f:
    submit = f.read()

for fil in files:
    with open('job_%s.sh'%fil, 'w') as f:
        f.write(job_script.replace('GF_HHH_SM_c3_0_d4_0',fil))


    with open('submit_%s.sh'%fil,'w') as f:
        new_submit = submit.replace('job.sh', 'job_%s.sh'%fil)
        new_submit = new_submit.replace('output/job.$(ClusterId).$(ProcId).out','output/job_%s.$(ClusterId).$(ProcId).out'%fil)
        f.write(new_submit)
        

print("Done preparing jobs for condor")


