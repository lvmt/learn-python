#/usr/bin/env python
# -*- coding:utf-8 -*-

"""学习邮件发送 

"""  

import smtplib 

"""
发送邮件有两种模式：

１．直接连接邮件服务提供商(被发送者邮件所在服务商)，然后发送邮件即可．好比你要给　xx@hotmail.com 发邮件，直接链接微软的邮件服务发送邮件即可，一般会被微软邮件反垃圾邮件屏蔽．

２．代理转发模式，登录你自己的邮件服务上如qq邮件服务商，发送到qq邮箱中转站，qq代理将邮件投递到微软邮件服务

你代码使用的就是第一种模式．因此　smtpli.SMTP("你要发送的人注册的邮箱的提供商的地址")才能发送

 
参考：

１．http://www.cnblogs.com/leetao94/p/5460520.html

２．http://blog.csdn.net/bravezhe/article/details/7659198
"""

import smtplib
import email

"""导入相关的库文件
"""
# 构造文本
from email.mime.text import MIMEText  
# 构造图片
from email.mime.image import MIMEImage
# 聚合对象
from email.mime.multipart import MIMEMultipart
from email.header import Header


""" 设置邮箱域名，发件人，邮箱授权码，收件人邮箱
"""
## # SMTP服务器,这里使用163邮箱
mail_host = "smtp.163.com"
## 发件人邮箱
mail_sender = "13554221497@163.com"
## 邮箱授权码,注意这里不是邮箱密码, 
mail_license = "Lmt921108"
## 收件人邮箱，可以为多个收件人
mail_receviers = ['2546871627@qq.com', 'lvmengting4480@novogene.com']
## 构建mimemultipart对象
mm = MIMEMultipart('related')

"""设置邮箱头部信息
"""
## 邮件主题
subject_content = """python邮件测试"""
## 设置发送者，遵循格式要求
mm["From"] = "lvmengting<13554221497@163.com>"
mm["To"] = "lmt2<2546871627@qq.com>,lmt<lvmengting4480@novogene.com>"         ## 这个需要和mail_receviers保持一致，最终的收件人，由To确定
## 设置邮件主题
mm["Subject"] = Header(subject_content, "utf-8")


"""添加正文
"""
## 邮件正文内容
body_content = """你好， 这是一个邮件测试！"""

## 构造文本， arg1:内容； arg2：文本格式； arg3：编码方式
message_text = MIMEText(body_content, "plain", "utf-8")

## 向MIMEMultipart对象中添加文本对象
mm.attach(message_text)


"""添加图片
"""
# 二进制读取图片
image_data = open('test.jpg','rb')
# 设置读取获取的二进制数据
message_image = MIMEImage(image_data.read())
# 关闭刚才打开的文件
image_data.close()
# 添加图片文件到邮件信息当中去
mm.attach(message_image)


"""添加excel附件（excel表格）
"""
## 构造附件
atta = MIMEText(open('sample.xlsx', 'rb').read(), 'base64', 'utf-8')
## 设置附件信息
atta["Content-Disposition"] = 'attachment; filename="sample.xlsx"'
## 添加信息到邮件信息当中
mm.attach(atta)

"""发送邮件
"""
## 创建SMTP对象
stp = smtplib.SMTP()
## 设置发件人邮箱域名和端口，端口地址为25 
stp.connect(mail_host, 25)
## set_debuglevel(1)可以打印出和SMTP服务器交互的所有信息
stp.set_debuglevel(1)
## 登录邮箱，
stp.login(mail_sender, mail_license)
## 发送邮件
stp.sendmail(mail_sender, mail_receviers, mm.as_string())
print("邮件发送成功")
## 关闭SMTP对象
stp.quit()





















