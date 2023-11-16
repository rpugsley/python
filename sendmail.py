import sys
import getopt
import smtplib
import email.mime.text
import syslog
import os,time
from email.mime.text import MIMEText

# This is the Gmail address to send emails from
GMAIL_ADDRESS = 'aaaa@gmail.com'
# This is the app-specific password:(https://support.google.com/accounts/answer/185833?hl=en)
GMAIL_PASSWORD = 'pass'
# This is the address where the mail is sent to:
RECIPIENT_ADDRESS = 'bbb@gmail.com'

def getargus(argv):
  """
  function getargus() extracts the supported commandline options to variables
  """
  inputfile = ''
  subject = ''
  recipient = ''
  msg_text = ''
  usage = 'Usage: simplemail.py -s <subject> -a <message>'
  try:
    opts, args = getopt.getopt(argv,"hs:a:")
  except getopt.GetoptError:
    print(usage)
    sys.exit(2)
  if (opts == []):
    print(usage)
    sys.exit(2)

  for opt, arg in opts:
    if (opt == '-h') or (opts == ""):
      print(usage)
      sys.exit()
    elif opt == '-a':
      # This is the string to be sent as the message body
      msg_text = arg
    elif opt == '-s':
      subject = arg

  return (subject, msg_text)

if __name__ == "__main__":
  subject = ''
  msg_text = ''
  # Get the commandline arguments
  subject, msg_text = getargus(sys.argv[1:])

  from_email = GMAIL_ADDRESS
  to_email = RECIPIENT_ADDRESS

  # Create a text/plain message from the given string
  msg = MIMEText(msg_text)
  # Set the message headers
  msg['Subject'] = subject
  msg['From'] = from_email
  msg['To'] = to_email
  # Create a secure SMTP connection
  s = smtplib.SMTP_SSL('smtp.gmail.com', '465')
  # Login with the Gmail credentials
  s.login(GMAIL_ADDRESS, GMAIL_PASSWORD)
  # Send the message
  s.sendmail(from_email, to_email, msg.as_string())
  # Close the connection
  s.quit()
