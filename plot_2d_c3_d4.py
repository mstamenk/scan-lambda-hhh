# Script to plot the lambda3 and lambda4 contributions from ggF HHH
# author Marko Stamenkovic

import os
import glob
import ROOT
import tdrstyle,CMS_lumi
import re

from array import array


# path

path = 'genproductions/bin/MadGraph5_aMCatNLO/'

log_files = glob.glob(path + '/' + '*.log')

# set cms style
tdrstyle.setTDRStyle()
CMS_lumi.extraText = "Internal"
CMS_lumi.writeExtraText = 1
CMS_lumi.lumi_sqrtS = "13 TeV"

# main

regexp = 'Cross-section :   (.*) pb'
xsec_sm = 0.03253

#print(log_files)


x = []
y = []

for log in log_files:
    filename = os.path.basename(log)

    c3 = float(filename.split('_')[4])
    d4 = float(filename.split('_')[6].replace('.log',''))
    lam3 = c3+1
    lam4 = d4+1

    print(c3,d4)
    x.append(lam3)
    y.append(lam4)


x = list(set(x))
y = list(set(y))

print(len(x)-1,min(x),max(x),len(y)-1,min(y),max(y))

h_2D = ROOT.TH2F('xsec', 'xsec', len(x),min(x),max(x),len(y),min(y),max(y))

maxi = 0

for log in log_files:
    filename = os.path.basename(log)

    with open(log, 'r') as f:
        text = f.read()

    print(log)
    try:
        match = re.findall(regexp,text)[0]
        xsec = float(match.split('+-')[0])
        error = float(match.split('+-')[1])
    except:
        print('No xsec in %s'%log)
        continue

    c3 = float(filename.split('_')[4])
    d4 = float(filename.split('_')[6].replace('.log',''))
    lam3 = c3+1
    lam4 = d4+1

    print(lam3,lam4,xsec)
    x_bin = h_2D.GetXaxis().FindBin(lam3)
    y_bin = h_2D.GetYaxis().FindBin(lam4)
    print(x_bin, y_bin, xsec * 1000, xsec * 1000 / xsec_sm)
    h_2D.SetBinContent(x_bin, y_bin, xsec * 1000 / xsec_sm)
    maxi = max(maxi,xsec*1000)

print(maxi) 
x_contour = array('d')
x_contour.append(1)
x_contour.append(10)
x_contour.append( 50)
x_contour.append( 100)
x_contour.append( 250)
x_contour.append( 500)
#x_contour.append(550)

h_2D.SetMinimum(0)

h_2D_cont = h_2D.Clone('contour')

h_2D_cont.SetContour(len(x_contour), x_contour)
h_2D.SetContour(600)
#h_2D.SetMaximum(h_2D.GetMaximum()*1.3)

h_2D.GetXaxis().SetTitle('#kappa_{#lambda_{3}}')
h_2D.GetYaxis().SetTitle('#kappa_{#lambda_{4}}')
h_2D.GetZaxis().SetTitle('#sigma(HHH) / #sigma_{SM}(HHH)')
h_2D.GetZaxis().SetNdivisions(30)
ROOT.gStyle.SetPalette(ROOT.kRainBow)
c = ROOT.TCanvas('c','c',900,900)
c.SetRightMargin(0.2)
h_2D.Draw("colz")
h_2D_cont.Draw('cont3 same')
c.Print('Plot_2D.pdf')
