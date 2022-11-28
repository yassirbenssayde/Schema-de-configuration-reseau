import csv

def add_row(path):
    #éventuellement check si fichier existant et si non en créer un avec les fieldnames attendus en fonction du path fournit
    with open (path, 'a') as file:
        obj = csv.writer(file)
        #test le chemin fournit pour vérifier de quel type est le fichier que l'on souhaite modifier
        try:
            if (path.__contains__("Machine_Name")):
                ID_machine = input("Please enter the ID_machine you wish to add")
                machine_name = input("Please enter the machine_name you wish to add")
                obj.writerow([ID_machine, machine_name])
            elif (path.__contains__("Routing_Table")):
                ID_machine = input("Please enter the ID_machine you wish to add")
                network_address = input("Please enter the network_address you wish to add")
                mask = input("Please enter the mask you wish to add")
                interfaces = input("Please enter the interfaces you wish to add")
                obj.writerow([ID_machine, network_address, mask, interfaces])
            elif (path.__contains__("Machine_Address")):
                ID_machine = input("Please enter the ID_machine you wish to add")
                address1 = input("Please enter the first address you wish to add")
                address2 = input("Please enter the second adress you wish to add")
                mask = input("Please enter the mask you wish to add")
                obj.writerow([ID_machine, address1, address2, mask])
            elif (path.__contains__("Machine_Interface")):
                ID_machine = input("Please enter the ID_machine you wish to add")
                interface1 = input("Please enter the first interface you wish to add")
                interface2 = input("Please enter the second interface you wish to add")
                obj.writerow([ID_machine, interface1, interface2])
            elif (path.__contains__("Machine_Type")):
                ID_machine = input("Please enter the ID_machine you wish to add")
                machine_type = input("Please enter the type of the machine you wish to add")
                obj.writerow([ID_machine, machine_type])
        except:
            print("Error: the specified file is incorrectly named, verify it contains one of those: machine_name ; routing_table ; machine_address ; machine_interface ; machine_type")
    
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
            print("here should be an error")
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
            
dict_MachineName("Machine_Name.csv")
find_Interface("Machine_Interface.csv", "/0")
find_Interface("Machine_Interface.csv", "/1")
find_Interface("Machine_Interface.csv", "/2")
find_Interface("Machine_Interface.csv", "/3")
find_Interface("Machine_Interface.csv", "/4")
find_Interface("Machine_Interface.csv", "/5")