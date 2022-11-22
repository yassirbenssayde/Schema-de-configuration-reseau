import csv

with open("Machine_Address.csv", "r") as file :
    reader = csv.reader(file)
    
    for line in reader:
      print(line)
      

    


