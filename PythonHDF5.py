# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 00:17:51 2018

@author: Marko
"""

import numpy as np
import h5py

#imports my file for data gathering purposes
import sys
sys.path.insert(0, "D:\Downloads\Computer Notes\Stock App Files")
#to check the system path
sys.path
#import my code file
#import CleanAndDownload as cd
from CleanAndDownload import GetTickers as gt
#remove the code file if needed
#sys.path.remove('D:\\Downloads\\Computer Notes\\Stock App Files')

aigDaily = gt.DownloadAndClean(gt(), "daily", 'aig')
muDaily = gt.DownloadAndClean(gt(), "daily","mu")
bacDaily = gt.DownloadAndClean(gt(), 'daily', 'bac')
dnpDaily = gt.DownloadAndClean(gt(), 'daily', 'dnp')


aigDailyAdj = gt.DownloadAndClean(gt(), "dailyAdjusted", 'aig')
muDailyAdj = gt.DownloadAndClean(gt(), "dailyAdjusted","mu")
bacDailyAdj = gt.DownloadAndClean(gt(), 'dailyAdjusted', 'bac')
dnpDailyAdj = gt.DownloadAndClean(gt(), 'dailyAdjusted', 'dnp')





#allows us to play with the divs only
def divs(coll, onlyDivs = True):
    if onlyDivs:
        divs = coll.loc[:, '7. dividend amount']
        divs.plot()
        return divs
    else:
        divs = coll.loc[:, '7. dividend amount']
        divs = divs[divs > 0]
        #return divs
        divs.plot()
        return divs



import matplotlib
import matplotlib.pyplot as py


aigClose = aigDaily['4. close']


fig = matplotlib.figure()
ax = fig.add_subplot(1,1,1)




















import plotly
plotly.__version__





















from timeit import timeit

f = h5py.File(r'D:\chapter03.hdf5')
f.create_dataset("AIG", data = aigDaily)
dset = f["AIG"]
f.close()

out = dset[...]
out[:, 0:1]

dset = f.create_dataset('fixed', (2,2))
dset.shape



f = h5py.File(r'D:\imagetest.hdf5')
dset = f.create_dataset("Images", (100, 480, 640), dtype='uint8')
image = dset[0, :, :]
image.shape



dset1 = f.create_dataset('timetraces1', (1, 1000), maxshape=(None, 1000))
dset2 = f.create_dataset('timetraces2', (5000, 1000), maxshape=(None, 1000))
f.close()


f = h5py.File(r"D:\Groups.hdf5")
subgroup = f.create_group("SubGroup")
f.require_group("SubGroup")
f.require_dataset('Dataset1', (), dtype='int64')

f["Dataset1"] = 1.0
f["Dataset2"] = 2.0
f["Dataset3"] = 3.0
subgroup["Dataset4"] = 4.0
subSubGroup = subgroup.create_group("AnotherGroup")

out = f.create_group('/some/big/path')
out
f.close()






with h5py.File(r'D:\fileWithResource.hdf5', 'w') as f1:
    f1.create_group('mygroup')
    
f2 = h5py.File(r'D:\linkingFile.hdf5', 'w')
f2['linkname'] = h5py.ExternalLink(r'D:\fileWithResource.hdf5', 'mygroup')

grp = f2['linkname']
grp.name

grp.file



f = h5py.File(r'D:\attrs.hdf5')
dset = f.create_dataset('dataset', (100,))
dset.attrs
dset.attrs['title'] = 'Dataset from third round'
dset.attrs['sample rate'] = 100e6
dset.attrs['run id'] = 144






f = h5py.File(r"D:\Groups.hdf5")
subgroup = f.create_group("Subgroup")
subsubgroup = subgroup.create_group("AnotherGroup")

f["Dataset1"] = 1.0
f["Dataset2"] = 2.0
f["Dataset3"] = 3.0
subgroup["Dataset4"] = 4.0

dset4 = f["Subgroup"]["Dataset4"]
print(dset4)









f.close()














































