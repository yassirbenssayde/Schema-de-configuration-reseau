from diagrams import Cluster, Edge, Diagram
from diagrams.aws.network import VPCRouter  #Image Routeur
from diagrams.onprem.client import Client   #Image Machine
from diagrams.aws.management import OpsworksDeployments #Image Switch
import csv 
from io import StringIO



List_of_Interface = [];
List_of_Name = [];
List_of_type = []
List_of_addresse = []
List_of_complet = []

#lier au find_Interface
result = []
interutil = []
interutil1 = []

#------------------------OUVERTURE DES CSV----------------------

#Dictionnaire du Machine_Interface
with open ('CSV/Machine_Interface.csv','r')as MI:
    Interface = csv.DictReader(MI)
    for row in Interface :
        List_of_Interface.append(row)
List_of_Inter = List_of_Interface.copy()
    
#Dictionnaire du Machine_Name
with open ('CSV/Machine_Name.csv','r')as MI:
    Name = csv.DictReader(MI)
    for row in Name :
        List_of_Name.append(row)

#Dictionnaire du types
with open ('CSV/Machine_Types.csv','r')as MT:
    Type = csv.DictReader(MT)
    for row in Type :
        List_of_type.append(row)

#Dictionnaire du types
with open ('CSV/Machine_Adresse.csv','r')as MA:
    Addresse = csv.DictReader(MA)
    for row in Addresse :
        List_of_addresse.append(row)

#--------------AJOUT DE TOUT LES DONNES DANS UN DICTIONNAIRE--------

#Ajout de l'interface
List_of_complet = List_of_Interface.copy()

#ajout du name
for row in List_of_complet:
    for row1 in List_of_Name:
        if row['Id_Machine'] == row1['Id_Machine']:
            row['Name'] = row1['Machine_Name']
        else:
            continue

#ajout du type
for row in List_of_complet:
    for row1 in List_of_type:
        if row['Id_Machine'] == row1['Id_Machine']:
            row['Type'] = row1['Machine_Type']
        else:
            continue

#ajout des addresses et masque
for row in List_of_complet:
    for row1 in List_of_addresse:
        if row['Id_Machine'] == row1['Id_Machine']:
            row['adresse1'] = row1['Adress1']
            row['adresse2'] = row1['Adress2']
            row['Masque'] = row1['Masque']
        else:
            continue

#-------------------------RECUPERATION DES INTERFACES DES MACHINES---------------------------

#tdebut "recherche de liens"
def find_Interface(path, looking_for):
    with open(path, 'r') as file:
        if (path.__contains__("CSV/Machine_Interface")):
            reader = csv.DictReader(file)
            
            for line in reader:
                test1 = line["Interface1"]
                test2 = line["Interface2"]
                if (test1.__contains__(looking_for)):
                    result.append(test1)
                if (test2.__contains__(looking_for)):
                    result.append(test2)
            
            return result
        else:
            print("here should be an error")
#fin "recherche de liens"

def find_Interface2(path, looking_for):
    with open(path, 'r') as file:
        if (path.__contains__("CSV/Machine_Interface")):
            reader = csv.DictReader(file)
            for line in reader:
                test2 = line["Interface2"]
                if (test2.__contains__(looking_for)):
                    result.append(test2)
            return result
        else:
            print("here should be an error")
#fin "recherche de liens"

#-------------------------GENERATION DE L'IMAGE BASIC------------------------

with Diagram("Schema du reseau", show=False, filename="Image/Image_basic", direction="BT"):

#-----------------------Partie Node----------------------------
        
        #A chaque Type on lui attribue une image specifice  
        for row in List_of_complet:
            if row['Type'] == 'Routeur':
                row['Image'] = VPCRouter(str(row['Name']))
            elif row['Type'] == 'Switch':
                row['Image'] = OpsworksDeployments(str(row['Name']))
            elif row ['Type'] == 'Machine':
                row['Image'] = Client(str(row['Name']))
            else :
                print('Error Type')
#--------------------Partie Edge (Lien)------------------------
    
        #On doit utiliser la même variable que le nom
        
        
        for row in List_of_complet:
            
            interutil.append(row['Interface1'])
            
            #print("Ligne sur laquelle on test")
            #print(row)
            
            search = row['Interface1']
            search = search[3:]
            #print(search)
            
            find_Interface("CSV/Machine_Interface.csv",search)
            result.remove(str(row['Interface1']))
            #print("Interface connecter")
            #print(result)
            
            
            for elem in result:
                if elem in interutil:
                    continue
                else :
                    for row1 in List_of_complet:
                        if elem == row1['Interface1']:
                            row['Image'] - row1['Image']
                        elif elem == row1['Interface2']:
                            row['Image'] - row1['Image']
            result = []
            #print("Inrerutils")
            
        interutil = []
        for row in List_of_complet:
            #print("Ligne sur laquelle on test")
            #print(row)
            if row['Interface2'] == "":
                continue
            else:
                interutil.append(row['Interface2'])
                search = row['Interface2']
                search = search[3:]
                #print(search)
                find_Interface2("CSV/Machine_Interface.csv",search)
                result.remove(str(row['Interface2']))
                #print(result)
                
                for elem in result:
                    if elem in interutil:
                        continue
                    else :
                        #print(elem)
                        for row1 in List_of_complet:
                            if elem == row1['Interface2']:
                                row['Image'] - row1['Image']
                result = []
                #print(result)
            