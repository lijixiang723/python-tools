from xsmtplib import xsmtplib
from email.mime.text import MIMEText
from email.header import Header

# 邮箱服务器
mail_host = "smtp.qq.com"
# 你的邮箱用户名
mail_user = "xxxxx@qq.com"
# 发送方邮箱名
sender = "xxxxx@qq.com"
# 接受方邮箱名
get_mail = "xxxxx@163.com"
# 邮箱授权码
mail_password = "xxxxxxx"

smtp_object = xsmtplib.SMTP()
smtp_object.connect(mail_host, 25)
smtp_object.login(mail_user, mail_password)


def mail_manage():
    # 自定义邮件内容
    mail_msg = '<h1>这是一个邮件内容信息</h1>'
    receivers = get_mail

    message = MIMEText(mail_msg, 'html', 'utf-8')
    message['From'] = Header(sender, 'utf-8')
    message['To'] = Header("{}".format(get_mail), 'utf-8')

    # 自定义邮件标题
    subject = '这是一个邮件标题'
    message['Subject'] = Header(subject, 'utf-8')
    try:
        smtp_object.sendmail(sender, receivers, message.as_string())
        return "邮件发送成功"
    except Exception as e:
        return "邮件发送失败" + str(e)
    finally:
        # 退出邮箱登录
        smtp_object.quit()


if __name__ == '__main__':
    mail_manage()


































