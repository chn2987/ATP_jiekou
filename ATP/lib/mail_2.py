import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

def mail(title,body,path):
    fromaddr = '646572031@qq.com'
    password = 'ufxuoifkuvutbcij'#第三方授权码(不能直接用密码)
    toaddrs = ['1174873243@qq.com', '549048823@qq.com']#接收人
    #邮件正文
    content = body
    textApart = MIMEText(content)
    #附件1
    imageFile = path
    imageApart = MIMEImage(open(imageFile, 'rb').read(), imageFile.split('.')[-1])
    imageApart.add_header('Content-Disposition', 'attachment', filename=imageFile)

    #创建封装对象(实例化邮件对象)
    m = MIMEMultipart()
    m.attach(imageApart)#封装附件1
    m['Subject'] = title
    try:
        server = smtplib.SMTP('smtp.qq.com')#邮件服务器地址(不同邮件类型地址不一样)
        server.login(fromaddr,password)#登录邮箱
        server.sendmail(fromaddr, toaddrs, m.as_string())#发送邮件
        print('测试报告_发送成功')#发送状态
        server.quit()#退出邮件服务
    except smtplib.SMTPException as e:
        print('error:',e) #打印错误
    input('等待_用于直接运行py文件避免闪退')
