import csv

print("")
print("NOW MAIN TASK")
print("")

print("loggedin")
with open("nssheader.csv") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row

    for Ts, POE, POF, POL, POG, POC, CN, CA, S, QnA, N, FS0, LS0, ES0, CS0, E0, FS1, LS1, ES1, CS1, E1, FS2, LS2, ES2, CS2, E2, FS3, LS3, ES3, CS3, E3, FS4, LS4, ES4, CS4, E4, FS5, LS5, ES5, CS5, E5, FS6, LS6, ES6, CS6, E6, FS7, LS7, ES7, CS7, E7, FS8, LS8, ES8, CS8, E8, FS9, LS9, ES9, CS9, E9 in reader:
        def creator(FS, LS, ES, CS, CN, events):
            if events != "":
                if events.count("Poster") != 0:
                    with open('nsslist/Poster.csv', 'a') as csvfile:
                        filewriter = csv.writer(csvfile, delimiter=',', lineterminator='\n')
                        filewriter.writerow([FS, LS, ES, CS, CN])
                if events.count("Bingo") != 0:
                    with open('nsslist/Bingo.csv', 'a') as csvfile:
                        filewriter = csv.writer(csvfile, delimiter=',', lineterminator='\n')
                        filewriter.writerow([FS, LS, ES, CS, CN])
                if events.count("Kavyanjali") != 0:
                    with open('nsslist/Kavyanjali.csv', 'a') as csvfile:
                        filewriter = csv.writer(csvfile, delimiter=',', lineterminator='\n')
                        filewriter.writerow([FS, LS, ES, CS, CN])
                if events.count("Step") != 0:
                    with open('nsslist/Step.csv', 'a') as csvfile:
                        filewriter = csv.writer(csvfile, delimiter=',', lineterminator='\n')
                        filewriter.writerow([FS, LS, ES, CS, CN])
                if events.count("Act") != 0:
                    with open('nsslist/Act.csv', 'a') as csvfile:
                        filewriter = csv.writer(csvfile, delimiter=',', lineterminator='\n')
                        filewriter.writerow([FS, LS, ES, CS, CN])


        if FS0 != "":
            creator(FS0, LS0, ES0, CS0, CN, E0)
        if FS1 != "":
            creator(FS1, LS1, ES1, CS1, CN, E1)
        if FS2 != "":
            creator(FS2, LS2, ES2, CS2, CN, E2)
        if FS3 != "":
            creator(FS3, LS3, ES3, CS3, CN, E3)
        if FS4 != "":
            creator(FS4, LS4, ES4, CS4, CN, E4)
        if FS5 != "":
            creator(FS5, LS5, ES5, CS5, CN, E5)
        if FS6 != "":
            creator(FS6, LS6, ES6, CS6, CN, E6)
        if FS7 != "":
            creator(FS7, LS7, ES7, CS7, CN, E7)
        if FS8 != "":
            creator(FS8, LS8, ES8, CS8, CN, E8)
        if FS9 != "":
            creator(FS9, LS9, ES9, CS9, CN, E9)
        if POF != "":
            with open('nsslist/PO.csv', 'a') as csvfile:
                filewriter = csv.writer(csvfile, delimiter=',', lineterminator='\n')
                filewriter.writerow([POF, POL, POG, QnA, POE, POC, CN, CA, S])

print("")
print("TASK SUCCESSFULLY COMPLETED")
