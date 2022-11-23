import csv

def add_row(path):
    #éventuellement check si fichier existant et si non en créer un avec les fieldnames attendus en fonction du path fournit
    with open (path, 'a') as file:
        obj = csv.writer(file, dialect='excel')
        #test le chemin fournit pour vérifier de quel type est le fichier que l'on souhaite modifier
        try:
            if (path.contains("machine_name")):
                ID_machine = input("Please enter the ID_machine you wish to add")
                machine_name = input("Please enter the machine_name you wish to add")
                obj.writerow([ID_machine, machine_name])
            elif (path.contains("routing_table")):
                ID_machine = input("Please enter the ID_machine you wish to add")
                network_address = input("Please enter the network_address you wish to add")
                mask = input("Please enter the mask you wish to add")
                interfaces = input("Please enter the interfaces you wish to add")
                obj.writerow([ID_machine, network_address, mask, interfaces])
            elif (path.contains("machine_address")):
                ID_machine = input("Please enter the ID_machine you wish to add")
                address1 = input("Please enter the first address you wish to add")
                address2 = input("Please enter the second adress you wish to add")
                mask = input("Please enter the mask you wish to add")
                obj.writerow([ID_machine, address1, address2, mask])
            elif (path.contains("machine_interface")):
                ID_machine = input("Please enter the ID_machine you wish to add")
                interface1 = input("Please enter the first interface you wish to add")
                interface2 = input("Please enter the second interface you wish to add")
                obj.writerow([ID_machine, interface1, interface2])
            elif (path.contains("machine_type")):
                ID_machine = input("Please enter the ID_machine you wish to add")
                machine_type = input("Please enter the type of the machine you wish to add")
                obj.writerow([ID_machine, machine_type])
        except:
            print("Error: the specified file is incorrectly named, verify it contains one of those: machine_name ; routing_table ; machine_address ; machine_interface ; machine_type")
    file.close()
    
#test de lecture
with open("Machine_Address.csv", "r") as file :
    reader = csv.reader(file)
    
    for line in reader:
      print(line)