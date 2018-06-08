#! python3
import re
import PyPDF2
import pandas as pd

#Zendesk ticket
ticketNumRegex = re.compile(r'''
\#\d\d\d\d\d\d #e.g.752944
'''
, re.VERBOSE)

#User email
EmailNumRegex = re.compile(r'''
# some.+_thing@(\d{2,5}))?.com
[a-zA-Z0-9_.+]+  # name part
@                # @ symbol
[a-zA-Z0-9_.+]+  # domain name
'''
, re.VERBOSE)

#User ID number
UserIdRegex = re.compile(r'''
ID:              # repetitive part
\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d|
\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d
'''
, re.VERBOSE)

#For-loop to open many files


#Read the PDF file
pdfFileObj = open('test.pdf', 'rb')

#Num of pages in PDF
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
numPages = pdfReader.numPages
print('There are: '+
      str(numPages)+
      ' pages in this PDF.')

#?PDF is encrypted
isEncrypted = pdfReader.isEncrypted
print('This PDF is encrypted: '+
      str(isEncrypted))

#Page obj for page 1
pageObj = pdfReader.getPage(0)

#Text for search !=work
text = pageObj.extractText()

#text for test
text = '''

'''

#Extract data from text
extractedTicket = ticketNumRegex.findall(text)
extractedEmail = EmailNumRegex.findall(text)
extractedUserId = UserIdRegex.findall(text)

#Remove unnecessary information from the results
lowercase_extractedEmail = [x.lower()
                            for x in extractedEmail]

y = list(set(lowercase_extractedEmail))
print(y)


for i in y:
    if i == 'sessiongamesemailer@gmail.com':
        y.remove(i)


#Problem: if there're 2 user emails *e.g.
#request email & meta email  => program crashes
for i in y:
    if i == 'joeri.martens78@seznam.cz':
        y.remove(i)
for i in y:
    if i == 'privacy@redbull.com':
        y.remove(i)


for i in extractedUserId:
    set(extractedUserId)
    if i == i:
        extractedUserId.remove(i)
    elif i == '':
        extractedUserId.remove(i)

final = [extractedTicket,
         y,
         extractedUserId]

print(len(extractedTicket))
print(len(y))
print(len(extractedUserId))

#Create datafrome using Pandas
df = pd.DataFrame({
    'Zendesk ticket num':extractedTicket,
    'User request email': y,
    'User ID': extractedUserId
})
#Save as csv file
#df.to_csv('new-csv-file.csv')


print(df)
