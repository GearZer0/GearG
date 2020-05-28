import paramiko
from scp import SCPClient
import win32com.client
import os

def createSSHClient(server, port, user, password):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, port, user, password)
    return client

def sendEmail(filenames):
    outlook = win32com.client.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = ' '
    mail.Subject = ' '
    mail.Body = ' '
#   mail.HTMLBody = '<h2>HTML Message body</h2>' #this field is optional

    # To attach file to the email (optional):
    for filename in filenames:
        attachment  = filename
        mail.Attachments.Add(attachment)

    mail.SentOnBehalfOfName = ' '
    mail.Send()
    print("Email sent ...")

if __name__ == "__main__":
    try:
        os.mkdir("SCP")
    except:
        pass
    server = " " # place the host name
    port = "22" # place the port
    user = " " # place the username
    password = input("Enter Password: ")
    ssh = createSSHClient(server, port, user, password)
    scp = SCPClient(ssh.get_transport())
    files = ['a','b'] # file names on server
    local_files = []
    for file_name in files:
        path = "/path/to/folder/" + file_name # place the FOLDER path that you want copied
        filename = path.split('/')[-1] + ".csv"
        scp.get(path, 'SCP/' + filename)
        if os.stat('SCP/' + filename).st_size == 0:
            os.remove('SCP/' + filename) # zero length file
            continue
        local_files.append('SCP/' + filename)
    sendEmail(local_files)
    scp.close()
    for file_name in local_files:
        os.remove('SCP/' + file_name)
