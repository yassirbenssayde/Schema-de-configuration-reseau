import csv,os

#Ajout de ligne
def add_row(path, Id_machine):
    #éventuellement check si fichier existant et si non en créer un avec les fieldnames attendus en fonction du path fournit
    with open (path, 'a', newline='') as file:
        write = csv.writer(file)
        #test le chemin fournit pour vérifier de quel type est le fichier que l'on souhaite modifier
        if (path.__contains__("Machine_Name")):
            machine_name = input("Please enter the machine_name you wish to add: ")
            write.writerow([Id_machine, machine_name])
        elif (path.__contains__("Machine_Address")):
            address1 = input("Please enter the first address you wish to add: ")
            address2 = input("Please enter the second adress you wish to add: ")
            mask = input("Please enter the mask you wish to add: ")
            write.writerow([Id_machine, address1, address2, mask])
        elif (path.__contains__("Machine_Interface")):
            interface1 = f"Fa{Id_machine}/"+input("Please enter the first interface you wish to add: ")
            interface2 = input("Please enter the second interface you wish to add, if you have only one interface please write NULL: ")
            if interface2 != "NULL":
                interface2 = f"Fa{Id_machine}/"+interface2
            write.writerow([Id_machine, interface1, interface2])
        elif (path.__contains__("Machine_Type")):
            machine_type = str
            is_TypeOK = False
            while is_TypeOK != True:
                machine_type = input("Please enter the type of the machine you wish to add. It must be one of those: Router ; Switch ; Client : ")
                if (machine_type == "Router" or machine_type == "Switch" or machine_type == "Client"):
                    is_TypeOK = True
            write.writerow([Id_machine, machine_type])
        else:
            print("Error: the specified file is incorrectly named, please verify it contains one of those: Machine_Name ; Machine_Address ; Machine_Interface ; Machine_Type")
            
#Suppression de lignes
def del_row (path, searchkey):
    with open (path, 'r') as original, open ("tmp.csv", 'a', newline='') as copy:
        write = csv.writer(copy)
        for line in csv.reader(original):
            if (line[0] != str(searchkey)):
                write.writerow(line)
    os.replace("tmp.csv", path)
 
def del_machine (searchkey, folder =""):
    if folder != "":
        del_row(f"{folder}/Machine_Name.csv", searchkey)
        del_row(f"{folder}/Machine_Type.csv", searchkey)
        del_row(f"{folder}/Machine_Interface.csv", searchkey)
        del_row(f"{folder}/Machine_Address.csv", searchkey)
    else:
        del_row("Machine_Name.csv", searchkey)
        del_row("Machine_Type.csv", searchkey)
        del_row("Machine_Interface.csv", searchkey)
        del_row("Machine_Address.csv", searchkey)

#Modification de ligne
def mod_row (path, searchkey):
    with open (path, 'r') as original, open ("tmp.csv", 'a', newline='') as copy:
        write = csv.writer(copy)
        for line in csv.reader(original):
            if (line[0] != str(searchkey)):
                write.writerow(line)
            else:
                Id_machine = searchkey
                if (path.__contains__("Machine_Name")):
                    machine_name = input(f"Please enter the machine_name you wish to set for the machine n°{searchkey}: ")
                    write.writerow([Id_machine, machine_name])
                elif (path.__contains__("Machine_Address")):
                    address1 = input(f"Please enter the first address you wish to set for the machine n°{searchkey}: ")
                    address2 = input(f"Please enter the second adress you wish to set for the machine n°{searchkey}: ")
                    mask = input(f"Please enter the mask you wish to set for the machine n°{searchkey}: ")
                    write.writerow([Id_machine, address1, address2, mask])
                elif (path.__contains__("Machine_Interface")):
                    interface1 = f"Fa{Id_machine}/"+input(f"Please enter the first interface you wish to set for the machine n°{searchkey}: ")
                    interface2 = f"Fa{Id_machine}/"+input(f"Please enter the second interface you wish to set for the machine n°{searchkey}: ")
                    write.writerow([Id_machine, interface1, interface2])
                elif (path.__contains__("Machine_Type")):
                    Id_machine = input(f"Please enter the Id_machine you wish to set for the machine n°{searchkey}: ")
                    machine_type = str
                    is_TypeOK = False
                    while is_TypeOK != True:
                        machine_type = input(f"Please enter the type of the machine you wish to set for the machine n°{searchkey}. It must be one of those: Router ; Switch ; Client")
                        if (machine_type == "Router" or machine_type == "Switch" or machine_type == "Client"):
                            is_TypeOK = True
                    write.writerow([Id_machine, machine_type])
                else:
                    print("Error: the specified file is incorrectly named, please verify it contains one of those: Machine_Name ; Machine_Address ; Machine_Interface ; Machine_Type")
    os.replace("tmp.csv", path)
                    
def mod_machine (searchkey, folder =""):
    if folder != "":
        mod_row(f"{folder}/Machine_Name.csv", searchkey)
        mod_row(f"{folder}/Machine_Type.csv", searchkey)
        mod_row(f"{folder}/Machine_Interface.csv", searchkey)
        mod_row(f"{folder}/Machine_Address.csv", searchkey)
    else:
        mod_row("Machine_Name.csv", searchkey)
        mod_row("Machine_Type.csv", searchkey)
        mod_row("Machine_Interface.csv", searchkey)
        mod_row("Machine_Address.csv", searchkey)

#Initialise le premier identifiant libre
def next_id(folder =""):
    result = 1
    if folder != "":
        path = f"{folder}/Machine_Name.csv"
    else:
        path = "Machine_Name.csv"
    with open (path, 'r') as file:
        for line in csv.DictReader(file):
            line_value = int(line["Id_machine"])
            if line_value == result+1:
                result = line_value
        return result+1

#Crée une nouvelle machine
def add_machine(folder =""):
    id = next_id(folder)
    if folder != "":
        add_row(f"{folder}/Machine_Name.csv", id)
        add_row(f"{folder}/Machine_Type.csv", id)
        add_row(f"{folder}/Machine_Interface.csv", id)
        add_row(f"{folder}/Machine_Address.csv", id)
    else:
        add_row("Machine_Name.csv", id)
        add_row("Machine_Type.csv", id)
        add_row("Machine_Interface.csv", id)
        add_row("Machine_Address.csv", id)

#Sert pour les tests
def main():
    add_machine("csv")
    
main()