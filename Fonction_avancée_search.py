import csv

#debut "recherche de liens"
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
            return result
        else:
            print("Error: the specified file is incorrectly named, please verify it contains Machine_Interface")
#fin "recherche de liens"

#créer un dictionnaire pour le nom des machines
def dict_MachineName(path):
    with open(path , 'r') as file:
        if (path.__contains__("Machine_Name")):
            result = {}
            reader = csv.DictReader(file)
            for line in reader:
                result[line["Id_machine"]]=line["Machine_name"]
            return result
        else:
            print("Error: the specified file is incorrectly named, please verify it contains Machine_Name")
#créer un dictionnaire pour le nom des machines      
def dict_MachineType(path):
    with open(path, 'r') as file:
        if (path.__contains__("Machine_Type")):
            result = {}
            reader = csv.DictReader(file)
            for line in reader:
                result[line["Id_machine"]]=line["Machine_type"]
            return result
        else:
            print("Error: the specified file is incorrectly named, please verify it contains Machine_Type")  