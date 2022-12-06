import csv

def add_row(path):
    #éventuellement check si fichier existant et si non en créer un avec les fieldnames attendus en fonction du path fournit
    with open (path, 'a') as file:
        obj = csv.writer(file)
        #test le chemin fournit pour vérifier de quel type est le fichier que l'on souhaite modifier
        if (path.__contains__("Machine_Name")):
            ID_machine = input("Please enter the ID_machine you wish to add")
            machine_name = input("Please enter the machine_name you wish to add")
            obj.writerow([ID_machine, machine_name])
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
            machine_type = input("Please enter the type of the machine you wish to add ")
            obj.writerow([ID_machine, machine_type])
        else:
            print("Error: the specified file is incorrectly named, verify it contains one of those: machine_name ; routing_table ; machine_address ; machine_interface ; machine_type")
            
def del_row (path, searchkey):
    with open (path, 'r') as original:
        to_test = csv.DictReader(original)