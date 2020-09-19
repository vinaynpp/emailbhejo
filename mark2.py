import yagmail

contents = [
    "This is the body, and here is just text http://vinaypanchal.com",
    "You can find an audio file attached."
]
print("lets start")
meraemail = "nssucoearchive@gmail.com"
merapswd = "ucoerocx"

yagmail.register(meraemail, merapswd)

print("loggedin")
with yagmail.SMTP(meraemail) as yag:
    yag.send('yaadnahiabhi@gmail.com', 'subject', contents)

print("successfull")