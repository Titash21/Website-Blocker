import time
#define a namespace for datetime
from datetime import datetime as dt
#if you write r before, you tell python that you want to enter it as a raw strng and no special characters
hosts_path=r"C:\Windows\System32\drivers\etc\hosts"
host_temp=r"D:\Python Programs\Website Blocker\host"
redirect="127.0.0.1"
website_block_list=["www.facebook.com","facebook.com","www.pornhub.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,16) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,20):
        print("Working Hours...")
        #check if the host file already has these 4 websites listed to be blocked or not
        with open(hosts_path,'r+') as file:
            content=file.read()
            for website in website_block_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+ website+"\n")
    else:
        with open(hosts_path,'r+') as file:
            #make a list of all items in the file
            content=file.readlines()
            #take the pointer to the start of the file so that you can copy the lines at the starting of the file and delete all content after that
            file.seek(0)
            for eachLine in content:
                #list comprehension
                #any and all are useful Python functions. Given an iterable (like a list, a generator, an str, etc.), these functions
                #check if any or all of the values are True (or "truthy").
                #if the website is not present in the line, write that line to the new file
                if not any(website in eachLine for website in website_block_list):
                    file.write(eachLine)
            #after the file contents are written the pointer will point to the last line which does not contain the website names from the website_block_list
            #the truncate method will delete all the lines from the file below it
            file.truncate()
    time.sleep(5)
