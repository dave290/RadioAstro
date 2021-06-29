#plotkel.py
#plots a single data scan from a .kel file
#this is not required for the fit.py core program

import read_parameters
import read_datafilename

#Initial values for list variables specific to each set of .kel files
A=read_datafilename.get_datafilename()
file=[str(A[0])]
coordinate=[str(A[1])]
print(file)
print(coordinate)

frequencyA=[0]        #defines value of first item in array
intensityA=[0]        #defines value of first item in array
stuff=read_parameters.get_stuff()
startline=stuff[1]
endline=stuff[2]

for workingfile in file:
    with open(workingfile, 'r') as f:    
        N=0
        for line in f:
            N=N+1
            if N>=startline and N<=endline:
                linestring=line.split()      
                frequency=float(linestring[1])
                frequencyA.append(frequency)
                intensity=float(linestring[2])
                intensityA.append(intensity)
    f.closed
    True
    frequencyA[0]=frequencyA[1]
    intensityA[0]=intensityA[1]

import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
fig=plt.figure(figsize=(10,6))
ax=plt.axes()
#title
ax.set_title("Intensity_(Kelvins) vs " + A[1])
#label axes
ax.set_xlabel(A[1])
ax.set_ylabel("Intensity_(K)")
#set axis endpoints
#ax.set_xlim(1419500000,1421500000)
#set axis ticks
#ax.set_xticks([1419500000,1420000000,1420500000,1421000000,1421500000])
#plot array data
ax.scatter(frequencyA,intensityA, marker=".", c="red")
plt.show()
