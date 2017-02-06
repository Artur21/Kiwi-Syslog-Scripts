import re
#define the string
rawtext = "2786: Dec 3 03:51:38: %LINEPROTO-5-UPDOWN: Line protocol on Interface serial100/34, changed state to down"
#create the regexp to capture 
match = re.search(r'(\w+\/\d+).*(up|down)$', rawtext)
#print out the match
if match:
   interface = match.group(1)
   status = match.group(2)
print (interface)
print (status)
