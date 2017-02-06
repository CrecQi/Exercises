# -*- coding: utf-8 -*- 
#Keep seaching PowerPoints in Desktop and send them with E-Mail
#Copyright BobLau 2017
#This version is adopted for Windows

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib, os, sys


def FindPPT(start_dir):
	for cur_path, dir_names, file_names in os.walk(start_dir):
		for file_name in file_names:
			if file_name.endswith('.ppt') or file_name.endswith('.pptx'):
				attachment_list.append(os.path.join(cur_path, file_name))
	return attachment_list


def send_attached_mail(mail_to, mail_subject, body_words, mail_attachment):
	msg = MIMEMultipart()  #创建一个邮件（主体）实例
	#定义邮件（主体）头
	msg['Subject'] = mail_subject
	msg['From'] = login_name
	msg['To'] = mail_to

	#创建附件
	f = open(mail_attachment,'rb')    #以二进制读的方式打开（不以二进制方式的话附件打开是乱码,可能与MIME以二进制方式传输有关
	att = MIMEText(f.read(), 'plain', 'utf-8')    #在FindPPT函数内的中文文件名是乱码，但实际上发到邮箱的附件正常显示中文，可能与这里有关
	##定义附件头（告诉邮件程序应如何处理附件）
	att.add_header('Content-Disposition', 'attachment', filename = mail_attachment) 
	#att['Content-Disposition'] = 'attachment', filename = 'mail_attachment.ppt' #定义“编排模式”，实际上是通过定义文件名来规定附件的打开方式
	msg.attach(att) 	#添附到邮件主体

	#创建正文
	body = MIMEText(body_words, 'plain', 'utf-8')
	msg.attach(body)	#添附到邮件主体


	#Send
	try:
		server = smtplib.SMTP_SSL('smtp.qq.com',465)  #创建SMTP实例（SSL加密）
		server.login(login_name, auth_num)   #登录QQ邮箱的SMTP服务器
		server.sendmail(msg['From'], msg['To'], msg.as_string())  #发送邮件
		server.quit()    #断开与SMTP服务器的连接
		return True
	except Exception, e:
		return False


login_name = raw_input("Enter your Email address:")     #user name
auth_num = raw_input("Enter the authorizing number:")   #authorizing number
attachment_list = []
sent_list = []
message = 0
while True:
	f_list = FindPPT('C:\Users\Administrator\Desktop')
	if f_list == []:
                if message == 0:
                        print "Seaching..."
                        message = 1
		continue
	else:
		for file in f_list:
			if file not in sent_list:
				print '[Sending]', file
				if send_attached_mail(login_name, 'PPT Files', 'PPTs from Desktop...', file):
					print "[Succeeded]"
					sent_list.append(file)
					message = 1
				else:
					print "[Failed]", file
					message = 1
			elif message == 1:
                                print "Seaching..."
                                message = 2
                                

