import re

# Open poorly formatted FAQ
f = open("badFAQ.html",errors="ignore")
file_str = f.read()
f.close()

# Clean tags
r = re.sub('.style.*?">','>',file_str)
file_str = r

# Delete &nbsp; 
r = re.sub('&nbsp;',' ',file_str)
file_str = r

# Delete <span>,</span>
r = re.sub('(<span>|</span>)','',file_str)
file_str = r

# Delete <p></p>
r = re.sub('(<p></p>\n\n|<p></p>\n)','',file_str)
file_str = r

# Write the final string to the output file
f = open("goodFAQ.html","w")
f.write(file_str)
f.close()