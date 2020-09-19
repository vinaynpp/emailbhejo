import yagmail
import csv
import keyring

poster = "WhatsApp link for Poster Making"
bingo = "WhatsApp link for Virtual Bingo"
jali = "WhatsApp link for Kavyanjali"
step = "WhatsApp link for Step Up India"
solo = "WhatsApp link for Solo Act"


def creator(content, events):
    if events != "":
        if events.count("Poster") != 0:
            content.append(poster)
        if events.count("Bingo") != 0:
            content.append(bingo)
        if events.count("Kavyanjali") != 0:
            content.append(jali)
        if events.count("Step") != 0:
            content.append(step)
        if events.count("Act") != 0:
            content.append(solo)
        print(content)
        return content




print("")
print("LET'S START")
print("")
# meraemail = str(input("OWN EMAIL \n"))
# merapswd = str(input("OWN PASSWORD \n"))
meraemail = ""
merapswd = ""

yagmail.register(meraemail, merapswd)

print("")
print("NOW MAIN TASK")
print("")

print("loggedin")

with yagmail.SMTP(meraemail) as yag:
    with open("nssheader.csv") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row

        for Ts, POE, POF, POL, POG, POC, CN, CA, S, QnA, N, FS0, LS0, ES0, CS0, E0, FS1, LS1, ES1, CS1, E1, FS2, LS2, ES2, CS2, E2, FS3, LS3, ES3, CS3, E3, FS4, LS4, ES4, CS4, E4, FS5, LS5, ES5, CS5, E5, FS6, LS6, ES6, CS6, E6, FS7, LS7, ES7, CS7, E7, FS8, LS8, ES8, CS8, E8, FS9, LS9, ES9, CS9, E9 in reader:
            contents = ["hiiiiiiiii"]

            contents = [creator(contents, E9)]
#           yag.send(POE, 'ORACLE ACCOUNT CREDENTIALS', contents)



            print(contents)

print("")
print("TASK SUCCESSFULLY COMPLETED")
