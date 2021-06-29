#fit.py (core script)
#fits data from a .kel file with a function made up of 1-3 gaussian functions
#can fit either frequency or velocity
#note that the variable name "frequency" is used in the program
#David Schultz, June 28, 2021

import collections        #needed for deque, remove, & rotate
import read_datafilename  #reads name of .kel file
import read_datafile      #reads contents of a single .kel file
import read_parameters    #reads fit_parameters.txt
import modify_parameters  #modifies parameter list
import minimize           #fits center, coefficient & sigma vals
import plot               #plots data and final fit

#READ NAME AND TYPE OF .KEL FILE*****************************************
A=read_datafilename.get_datafilename()
print("\n")
datafilename=A[0]; print("Data file",datafilename)
coordinate=A[1]; print("Coordinate",coordinate)
newfilename=datafilename[0:15]+".dat"  #rename .kel to .dat

with open(newfilename, 'w') as g:
    g.write(A[0]);g.write("\n")
    g.write(coordinate);g.write("\n")

    #GET PARAMETERS
    parameter=read_parameters.get_params()
    print("Initial parameters: center, coefficient, sigma");print(parameter)
    g.write("Initial parameters: center, coefficient, sigma");g.write("\n")
    g.write("Peak A "+str(parameter[0:3]));g.write("\n")
    g.write("Peak B "+str(parameter[3:6]));g.write("\n")
    g.write("Peak C "+str(parameter[6:9]));g.write("\n")

    #GET FLAGS
    flag=read_parameters.get_flags()
    centerflagA=flag[0];coefflagA=flag[1];sigmaflagA=flag[2]
    centerflagB=flag[3];coefflagB=flag[4];sigmaflagB=flag[5]
    centerflagC=flag[6];coefflagC=flag[7];sigmaflagC=flag[8]
    print("Flags: Peak A (x3), Peak B (x3), Peak C (x3)");print(flag)
    g.write("Flags: Peak A (x3), Peak B (x3), Peak C (x3)");g.write("\n")
    g.write("Flag A "+str(flag[0:3]));g.write("\n")
    g.write("Flag B "+str(flag[3:6]));g.write("\n")
    g.write("Flag C "+str(flag[6:9]));g.write("\n")

    #GET STUFF
    stuff=read_parameters.get_stuff()
    total_iterations=stuff[0];startline=stuff[1];endline=stuff[2]
    print("Iterations, startline, endline");print(stuff)
    g.write("Iterations, startline, endline");g.write("\n")
    g.write(str(stuff));g.write("\n")

    #GET STEPS AND MAX_PASSES
    steplist=read_parameters.get_step()
    print("Stepsize & Maximum Passes: Center (x2), Coefficient (x2), Sigma (x2)")
    print(steplist)
    g.write("Stepsize & Maximum Passes: Center (x2), Coefficient (x2), Sigma (x2)");g.write("\n")
    g.write(str(steplist));g.write("\n")

    #READ EXPERIMENTAL DATA
    frequency=read_datafile.frequency(startline,endline)
    intensity=read_datafile.intensity(startline,endline)

    #GENERATE PARAMETER FILES WITH ROTATED PEAKS FOR FITTING
    parameterA=modify_parameters.fitA(parameter)
    parameterAB=modify_parameters.fitAB(parameter)
    parameterABC=modify_parameters.fitABC(parameter)

    #EXECUTE ITERATIONS***********************************************
    print("Differences")
    g.write("Differences");g.write("\n")
    Z=[99999]
    sumterms=0
    for iterations in range(total_iterations):
        for i in range(3):
            #Fit center***********************************************
            if i==0 and centerflagA==1: #fit peak A 
                centerA=minimize.center(frequency,intensity,parameterA,startline,endline,steplist)
                parameter[0]=centerA[0]
                sumterms=centerA[1]  
            if i==1 and centerflagB==1: #fit peak B
                centerB=minimize.center(frequency,intensity,parameterAB,startline,endline,steplist)
                parameter[3]=centerB[0]
                sumterms=centerB[1]
            if i==2 and centerflagC==1: #fit peak C
                centerC=minimize.center(frequency,intensity,parameterABC,startline,endline,steplist) 
                parameter[6]=centerC[0]
                sumterms=centerC[1]
            parameterA=modify_parameters.fitA(parameter)
            parameterAB=modify_parameters.fitAB(parameter) 
            parameterABC=modify_parameters.fitABC(parameter)

            #Fit coefficient******************************************
            if i==0 and coefflagA==1:
                coefA=minimize.coef(frequency,intensity,parameterA,startline,endline,steplist)
                parameter[1]=coefA[0]
                sumterms=coefA[1]
            if i==1 and coefflagB==1:
                coefB=minimize.coef(frequency,intensity,parameterAB,startline,endline,steplist)
                parameter[4]=coefB[0]
                sumterms=coefB[1]
            if i==2 and coefflagC==1:
                coefC=minimize.coef(frequency,intensity,parameterABC,startline,endline,steplist) 
                parameter[7]=coefC[0]
                sumterms=coefC[1]
            parameterA=modify_parameters.fitA(parameter)
            parameterAB=modify_parameters.fitAB(parameter)
            parameterABC=modify_parameters.fitABC(parameter)

            #Fit sigma************************************************            
            if i==0 and sigmaflagA==1:
                sigmaA=minimize.sigma(frequency,intensity,parameterA,startline,endline,steplist)
                parameter[2]=sigmaA[0]
                sumterms=sigmaA[1]
            if i==1 and sigmaflagB==1:
                sigmaB=minimize.sigma(frequency,intensity,parameterAB,startline,endline,steplist)
                parameter[5]=sigmaB[0]
                sumterms=sigmaB[1]
            if i==2 and sigmaflagC==1:
                sigmaC=minimize.sigma(frequency,intensity,parameterABC,startline,endline,steplist) 
                parameter[8]=sigmaC[0]
                sumterms=sigmaC[1]      
            parameterA=modify_parameters.fitA(parameter)
            parameterAB=modify_parameters.fitAB(parameter)
            parameterABC=modify_parameters.fitABC(parameter)

        Z.append(sumterms)
        if Z[iterations+1]<Z[iterations]:
            print(Z)
            g.write(str(Z));g.write("\n")  
        else:
            break
    print("***************ALL DONE*******************")
    print("Final parameters")
    print(parameter)
    print("\n")
    g.write("Final parameters");g.write("\n")
    g.write("Peak A "+str(parameter[0:3]));g.write("\n")
    g.write("Peak B "+str(parameter[3:6]));g.write("\n")
    g.write("Peak C "+str(parameter[6:9]));g.write("\n")    
g.closed
True

plot.do_it(frequency,intensity,parameter,startline,endline,coordinate)
exit()
