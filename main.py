import os
import re
import argparse
from aliyundrive import Aliyundrive
import notify


def main():
    parser = argparse.ArgumentParser()
    ali = Aliyundrive()
    message_all = []

    for idx, token in enumerate(token_string):
        result = ali.aliyundrive_check_in(token)
        message_all.append(str(result))

        if idx < len(token_string) - 1:
            message_all.append('--')

    title = '阿里云盘签到结果'
    message_all = '\n'.join(message_all)
    message_all = re.sub('\n+', '\n', message_all).rstrip('\n')

    notify.send(title, message_all)

    print('finish')


if __name__ == '__main__':
    main()
