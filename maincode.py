import pyperclip,re
phonenumberformat=re.compile(r'''(
(\d{3}|\(\d{3}\))? #the first of phone number
(\s|\.|-)? #separator between first and second part
(\d{3}) # second part of phone number
(\s|\.|-) #separator between second and third part
(\d{4})
(\s*(ext|x|ext.)\s*(\d{2,5}))? #extention

)''', re.VERBOSE)
emailaddress=re.compile(r'''(
[a-zA-Z%-+-]+ #username 
@ # the @ symbol
[a-zA-z]+ #the domain name
\.
[a-zA-Z]{3,5} # the last part of the email
)''',re.VERBOSE)

source=str(pyperclip.paste()) #assigned the copied info to a variable
phone_numbers=phonenumberformat.findall(source)     # finding all matches in source
emails=emailaddress.findall(source)

matches=[]
for email in emails:
    matches.append(email) # appends all matched emails into the match array
for phone_number in phone_numbers:
    phone_number="-".join((phone_number[1],phone_number[3],phone_number[5])) #joins each section of phone with a - and appends it
    matches.append(phone_number)
    if phone_number[8]!='':
        phone_number+="x"+ phone_number[8] #accounts for extensions
if len(matches)>0:
    pyperclip.copy('\n'.join(matches))
    print("copied to clipboard")
    print('\n'.join(matches))
else:
 print('phone numbers or email addresses were no found.')


