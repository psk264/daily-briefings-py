# app/email_service.py

from logging import error, exception
import smtplib
import os
from dotenv import load_dotenv
# from sendgrid import SendGridAPIClient
# from sendgrid.helpers.mail import Mail

load_dotenv()

# SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
# SENDER_EMAIL_ADDRESS = os.getenv("SENDER_EMAIL_ADDRESS")


# def send_email(subject="[Daily Briefing] This is a test", html="<p>Hello World</p>", recipient_address=SENDER_EMAIL_ADDRESS):
#     """
#     Sends an email with the specified subject and html contents to the specified recipient,

#     If recipient is not specified, sends to the admin's sender address by default.
#     """
#     client = SendGridAPIClient(SENDGRID_API_KEY) #> <class 'sendgrid.sendgrid.SendGridAPIClient>
#     print("CLIENT:", type(client))
#     print("SUBJECT:", subject)
#     #print("HTML:", html)

#     message = Mail(from_email=SENDER_EMAIL_ADDRESS, to_emails=recipient_address, subject=subject, html_content=html)
#     try:
#         response = client.send(message)
#         print("RESPONSE:", type(response)) #> <class 'python_http_client.client.Response'>
#         print(response.status_code) #> 202 indicates SUCCESS
#         return response
#     except Exception as e:
#         print("OOPS", type(e), e.message)
#         return None




#
#!/usr/bin/python3
# ---------------------------------------------------------------------- #
# Following custom function is to send the receipt via email (gmail smtp)
# ... Reference: https://www.tutorialspoint.com/send-mail-from-your-gmail-account-using-python
# ... This code block requires a gmail account without 2-factor authentication
# ... Also, less secure access enabled as mentioned in above article
# ---------------------------------------------------------------------- #

def send_email(subject="[Daily Briefing] This is a test", html="<p>Hello World</p>"):
    load_dotenv()
    SENDER_ADDRESS = os.getenv("GMAIL_SENDER", default="OOPS, please set env var called 'SENDER_ADDRESS'")
    SENDER_AUTH = os.getenv("GMAIL_AUTH")
    EMAIL_SERVER = os.getenv("EMAIL_SERVER_SMTP")
    CUSTOMER_ADDRESS=SENDER_ADDRESS #Send default value in case of empty customer email address
    # CUSTOMER_ADDRESS = input("Please enter customer's email address: ")


    # while len(CUSTOMER_ADDRESS)>0:
    #     if("@" in CUSTOMER_ADDRESS and "." in CUSTOMER_ADDRESS):
    #         break
    #     else:
    #         print("Sorry, you entered invalid email address")
    #         print("Please review and print the receipt instead. A copy of receipt is stored in receipts directory")
    #         return
    # print(subject)
    # print(html)
    sender = SENDER_ADDRESS
    receivers = [CUSTOMER_ADDRESS]
    # subject="[Daily Briefing] This is a test"
    # # html="<p>Hello World</p>"

    # message = Mail(from_email=sender, to_emails=receivers, subject=subject, html_content=html)
    
    message = """Subject: {subject}""" + html

    try:
        smtpObj = smtplib.SMTP(EMAIL_SERVER, 587)
        smtpObj.starttls() #enable security
        smtpObj.login(SENDER_ADDRESS, SENDER_AUTH) #login with mail_id and password
        smtpObj.sendmail(sender, CUSTOMER_ADDRESS, message)         
        print("Successfully sent email")
    except Exception as SMTPException:
        print("Error: unable to send email")
    


        
if __name__ == "__main__":
    example_subject = "[Daily Briefing] This is a test"

    example_html = f"""
    <h3>This is a test of the Daily Briefing Service</h3>

    <h4>Today's Date</h4>
    <p>Monday, January 1, 2040</p>

    <h4>My Stocks</h4>
    <ul>
        <li>MSFT | +3%</li>
        <li>GOOG | +2%</li>
        <li>AAPL | +4%</li>
    </ul>

    <h4>My Forecast</h4>
    <ul>
        <li>10:00 AM | 65 DEGREES | CLEAR SKIES</li>
        <li>01:00 PM | 70 DEGREES | CLEAR SKIES</li>
        <li>04:00 PM | 75 DEGREES | CLEAR SKIES</li>
        <li>07:00 PM | 67 DEGREES | PARTLY CLOUDY</li>
        <li>10:00 PM | 56 DEGREES | CLEAR SKIES</li>
    </ul>
    """

    send_email(example_subject, example_html)  
