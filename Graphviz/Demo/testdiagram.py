#Utilisation de diagrams on utilise Graphviz pour rendre le diagramme.
#Puis on installe diagrams


#Cette ligne importera les morceaux de diagramme nécessaires pour créer les éléments de diagramme génériques. 
from diagrams import Cluster, Edge, Diagram

#Ajoutez les lignes suivantes pour importer les icônes Droplet, DbaasPrimary et Logstash : 

#Image Switch
from diagrams.aws.management import OpsworksDeployments
#Image Routeur
from diagrams.aws.network    import VPCCustomerGateway
#Image Machine
from diagrams.onprem.client  import Client



#La show peut l'ouvrir lors de la création, mais il a été défini sur False puisque nous travaillons sur un hôte Linux. 
# Le fichier généré sera nommé quelle que soit la chaîne assignée à filename. 
# La direction est la direction dans laquelle nous voulons que le diagramme soit imprimé. 
# Les valeurs prises en charge pour directionsommes TB(Haut -> Bas) et LR(Gauche -> Droite). 
# Sélection du direction peut faciliter la lecture du schéma. Pour ce diagramme, nous utiliserons LR.
with Diagram("Schema du reseau", show=False):
    #ajoutez les icônes au diagramme : 
    with Cluster ("Reseau"):
        with Cluster("Reseau Internet1"):
            Routeur1 = VPCCustomerGateway("Router1")
            switch1  = OpsworksDeployments("Switch1")
            Machine1 = Client("Machine1")
        
        with Cluster("Reseau Interne2"):
            Routeur2 = VPCCustomerGateway("Router2")
            switch2  = OpsworksDeployments("Switch2")
            Machine2 = Client("Machine2")
        
    
    
    #La création des dépendances entre les différents éléments du diagramme
    Machine1 >> switch1 >> Routeur1
    Machine2 >> switch2 >> Routeur2
    Machine2 >> Edge(color="firebrick", style="dashed") >> Routeur2  
    Machine1 >> Edge(color="firebrick", style="dashed") >> Routeur1
    Routeur2 >> Routeur1
    Routeur2 << Routeur1
    




