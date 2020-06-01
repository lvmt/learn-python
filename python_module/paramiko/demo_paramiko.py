#!/usr/bin/env python
#-*- coding:utf-8 -*-


import paramiko

"""
基于用户名和密码的 sshclien 方式登陆
"""

# # 建立一个sshclient对象
# ssh = paramiko.SSHClient()

# # 允许将信任的主机自动加入到host_allow列表，此方法必须放在connect方法的前面
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# # 调用connect 方法连接服务器
# ssh.connect(hostname="192.168.96.4", port=22, username="lvmengting4480", password="lmt-lvmengting")

# #执行命令
# stdin, stdout, stderr = ssh.exec_command("pwd")
# print(stdout.read().decode())

# # 关闭连接
# ssh.close()


"""  基于用户名和密码的 transport 方式登录 """

trans = paramiko.Transport(("192.168.96.4", 22))
trans.connect(username="lvmengting4480", password="lmt-lvmengting")

# 将sshclient的对象的transport指定为以上的trans
ssh = paramiko.SSHClient()
ssh._transport = trans

stdid, stdout, stderr = ssh.exec_command("df -hl")
print(stdout.read().decode())

trans.close



""" 传输sftp文件 """
trans = paramiko.Transport(("192.168.96.4", 22))
trans.connect(username="lvmengting4480", password="lmt-lvmengting")

# 实例化一个sftp对象，指定连接的通道
sftp = paramiko.SFTPClient.from_transport(trans)

# 发送文件
sftp.put(localpath="/NJPROJ2/DISEASE/WORK/lvmengting/name.200", remotepath="\F\git\learn-python>")

# # 下载文件
# sftp.get(remotepath, localpath)

trans.close()
