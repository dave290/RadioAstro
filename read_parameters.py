#read_parameters.py

import read_datafilename
import collections

def get_params():
    file=["parameters.txt"]
    parameter_list=[0]
    for workingfile in file:
        with open(workingfile,'r') as f:
            for line in f:
                linestring=line.split()
                if linestring[0]=="P":     
                    parameter=float(linestring[2])
                    parameter_list.append(parameter)
        f.closed
        True
    parameter_list_dequed=collections.deque(parameter_list)
    parameter_list_dequed.remove(0)
    parameter=list(parameter_list_dequed)
    return parameter

def get_flags():
    file=["parameters.txt"]
    flag=[0]
    for workingfile in file:
        with open(workingfile,'r') as f:
            for line in f:
                linestring=line.split()
                if linestring[0] == "F":      
                    flagtemp1=int(linestring[1])
                    flagtemp2=int(linestring[2])
                    flagtemp3=int(linestring[3])
                    flag.append(flagtemp1)
                    flag.append(flagtemp2)
                    flag.append(flagtemp3)
        f.closed
        True
    flag_dequed=collections.deque(flag)
    flag_dequed.remove(0)
    flag=list(flag_dequed)
    return flag

def get_step():
    file=["parameters.txt"]
    step=[0]
    for workingfile in file:
        with open(workingfile,'r') as f:
            for line in f:
                linestring=line.split()
                if linestring[0] == "S":      
                    steptemp1=float(linestring[2])
                    steptemp2=int(linestring[3])
                    step.append(steptemp1)
                    step.append(steptemp2)
        f.closed
        True
    step_dequed=collections.deque(step)
    step_dequed.remove(0)
    step=list(step_dequed)
    return step

def get_stuff():
    #get iterations, lower and upper fit thresholds
    file=["parameters.txt"]
    for workingfile in file:
        with open(workingfile,'r') as f:
            for line in f:
                linestring=line.split()
                if linestring[0] == "Iterations":      
                    iterations=int(linestring[1])
                if linestring[0] == "Lowerfitthreshold":      
                    lowerfitthreshold=float(linestring[1])
                if linestring[0] == "Upperfitthreshold":
                    upperfitthreshold=float(linestring[1])             
        f.closed
        True

    #determine starting and ending line numbers from data file
    A=read_datafilename.get_datafilename()
    datafile=[str(A[0])]
    for workingfile in datafile:
        with open(workingfile, 'r') as f:    
            linesofdata=[0]
            line_no=0
            for line in f:
                line_no=line_no+1
                linestring=line.split()
                if linestring[0]=="#":
                    pass
                else:
                    frequency=float(linestring[1])
                    if frequency>=lowerfitthreshold and frequency<=upperfitthreshold:
                        linesofdata.append(line_no)
        f.closed
        True
    startline=int(linesofdata[1])
    endline=int(linesofdata[-1])
    stuff=[iterations,startline,endline]
    return stuff
