import smtplib

fromaddr = 'fenya74.09@gmail.com'
toaddrs  = 'fenya74.09@gmail.com'
msg = 'Why,Oh why!'
username = 'fenya74.09'
password = 'pmnk zkos jcqc wevc'
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username, password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()