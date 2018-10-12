import re



line = '812-2-10'
  
#   1999-1-20
  
#   1999-01-20
  
#   812-2-10

myRegex = '^\d{1,4}?-\d{1,2}-\d{1,2}$'

matchObj = re.search(myRegex, line)

if not matchObj:
   print('no match')
else:
   myMatch = matchObj.group(0)
   print(myMatch)