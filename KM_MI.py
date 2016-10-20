

print ("Pozdravljeni sem program za pretvarjanje kilometrov v milje")
while True:
    kilometri = int (raw_input ("vnesi kilometre"))
    print  ("to znese " + str(kilometri * 1.6) + " milj")
    odgovor = raw_input ("ali zelite se pretvarjati kilometre da/ne")
    if odgovor == "ne":
        print ("Hvala lepa in nasvidenje")   
        break
    
