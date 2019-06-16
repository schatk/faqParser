import re

# Open the poorly formatted FAQ
f = open("badFAQ.html")
file_str = f.read()
f.close()

# Clear styling from tags (will also remove <span> tags)
r = re.sub('.style.*">','>',file_str)
file_str = r

# Parse that formatted string, remove all </span> tags
r = re.sub('</span>','',file_str)
file_str = r

# Remove all &nbsp; 
r = re.sub('&nbsp;',' ',file_str)
file_str = r

# Write the final string to the output file
f = open("goodFAQ.html","w")
f.write(file_str)
f.close()