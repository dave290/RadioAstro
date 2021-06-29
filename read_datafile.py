#read_file.py

import numpy
import collections
import read_parameters
import read_datafilename

#get the name of the .kel file
A=read_datafilename.get_datafilename()
datafile=A[0]
file=[str(A[0])]

def frequency(startline,endline):
    freq_list=[0]         #defines array used to store frequencies
    for workingfile in file:
        with open(workingfile, 'r') as f:    
            line_no=0
            for line in f:
                line_no=line_no+1
                if line_no>=startline and line_no<=endline:
                    linestring=line.split()      
                    freq=float(linestring[1])
                    freq_list.append(freq)
        f.closed
        True
    dequed_freq_list=collections.deque(freq_list)
    dequed_freq_list.remove(0)
    frequency=list(dequed_freq_list)
    return frequency

def intensity(startline,endline):
    int_list=[0]          #defines array used to store experimental intensities
    for workingfile in file:
        with open(workingfile, 'r') as f:    
            line_no=0
            for line in f:
                line_no=line_no+1
                if line_no>=startline and line_no<=endline:
                    linestring=line.split()      
                    int=float(linestring[2])
                    int_list.append(int)
        f.closed
        True
    dequed_int_list=collections.deque(int_list)
    dequed_int_list.remove(0)
    intensity=list(dequed_int_list)
    return intensity

