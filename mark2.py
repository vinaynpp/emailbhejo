import yagmail

contents = [
    "This is the body, and here is just text http://vinaypanchal.com",
    "You can find an audio file attached."
]
print("lets start")
yagmail.register('yaadnahiabhi@gmail.com', 'khuljasimsim')

print("loggedin")
with yagmail.SMTP('yaadnahiabhi@gmail.com') as yag:
    yag.send('tuguesskar@gmail.com', 'subject', contents)

print("successfull")