# AutomateSCP tool

AutomateSCP tool automatically copy file remotely from a server using SCP to a folder locally (i.e desktop) and then email the results.

## Break down of the automation steps
````
1. Login remotely to server using SCP
2. Input Password to the server
3. Copy files to a local folder
4. delete file that is 0kb
5. convert the file into .csv
6. send email to recipient
7. Delete all the files in local folder
````

## Configuration
Fill in the following in auto.py :
<pre>
1. mail.To = ' '                                          'Input email address of the recipient'
2. mail.Subject = ' '                                     'Input email subject name'
3. mail.Body = ' '                                        'Input body of the email'
4. mail.SentOnBehalfOfName = ' '                          'Input email address of the sender'
5. server = " "                                           'Input IP address of the server'
6. user = " "                                             'Input the username of the server'
7. files = ['a','b']                                      'Input the filename(s) of the files in the server'
8. path = "/path/to/folder/" + file_name                  'Input the folder path of the server'
</pre>

## Requirements
Install the following modules :
### Python pip install xxxxxxxxx
````
1. paramiko
2. scp 
3. pywin32
````

# Command to run this tool
python auto.py

# Create the Batch File
Create a Notepad file and input the following into the notepad :
```
cd "Path where your script is"
python auto.py
pause
```
Save the Notepad as name.bat
