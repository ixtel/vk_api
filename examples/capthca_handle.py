# -*- coding: utf-8 -*-

"""
@author: Kirill Python
@contact: https://vk.com/python273
"""

import vk_api


def captcha_handler(captcha):
    """
        При возникновении капчи вызывается эта функция и ей передается объект
        капчи. Через метод get_url можно получить ссылку на изображение.
        Через метод try_again можно попытаться отправить запрос с кодом капчи
    """

    key = input("Enter Captcha {0}: ".format(captcha.get_url())).strip()

    # Пробуем снова отправить запрос с капчей
    return captcha.try_again(key)


def main():
    """ Пример: обработка капчи """

    login, password = 'python@vk.com', 'mypassword'
    vk_session = vk_api.VkApi(
        login, password,
        captcha_handler=captcha_handler  # функция для обработки капчи
    )

    try:
        vk_session.authorization()
    except vk_api.AuthorizationError as error_msg:
        print(error_msg)
        return

    # some code
    # ...

if __name__ == '__main__':
    main()
