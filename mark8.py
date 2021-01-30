import yagmail

contents = [
    """Hello Sir/Madam
    Congratulations on your well - deserved success.
    The NSS unit of Universal College of Engineering would like to thank you
    for participating in Inter College Event organised on 24th September 2020.
    
    We have attached your certificate in this email.
    Wish you all the best for your future endeavours.
    
    Reagards,
    NSS UCoE."""
]
print("lets start")
meraemail = "nssucoearchive@gmail.com"
merapswd = "ucoerocx"

yagmail.register(meraemail, merapswd)

print("loggedin")
with yagmail.SMTP(meraemail) as yag:
    yag.send(meraemail, "subject", [contents, '1223.jpg'])

print("successfull")