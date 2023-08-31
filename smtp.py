"""
    @Author: ImYrS Yang
    @Date: 2023/2/27
    @Copyright: ImYrS Yang
    @Description: 
"""

import logging, os, smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr

from configobj import ConfigObj


class Pusher:

    def __init__():
        #SMTP
        self.host = os.environ.get('SMTP_HOST')
        self.port = os.environ.get('SMTP_PORT')
        self.tls = os.environ.get('SMTP_TLS')
        self.user = os.environ.get('SMTP_USER')
        self.password = os.environ.get('SMTP_PASSWORD')
        self.sender = os.environ.get('SMTP_SENDER')
        self.receiver = os.environ.get('SMTP_RECEIVER')

    def send(self, title: str, content: str) -> None:
        """
        发送消息

        :param title: 通知标题
        :param content: 消息内容
        :return:
        """
        smtp = smtplib.SMTP(self.host, self.port)
        smtp.ehlo()

        if self.tls:
            smtp.starttls()

        smtp.login(self.user, self.password)

        message = MIMEText(content, 'plain', 'utf-8')
        message['From'] = formataddr((str(Header('Airpot checkin', 'utf-8')), self.sender))
        message['To'] = self.receiver
        message['Subject'] = title
        print("开始发送")
        smtp.sendmail(self.sender, [self.receiver], message.as_string())


def push(
        content: str,
        content_html: str,
        title: str,
) -> bool:
    """
    签到消息推送
    :param content: 推送内容
    :param content_html: 推送内容, HTML 格式
    :param title: 标题
    :return:
    """

    try:
        pusher = Pusher()
        if (not self.host
            or not self.port
            or not self.tls 
            or not self.user
            or not self.password
            or not self.sender
            or not self.receiver):
            logging.error('SMTP 推送参数配置不完整')
            return False
            
        print("smtp参数配置完整")
        pusher.send(title, content)
        logging.info('SMTP 推送成功')
    except Exception as e:
        logging.error(f'SMTP 推送失败, 错误信息: {e}')
        return False

    return True
