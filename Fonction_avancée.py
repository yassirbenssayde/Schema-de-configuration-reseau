import csv,os, schema_evolue_avec_methode

#Ajout de ligne

def add_row(path, Id_machine, folder=""):
    path = f"{folder}{path}"
    with open (path, 'r', newline='') as original, open("tmp.csv", 'a', newline='') as copy:
        write = csv.writer(copy)
        for line in csv.reader(original):
            if (line[0] == str(Id_machine-1)):
                write.writerow(line)

                #test le chemin fournit pour vérifier de quel type est le fichier que l'on souhaite modifier

                if (path.__contains__("Machine_Name")):
                    machine_name = input(f"Please enter the machine_name you wish to add for the machine n°{Id_machine}: ")
                    write.writerow([Id_machine, machine_name])
                elif (path.__contains__("Machine_Address")):
                    if check_type(f"{folder}Machine_Type.csv", Id_machine) == "Switch":
                        address1 = ""
                        address2 = ""
                        mask = ""
                    else:
                        address1 = input(f"Please enter the first address you wish to add. Attention: this address will define which cluster the machine n°{Id_machine} is part of: ")
                        print(is_Interface2(f"{folder}Machine_Interface.csv", Id_machine))
                        if is_Interface2(f"{folder}Machine_Interface.csv", Id_machine):
                            address2 = input(f"Please enter the second adress you wish to add for the machine n°{Id_machine}: ")
                        else:
                            address2 = ""
                        mask = input(f"Please enter the mask you wish to add for the machine n°{Id_machine}: ")
                    write.writerow([Id_machine, address1, address2, mask])
                elif (path.__contains__("Machine_Interface")):
                    interface1 = f"Fa{Id_machine}/"+input(f"Please enter the first interface you wish to add for the machine n°{Id_machine}: ")
                    interface2 = input(f"Please enter the second interface you wish to add for the machine n°{Id_machine}, if you have only one interface please leave it blank: ")
                    if interface2 != "":
                        interface2 = f"Fa{Id_machine}/"+interface2
                    write.writerow([Id_machine, interface1, interface2])
                elif (path.__contains__("Machine_Type")):
                    machine_type = str
                    is_TypeOK = False
                    while is_TypeOK != True:
                        machine_type = input(f"Please enter the type of the machine n°{Id_machine} you wish to add. It must be one of those: Router ; Switch ; Machine : ")
                        if (machine_type == "Router" or machine_type == "Switch" or machine_type == "Machine"):
                            is_TypeOK = True
                    write.writerow([Id_machine, machine_type])
                else:
                    print("Error: the specified file is incorrectly named, please verify it contains one of those: Machine_Name ; Machine_Address ; Machine_Interface ; Machine_Type")
            else:
                write.writerow(line)
    os.replace("tmp.csv", path)
            
#Suppression de lignes

def del_row (path, searchkey):
    with open (path, 'r') as original, open ("tmp.csv", 'a', newline='') as copy:
        write = csv.writer(copy)
        for line in csv.reader(original):
            if (line[0] != str(searchkey)):
                write.writerow(line)
    os.replace("tmp.csv", path)
 
def del_machine (searchkey, folder =""):
    del_row(f"{folder}Machine_Name.csv", searchkey)
    del_row(f"{folder}Machine_Type.csv", searchkey)
    del_row(f"{folder}Machine_Interface.csv", searchkey)
    del_row(f"{folder}Machine_Address.csv", searchkey)
    schema_evolue_avec_methode.gen_imgcluster()

#Modification de ligne

def mod_row (path, searchkey, folder=""):
    path = f"{folder}{path}"
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
                    if check_type(f"{folder}Machine_Type.csv", searchkey) == "Switch":
                        address1 = ""
                        address2 = ""
                        mask = ""
                    else:
                        address1 = input(f"Please enter the first address you wish to set for the machine n°{searchkey}. Attention: this address will define which cluster the machine is part of: ")
                        if is_Interface2(f"{folder}Machine_Interface", searchkey):
                            address2 = input(f"Please enter the second adress you wish to set for the machine n°{searchkey}: ")
                        else:
                            address2= ""
                        mask = input(f"Please enter the mask you wish to set for the machine n°{searchkey}: ")
                    write.writerow([Id_machine, address1, address2, mask])
                elif (path.__contains__("Machine_Interface")):
                    interface1 = f"Fa{Id_machine}/"+input(f"Please enter the first interface you wish to set for the machine n°{searchkey}: ")
                    interface2 = input(f"Please enter the second interface you wish to set for the machine n°{searchkey}, if you have only one interface please leave it blank: ")
                    if interface2 != "":
                        interface2 = f"Fa{Id_machine}/"+interface2
                    write.writerow([Id_machine, interface1, interface2])
                elif (path.__contains__("Machine_Type")):
                    Id_machine = input(f"Please enter the Id_machine you wish to set for the machine n°{searchkey}: ")
                    machine_type = str
                    is_TypeOK = False
                    while is_TypeOK != True:
                        machine_type = input(f"Please enter the type of the machine you wish to set for the machine n°{searchkey}. It must be one of those: Router ; Switch ; Machine : ")
                        if (machine_type == "Router" or machine_type == "Switch" or machine_type == "Machine"):
                            is_TypeOK = True
                    write.writerow([Id_machine, machine_type])
                else:
                    print("Error: the specified file is incorrectly named, please verify it contains one of those: Machine_Name ; Machine_Address ; Machine_Interface ; Machine_Type")
    os.replace("tmp.csv", path)
                    
def mod_machine (searchkey, folder =""):
    mod_row("Machine_Name.csv", searchkey, folder)
    mod_row("Machine_Type.csv", searchkey, folder)
    mod_row("Machine_Interface.csv", searchkey, folder)
    mod_row("Machine_Address.csv", searchkey, folder)
    schema_evolue_avec_methode.gen_imgcluster()

#Initialise le premier identifiant libre

def next_id(folder =""):
    result = 1
    if folder != "":
        path = f"{folder}Machine_Name.csv"
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
    add_row("Machine_Name.csv", id, folder)
    add_row("Machine_Type.csv", id, folder)
    add_row("Machine_Interface.csv", id, folder)
    add_row("Machine_Address.csv", id, folder)
    schema_evolue_avec_methode.gen_imgcluster()
    
#vérifie le type de la machine

def check_type(path, id):
    with open(path, 'r') as file:
        if (path.__contains__("Machine_Type")):
            for line in csv.DictReader(file):
                if (int(line["Id_machine"]) == id):
                    return line["Machine_type"]
            print("Specified id doesn't exist")
        else:
            print("Error: the specified file is incorrectly named, please verify it contains Machine_Type")
            
def is_Interface2(path, id):
    with open(path, 'r') as file:
        if (path.__contains__("Machine_Interface")):
            for line in csv.DictReader(file):
                if (int(line["Id_machine"]) == id):
                    if line["Interface2"] != "":
                        return True
                    else:
                        return False
            print("Specified id doesn't exist")
        else:
            print("Error: the specified file is incorrectly named, please verify it contains Machine_Interface")

#Sert pour les tests


def main():
    add_machine()
    del_machine(8)

main()