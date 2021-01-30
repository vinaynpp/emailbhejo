import yagmail
import csv
import keyring


print("")
print("LET'S START")
print("")
meraemail = str(input("OWN EMAIL \n"))
merapswd = str(input("OWN PASSWORD \n"))

yagmail.register(meraemail, merapswd)

print("")
print("NOW MAIN TASK")
print("")

print("loggedin")
with yagmail.SMTP(meraemail) as yag:
    with open("events.csv") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row

        for FS, LS, ES, CS, CN in reader:
            contents = [f"Dear {FS} {LS}",
                        "Join the following Google meet at sharp 8:45 AM on 24th September 2020 ",
                        "and keep your self mute.",
                        "Just watch the things going on at that time",
                        "Meeting Link for Participants: http://meet.google.com/gpg-pnmn-ugt ",
                        " Please don't share the link with others as it's for participants only.",
                        "You will get a certificates only by participating in the event.",
                        "We will take your attendance during the event.",
                        "Note: For joining the session with mobile, you need to install the Google meet app.",
                        "If you have any doubts, please do not hesitate to contact ",
                        "Mr. Praneeth Hegde (Coordinator)- 8425026490.",
                        "Wish you all the best!",
                        "Regards,",
                        "NSS UCOE"
            ]
            yag.send(ES, 'NSS DAY GOOGLE MEET DETAILS AND INSTRUCTIONS', contents)

print("")
print("TASK SUCCESSFULLY COMPLETED")
