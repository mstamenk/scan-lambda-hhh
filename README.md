# scan-lambda-hhh
Script to scan lambda3 and lambda4 in HHH production


# Step 1: prepare repositories with Madgraph cards

Just specify which mode in the script (`GF_HHH_SM` or `VBF_HHH`) and run `python prepare_scan.py`

# Step 2: genproduction

Clone the following repository:

```
git clone git@github.com:cms-sw/genproductions.git
```

Modify the following file to account for the new models to be used:

```
# at line XX
cp -r models/loop_sm_c3d4 
```
