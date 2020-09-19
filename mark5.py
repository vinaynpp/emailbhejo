import yagmail
import csv
import keyring

welcome = ["Thank you for registering for Inter College Event.",
           " We are looking forward to see on 24th September 2020 and celebrate the 51st NSS Day together.",
           "Event details:", "Date: 24th September 2020", "Time: 9AM-12PM", "Where: Google Meet"]

poster = f"WhatsApp link for Poster Making \n https://chat.whatsapp.com/CQp6wDm5j811ehkFYJAS89"
bingo = f"WhatsApp link for Virtual Bingo \n https://chat.whatsapp.com/K7OCpFuieAyEAa3uYve67G"
jali = f"WhatsApp link for Kavyanjali \n https://chat.whatsapp.com/GBqtw9POTMYGhfMBBL01nO"
step = f"WhatsApp link for Step Up India \n https://chat.whatsapp.com/GyWkv4qGhOg8Cp2UZSx9pw"
solo = f"WhatsApp link for Solo Act \n https://chat.whatsapp.com/IzrxSEICQDTGlQoxSZ0XR7"
contactus = ["Note: For joining the session with mobile, you need to install the Google meet app.",
             "If you have any doubts, please do not hesitate to contact us.",
             "Contact: Praneeth Hegde -( +91 84250 26490 )", "Wish you all the best!", "Regards,", "NSS UCoE."]


def creator(content, events):
    if events != "":
        del content[:]
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
meraemail = "yaadnahiabhi@gmail.com"
merapswd = "khuljasimsim"

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

            Pcontents = ["hiiiiiiiii"]
            if QnA == "Yes":
                Pcontents.append("WhatsApp link for QnA Event is \n https://chat.whatsapp.com/JynIYPLZEglCFLBiF0PGJc")
            Pcontents.append(contactus)

            yag.send(POE, 'NSS DAY EVENTS DETAIL UCOE', Pcontents)
            contents = []

            if FS0 != "":
                contents0 = [welcome, f"Dear {FS0} {LS0} ", f"From {CN}", f"{CA}",
                             F"Respected {POF} {POL} Had got you registered for the events"
                             "Here are the links for the WhatsApp groups for the same",
                             "", creator(contents, E0), contactus]
                yag.send(ES0, 'NSS DAY EVENTS DETAIL FROM NSS UCOE', contents0)

            if FS1 != "":
                contents1 = [welcome, f"Dear {FS1} {LS1} ", f"From {CN}", f"{CA}",
                             F"Respected {POF} {POL} Had got you registered for the events"
                             "Here are the links for the WhatsApp groups for the same",
                             "", creator(contents, E1), contactus]

                yag.send(ES1, 'NSS DAY EVENTS DETAIL FROM NSS UCOE', contents1)

            if FS2 != "":
                contents2 = [welcome, f"Dear {FS2} {LS2} ", f"From {CN}", f"{CA}",
                             F"Respected {POF} {POL} Had got you registered for the events"
                             "Here are the links for the WhatsApp groups for the same",
                             "", creator(contents, E2), contactus]
                yag.send(ES2, 'NSS DAY EVENTS DETAIL FROM NSS UCOE', contents2)
            if FS3 != "":
                contents3 = [welcome, f"Dear {FS3} {LS3} ", f"From {CN}", f"{CA}",
                             F"Respected {POF} {POL} Had got you registered for the events"
                             "Here are the links for the WhatsApp groups for the same",
                             "", creator(contents, E3), contactus]
                yag.send(ES3, 'NSS DAY EVENTS DETAIL FROM NSS UCOE', contents3)
            if FS4 != "":
                contents4 = [welcome, f"Dear {FS4} {LS4} ", f"From {CN}", f"{CA}",
                             F"Respected {POF} {POL} Had got you registered for the events"
                             "Here are the links for the WhatsApp groups for the same",
                             "", creator(contents, E4), contactus]
                yag.send(ES4, 'NSS DAY EVENTS DETAIL FROM NSS UCOE', contents4)

            if FS5 != "":
                contents5 = [welcome, f"Dear {FS5} {LS5} ", f"From {CN}", f"{CA}",
                             F"Respected {POF} {POL} Had got you registered for the events"
                             "Here are the links for the WhatsApp groups for the same",
                             "", creator(contents, E5), contactus]
                yag.send(ES5, 'NSS DAY EVENTS DETAIL FROM NSS UCOE', contents5)
            if FS6 != "":
                contents6 = [welcome, f"Dear {FS6} {LS6} ", f"From {CN}", f"{CA}",
                             F"Respected {POF} {POL} Had got you registered for the events"
                             "Here are the links for the WhatsApp groups for the same",
                             "", creator(contents, E6), contactus]
                yag.send(ES6, 'NSS DAY EVENTS DETAIL FROM NSS UCOE', contents6)
            if FS7 != "":
                contents7 = [welcome, f"Dear {FS7} {LS7} ", f"From {CN}", f"{CA}",
                             F"Respected {POF} {POL} Had got you registered for the events"
                             "Here are the links for the WhatsApp groups for the same",
                             "", creator(contents, E7), contactus]
                yag.send(ES7, 'NSS DAY EVENTS DETAIL FROM NSS UCOE', contents7)
            if FS8 != "":
                contents8 = [welcome, f"Dear {FS8} {LS8} ", f"From {CN}", f"{CA}",
                             F"Respected {POF} {POL} Had got you registered for the events"
                             "Here are the links for the WhatsApp groups for the same",
                             "", creator(contents, E8), contactus]
                yag.send(ES8, 'NSS DAY EVENTS DETAIL FROM NSS UCOE', contents8)
            if FS9 != "":
                contents9 = [welcome, f"Dear {FS9} {LS9} ", f"From {CN}", f"{CA}",
                             F"Respected {POF} {POL} Had got you registered for the events"
                             "Here are the links for the WhatsApp groups for the same",
                             "", creator(contents, E9), contactus]
                yag.send(ES9, 'NSS DAY EVENTS DETAIL FROM NSS UCOE', contents9)

            print(contents)

print("")
print("TASK SUCCESSFULLY COMPLETED")
