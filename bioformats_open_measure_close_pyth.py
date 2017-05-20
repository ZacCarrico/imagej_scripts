### Author: Zac Carrico
### Opens up images in the bio-format (or other) format in a given folder, "measures", saves the image as a tiff, and then closes the image

import os
from java.io import File
  
from ij import IJ

import glob
folder = "C:/Users/zcarrico/Box Sync/fastsbs/exp/170502_fcFocused_fastsbs_ZC brand new flow cell vs used flow cell/Cy3_unused_flowcell/Images/L001/C0.1/"
# C:\Users\zcarrico\Box Sync\fastsbs\exp\170502_fcFocused_fastsbs_ZC brand new flow cell vs used flow cell\Cy3_unused_flowcell
os.chdir(folder)
f = glob.glob("C:/Users/zcarrico/Box Sync/fastsbs/exp/170502_fcFocused_fastsbs_ZC brand new flow cell vs used flow cell/Cy3_unused_flowcell/Images/L001/C0.1/s_1_1101_t_03.tif")
#os.chdir("C:/Users/zcarrico/Box Sync/fastsbs/exp/170501_fcFocused_fastsbs_ZC better focus imaging of flow cells with BSA and Cy3/100mg_per_ml/Images/L001/C0.1/")
#f = glob.glob("C:/Users/zcarrico/Box Sync/fastsbs/exp/170501_fcFocused_fastsbs_ZC better focus imaging of flow cells with BSA and Cy3/100mg_per_ml/Images/L001/C0.1/*.tif")
for w in f:
	IJ.run("Bio-Formats Importer", "open=[" + w + "]")
	IJ.run("Measure")
	IJ.saveAs("Tiff", w) # this overwrites the original
	IJ.run("Close")
	print(w)
print("-- Done --");

# the below commands might be useful
#	print(w)
#	IJ.run("Bio-Formats Importer", "open='" + w);
#	x = IJ.openImage(w)
#	x.show()
#	IJ.run("Subtract Background...", "rolling=50")
#	IJ.setMinAndMax(-50, 6280) # you have to set the images Min and Max before 8-bit
#	# otherwise your images are not comparable
#	IJ.run("8-bit")
#	IJ.setAutoThreshold(x, "Default dark")
#	IJ.setThreshold(12, 255)
#	IJ.run('Smooth')
#	IJ.run("Analyze Particles...", "size=60-350 circularity=0.3-1.00 show=Overlay display")
#	'''
#	x = IJ.openImage(w)
#	IJ.run("Subtract Background...", "rolling=50")
#	IJ.setMinAndMax(-50, 6280) # you have to set the images Min and Max before 8-bit
#	IJ.roiManager("Select All");
#	IJ.run("Select All");
#	roiManager("Add");
#	roiManager("Measure");


# for reasons I don't understand the below doesn't work for converting backslashes to forward slashes
#folder = "C:\Users\zcarrico\Box Sync\fastsbs\exp\170501_fcFocused_fastsbs_ZC better focus imaging of flow cells with BSA and Cy3\0mg_per_ml\Images\L001\C0.1"
#print(folder.replace('\\','/'))
#folder = folder.replace("\\", "/")
#print(folder)
#os.chdir(folder)