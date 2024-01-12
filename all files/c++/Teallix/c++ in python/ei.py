import re

ai = 'purple Teallix@google.com, blah monkey bob@abc.com blah dishwasher'
emails = re.findall(r'[\w\.-]+@[\w\.-]+', ai)

for email in emails:
    print(email)