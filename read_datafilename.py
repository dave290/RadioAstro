#read_datafilename.py

def get_datafilename():
    file=["parameters.txt"]
    for workingfile in file:
        with open(workingfile,'r') as f:
            for line in f:
                linestring=line.split()
                if linestring[0]=="File":  
                    filename=linestring[1]
                if linestring[0]=="Coordinate":
                    coordinate=linestring[1]
        f.closed
        True
    return filename,coordinate