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

c3_min = 1.
d4_min = 1.

c3_max = 10.
d4_max = 100.

n_c3 = 50
n_d4 = 50

delta_c3 = (c3_max - c3_min)/ n_c3
delta_d4 = (d4_max - d4_min)/ n_d4

c3_scan = [ delta_c3 * x + c3_min for x in range(n_c3)]
d4_scan = [ delta_d4 * x + d4_min for x in range(n_d4)]

c3_scan_pre = [delta_c3 * x for x in range(6)]
d4_scan_pre = [delta_d4 * x for x in range(6)]

c3_scan = c3_scan_pre + c3_scan
d4_scan = d4_scan_pre + d4_scan

for c3 in c3_scan:
    for d4 in d4_scan:
        new_scan = '%s_c3_%.3f_d4_%.3f'%(production,c3,d4)
        new_dir = production + '/' + new_scan

        # create dir

        if not os.path.isdir(new_dir):
            os.makedirs(new_dir)

        # read file
        # start with customize
        with open(path_to_ref + '/' + reference + customize_card, 'r') as f:
            inp = f.read() 

        inp = inp.replace('set param_card tripcoup 4 0','set param_card tripcoup 4 %.3f'%c3)
        inp = inp.replace('set param_card quartcoup 6 0','set param_card quartcoup 6 %.3f'%d4)

        #print('set param_card tripcoup 4 %.3f'%c3)
        #print('set param_card quartcoup 6 %.3f'%d4)

        with open(new_dir + '/' + new_scan + customize_card, 'w') as f:
            f.write(inp)

        # proc
        with open(path_to_ref + '/' + reference + proc_card, 'r') as f:
            inp = f.read() 

        inp = inp.replace(reference, new_scan)

        with open(new_dir + '/' + new_scan + proc_card, 'w') as f:
            f.write(inp)

        # run
        with open(path_to_ref + '/' + reference + run_card,'r') as f:
            inp = f.read() 

        inp = inp.replace(reference, new_scan)

        with open(new_dir + '/' + new_scan + run_card, 'w') as f:
            f.write(inp)

        # madspin
        with open(path_to_ref + '/' + reference + madspin_card, 'r') as f:
            inp = f.read() 

        inp = inp.replace(reference, new_scan)

        with open(new_dir + '/' + new_scan + madspin_card, 'w') as f:
            f.write(inp)

