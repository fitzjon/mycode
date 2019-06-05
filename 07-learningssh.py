#!/usr/bin/python3
""" Author : fitzjon || Purpose: Learning SSH with Python """

import os

import paramiko

SRVRS = [{'ip':'10.10.2.3', 'un':'bender'}, {'ip':'10.10.2.4', 'un':'fry'}]

with open("cmd2issue.txt", "r") as cmds:
    CMDLIST = cmds.readlines() 
# CMDLIST = ['touch sshworked.txt', 'touch sshworked2.txt', 'uptime']


# This is to have the loop touch each file in the CMDLIST Function ( See Line 25 & 26 ) 
def cmdissue(sshsession, commandtoissue):
    ssh_stdin, ssh_stdout, ssh_stderr = sshsession.exec_command(commandtoissue.rstrip('n'))
    return ssh_stdout.read().decode('utf-8').rstrip('\n')

def main():
    # harvest RSA key (ssh private key)
    myprivkey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")

    for server in SRVRS:
        # init connection to remote machine
        sshsession = paramiko.SSHClient()
        sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        sshsession.connect(hostname=server['ip'], username=server['un'], pkey=myprivkey)

        # touch some files 
        # get uptime of server
        for commandtoissue in CMDLIST:
            result = cmdissue(sshsession, commandtoissue)
            if result != "":
                with open( (server['ip']).replace(".", "") + ".log", "a" ) as svrlog:
                    print("COMMAND ISSUED -", commandtoissue, file=svrlog)
                    print(result, file=svrlog)
                    # Below adds blank space
                    print("===============================================", file=svrlog)

        # close the connection
        sshsession.close()

if __name__ == '__main__':
    main()

