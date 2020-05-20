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

def sendEmail(filename):
    outlook = win32com.client.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = ' '
    mail.Subject = ' '
    mail.Body = ' '
#   mail.HTMLBody = '<h2>HTML Message body</h2>' #this field is optional

    # To attach a file to the email (optional):
    attachment  = filename
    mail.Attachments.Add(attachment)

    mail.SentOnBehalfOfName = ' '
    mail.Send()
    print("Email sent ...")

if __name__ == "__main__":
    server = "IP address" # place the host name
    port = "22" # place the port
    user = "Username" # place the username
    password = input("Enter Password: ")
    ssh = createSSHClient(server, port, user, password)
    scp = SCPClient(ssh.get_transport())
    path = "/path/to/file" # place the file path that you want copied
    filename = path.split('/')[-1] + ".csv"
    scp.get(path, filename)
    sendEmail(filename)
    scp.close()
    os.remove(filename)
