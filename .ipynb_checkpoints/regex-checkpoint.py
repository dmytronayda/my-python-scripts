#! python3
import re

#Create a regex for Zendesk ticket number (e.g. #752944)
ticketNumRegex = re.compile(r'''
\#\d\d\d\d\d\d       #____#752944
'''
, re.VERBOSE)

#Create a regex for User email (e.g. jafeth.sotela@gmail.com)
EmailNumRegex = re.compile(r'''
# some.+_thing@(\d{2,5}))?.com
[a-zA-Z0-9_.+]+      # name part
@                    # @ symbol
[a-zA-Z0-9_.+]+      # domain name part
'''
, re.VERBOSE)
#Create a regex for User ID number number - 20 digits (e.g. 999954983661096960)
UserIdRegex = re.compile(r'''
(\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d)|(\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d)  #____ this should be 20 | 21 digit num
'''
, re.VERBOSE)


#Paste the text to be reviewed
text = '''

'''

#Extract the ticket num, user ID, and email from this text
extractedTicket = ticketNumRegex.findall(text)
extractedEmail = EmailNumRegex.findall(text)
extractedUserId = UserIdRegex.findall(text)

preFinal = [extractedTicket,extractedEmail,extractedUserId]
final = [preFinal[0], preFinal[1][2], preFinal[2][1]]
for i in final:
    print(i)
