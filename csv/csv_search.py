import csv

#tdebut "recherche de liens"
def find_Interface(path, looking_for):
    with open(path, 'r') as file:
        if (path.__contains__("Machine_Interface")):
            reader = csv.DictReader(file)
            result = []
            for line in reader:
                test1 = line["Interface1"]
                test2 = line["Interface2"]
                if (test1.__contains__(looking_for)):
                    result.append(test1)
                if (test2.__contains__(looking_for)):
                    result.append(test2)
            print(result)
            return result
        else:
            print("here should be an error n1")
#fin "recherche de liens"

#créer un dictionnaire pour le nom des machines
def dict_MachineName(path):
    with open(path , 'r') as file:
        if (path.__contains__("Machine_Name")):
            result = {}
            reader = csv.DictReader(file)
            for line in reader:
                result[line["Id_machine"]]=line["Machine_name"]
            print(result)
            return result
        else:
            print("here should be an error n2")
            
def dict_MachineType(path):
    with open(path, 'r') as file:
        if (path.__contains__("Machine_Type")):
            result = {}
            reader = csv.DictReader(file)
            for line in reader:
                result[line["Id_machine"]]=line["Machine_type"]
            print(result)
            return result
        else:
            print("here should be an error n3")
            
def dict_Node():
    machineName = dict_MachineName("characteristics/Machine_Name.csv")
    machineType = dict_MachineType("characteristics/Machine_Type.csv")
    i = 0
    j = 0    
            
dict_MachineName("characteristics/Machine_Name.csv")
dict_MachineType("characteristics/Machine_Type.csv")
find_Interface("characteristics/Machine_Interface.csv", "/0")
find_Interface("characteristics/Machine_Interface.csv", "/1")
find_Interface("characteristics/Machine_Interface.csv", "/2")
find_Interface("characteristics/Machine_Interface.csv", "/3")
find_Interface("characteristics/Machine_Interface.csv", "/4")
find_Interface("characteristics/Machine_Interface.csv", "/5")