import smtplib, ssl

def notifyUser(origin,destination,date,dic):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "tgvmaximator@gmail.com"  # Enter your address
    receiver_email = "pierre.collignon@supelec.fr"  # Enter receiver address
    password = 'amsterdam86'
    message = """\
Subject: Bonjour M. Merlin,

Vous mangez allegrement des enormes chibres.
Par ailleurs un train est disponible pour votre voyage de {0} a {1} le {2}. Il y a un train tgvmax qui part a {3}""".format(origin, destination, date.strftime("%Y-%m-%d"), dic['departure_time'].strftime("%Hh%M"))
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)