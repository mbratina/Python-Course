##############################################################################
# paramiko_example.py
#
# Tries out some Paramiko commands to connect to the Cisco XE router
#
# 06/20/18 - Original code
##############################################################################
#   These packaages must  be  downloaded  first    paramiko     sshclient     ssh-paramiko     ssh-import-id
#  Do not rename this file to paramiko
import paramiko
import time
if __name__ == "__main__":
    pre_connection = paramiko.client.SSHClient()
    pre_connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    pre_connection.connect("192.168.10.80", port=22, username='admin', password='cisco', look_for_keys=False, allow_agent=False)
    connection = pre_connection.invoke_shell()
    output = connection.recv(65535)
    print output
    connection.send("show ip int brief\n")
    time.sleep(.5)
    output = connection.recv(65535)
    print output
    connection.send("show ver\n")
    time.sleep(.5)
    output = connection.recv(65535)
    print output
