import yagmail
import csv
import keyring

poster = f"WhatsApp link for Poster Making"
bingo = f"WhatsApp link for Virtual Bingo"
jali = f"WhatsApp link for Kavyanjali"
step = f"WhatsApp link for Step Up India"
solo = f"WhatsApp link for Solo Act"
contactus = " nssucoearchive@gmail.com"


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
            contents = ["Welcome to the Inter-College Mega Event on the occasion of 51st NSS Day,",
                        "brought to you by NSS UCoE!", "A number of competitions and fun events have been organised ",
                        "To celebrate the day in a amazing way.", "Show your incredible enthusiasm..!!",
                        "Mark the date, 24th September, 2020 (Thursday) - 9 am to 12 pm."]
            Pcontents = ["hiiiiiiiii"]
            if QnA == "Yes":
                Pcontents.append("WhatsApp link for QnA Event is \n  ")
            Pcontents.append(contactus)

            yag.send(POE, 'NSS DAY EVENTS DETAIL UCOE', Pcontents)

            if FS0 != "":
                contents0 = [f"Dear {FS0} {LS0} ", f"From {CN}", f"{CA}",
                             "Here are the links for the WhatsApp groups of the events you have signedup for",
                             "", creator(contents, E0), contactus]
                yag.send(FS0, 'NSS DAY EVENTS DETAIL FROM NSS UCOE', contents0)

            print(contents)

print("")
print("TASK SUCCESSFULLY COMPLETED")
