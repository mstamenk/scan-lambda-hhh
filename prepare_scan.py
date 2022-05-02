# Script to prepare the cross-section scans of lambda3 and lambda4
# author Marko Stamenkovic

# import 

import os

# global variables


customize_card = '_customizecards.dat'
proc_card = '_proc_card.dat'
run_card = '_run_card.dat'
madspin_card = '_madspin_card.dat'

production = 'GF_HHH_SM'
reference = '%s_c3_0_d4_0'%production

path_to_ref = production + '/' + reference


# main

c3 = 1
d4 = 1

n_c3 = 11
n_d4 = 11

c3_scan = [ x for x in range(n_c3)]
d4_scan = [ 10 * x for x in range(n_d4)]

for c3 in c3_scan:
    for d4 in d4_scan:
        new_scan = '%s_c3_%d_d4_%d'%(production,c3,d4)
        new_dir = production + '/' + new_scan

        # create dir

        if not os.path.isdir(new_dir):
            os.makedirs(new_dir)

        # read file
        # start with customize
        with open(path_to_ref + '/' + reference + customize_card) as f:
            inp = f.read() 

        inp = inp.replace('set param_card tripcoup 4 0','set param_card tripcoup 4 %s'%c3)
        inp = inp.replace('set param_card quartcoup 6 0','set param_card quartcoup 6 %s'%d4)

        with open(new_dir + '/' + new_scan + customize_card, 'w') as f:
            f.write(inp)

        # proc
        with open(path_to_ref + '/' + reference + proc_card) as f:
            inp = f.read() 

        inp = inp.replace(reference, new_scan)

        with open(new_dir + '/' + new_scan + proc_card, 'w') as f:
            f.write(inp)

        # run
        with open(path_to_ref + '/' + reference + run_card) as f:
            inp = f.read() 

        inp = inp.replace(reference, new_scan)

        with open(new_dir + '/' + new_scan + run_card, 'w') as f:
            f.write(inp)

        # madspin
        with open(path_to_ref + '/' + reference + madspin_card) as f:
            inp = f.read() 

        inp = inp.replace(reference, new_scan)

        with open(new_dir + '/' + new_scan + madspin_card, 'w') as f:
            f.write(inp)

