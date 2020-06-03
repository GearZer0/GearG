import paramiko
from scp import SCPClient
import win32com.client
import os
from getpass import getpass

def createSSHClient(server, port, user, password):
    try:
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(server, port, user, password)
        return client
    except paramiko.AuthenticationException:
        print("Wrong password")
        quit()

def sendEmail(filenames):
    outlook = win32com.client.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = ''
    mail.Subject = 'GTI'
    mail.Body = 'Hi Team, Please upload for GTI'
#   mail.HTMLBody = '<h2>HTML Message body</h2>' #this field is optional

    # To attach file to the email (optional):
    for filename in filenames:
        attachment  = filename
        mail.Attachments.Add(attachment)

    mail.SentOnBehalfOfName = ''
    mail.Send()
    print("Email sent ...") 

if __name__ == "__main__":
    try:
        os.mkdir("SCP") # folder name
    except:
        pass
    server = "" # place the host name
    port = "" # place the port
    user = "root" # place the username
    password = getpass()
    ssh = createSSHClient(server, port, user, password)
    scp = SCPClient(ssh.get_transport())
    files = [''] # file names on server
    local_files = []
    for file_name in files:
        path = "/root/gti_feed/tmp/" + file_name # place the FOLDER path that you want copied
        filename = path.split('/')[-1] + ".csv"
        scp.get(path, os.getcwd() + '/SCP/' + filename)
        if os.stat(os.getcwd() + '/SCP/' + filename).st_size == 0:
            os.remove(os.getcwd() + '/SCP/' + filename) # zero length file
            continue
        local_files.append(os.getcwd() + '/SCP/' + filename)
    sendEmail(local_files)
    scp.close()
    for file_name in files:
        try:
            os.remove(os.getcwd() + '/SCP/' + file_name + ".csv")
        except:
            pass
