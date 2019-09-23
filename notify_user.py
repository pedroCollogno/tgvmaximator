import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json

def notify_user(origin, destination, date, dic, user_list):
    for user in user_list:
        with open('emails_to_ping.json') as json_file:
            user_info = json.load(json_file)
            receiver_email = user_info[user]['email']
            name = user_info[user]['name']
            port = 465  # For SSL
            smtp_server = "smtp.gmail.com"
            sender_email = "tgvmaximator@gmail.com"  # Enter your address
            password = 'amsterdam86'
            message = MIMEMultipart("alternative")
            message["Subject"] = "Bonjour M. {}".format(name)
            message["From"] = sender_email
            message["To"] = receiver_email

            # Create the plain-text and HTML version of your message
            text = """\
            Bonjour M. {0},
            Un nouveau train TGVMax est disponible pour votre trajet de {1} a {2} le {3}. Il part à {4}. 
            Si cet horaire vous correspond vous pouvez aller manger nos couilles en salade.
            
            Cordialement,
            L'équipe TGVMaximator""".format(name, origin, destination, date.strftime("%Y-%m-%d"), dic['departure_time'].strftime("%Hh%M"))

            html = """\
            <html>
            <body>
                <p>Bonjour M. {0},<br>
                Un nouveau train TGVMax est disponible pour votre trajet de {1} a {2} le {3}. Il part à {4}. 
                Si cet horaire vous correspond vous pouvez aller manger mes couilles en salade.<br>
                Rendez-vous sur <a href="https://www.oui.sncf/bons-plans/tgvmax#!/">Oui.sncf</a> 
                pour vous faire une vinaigrette afin de mieux apprécier le plat de chibre.<br>
                <br>
                Cordialement,<br>
                L'équipe TGVMaximator
                </p>
            </body>
            </html>
            """.format(name,origin, destination, date.strftime("%Y-%m-%d"), dic['departure_time'].strftime("%Hh%M"))

            # Turn these into plain/html MIMEText objects
            part1 = MIMEText(text, "plain")
            part2 = MIMEText(html, "html")

            # Add HTML/plain-text parts to MIMEMultipart message
            # The email client will try to render the last part first
            message.attach(part1)
            message.attach(part2)

            # Create secure connection with server and send email
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(
                    sender_email, receiver_email, message.as_string()
                )
                print("Sent email to {}".format(name))