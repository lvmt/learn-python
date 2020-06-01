#!/usr/bin/env python
#-*- coding:utf-8 -*-


import glob
import paramiko
from scp import SCPClient, SCPException


hostname = '39.106.135.106'
username = 'report'
password = 'disease-report-2019'
port = 22

with paramiko.SSHClient() as ssh:
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=hostname,port=port,username=username,password=password)

    with SCPClient(ssh.get_transport(), socket_timeout=60) as scp:

        remote_path = '/data/www/project/report/Mapping'
        
        cmd = '''
        if [ ! -d {remote_path} ];then
            mkdir -p {remote_path}
        fi
        '''.format(**locals())
        
        stdin, stdout, stderr = ssh.exec_command(cmd)
        print(stdout.read())
        print(stderr.read())
        
        for each in glob.glob('Mapping/*'):
            print('uploading {}...'.format(each))
            # help(scp.put)
            scp.put(each, remote_path, recursive=True)
