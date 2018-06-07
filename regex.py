#! python3
import re
import PyPDF2
import pandas as pd

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
ID:                  # repetitive part
\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d|\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d #____ this should be 20 | 21 digit num
'''
, re.VERBOSE)

#Write a for-loop to open many files


#Read the PDF file and get the text from it
pdfFileObj = open('test.pdf', 'rb')

#Get the num of pages in PDF
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
numPages = pdfReader.numPages
print('There are: ' + str(numPages)+ ' pages in this PDF.')

#Check if PDF is encrypted
isEncrypted = pdfReader.isEncrypted
print('This PDF is encrypted: '+ str(isEncrypted))



#Get Page obj for page 1
pageObj = pdfReader.getPage(0)

#Get the text needed for search
text = pageObj.extractText()
#this does not print anything!!!

# text for test
text = '''
5/29/2018 https://redbull.zendesk.com/tickets/751945/print
https://redbull.zendesk.com/tickets/751945/print 1/1
#751945 EXT: AIR RACE 2_Prod v2300344 / 998661131503407104
User has requested for personal information
Submitted
May 27, 2018, 03:13
Received via
Mail
Requester
Sessiongamesemailer <sessiongamesemailer@gmail.com>
Status
New
Group
HQ.Privacy
Assignee
-
Country
International
Outgoing Email (Brand)
privacy@redbull.com
Sessiongamesemailer May 27, 03:13
User request e-mail: jashby81@yahoo.com
Account Info:
User ID: 998661131503407104
User Display Name: Justin
Account Email:
Meta Fields: {"redbull.email":"Jashby81@yahoo.com","redbull.avatar":null}
Build: AIR RACE 2_Prod v2300344
Bundle ID: com.redbull.airrace2
Fyber App ID: 45617
Support Software by Zendesk

'''

#Extract the ticket num, user ID, and email from this text
extractedTicket = ticketNumRegex.findall(text)
extractedEmail = EmailNumRegex.findall(text)
extractedUserId = UserIdRegex.findall(text)

#Remove unnecessary information from the results

#Remove one of the 'same' emails - case insensitive -- not working
#for i in extractedEmail:
 #   if i.lower() == i.lower():
  #      extractedEmail.remove(i)

for i in extractedEmail:
    if i == 'sessiongamesemailer@gmail.com':
        extractedEmail.remove(i)

for i in extractedEmail:
    if i == 'privacy@redbull.com':
        extractedEmail.remove(i)

for i in extractedUserId:
    if i == i:
        extractedUserId.remove(i)
    elif i == i:
        extractedUserId.remove(i)
    elif i == '':
        extractedUserId.remove(i)
final = [extractedTicket,extractedEmail,extractedUserId]
print(final)
#Create datafrome using Pandas, so that to store my findings into the csv file
#df = pd.DataFrame({
#    'Zendesk ticket num':extractedTicket,
#    'User request email': extractedEmail,
#    'User ID': extractedUserId
#})
#df.to_csv('new-csv-file.csv')
#print(df)
