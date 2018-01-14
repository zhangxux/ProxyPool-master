import random

from proxypool.setting import USERAGENT_LIST


class UserAgent(object):

    def user_agent(self):
        ua = random.choice(USERAGENT_LIST)
        return ua

if __name__ == '__main__':
    ua = UserAgent()
    print(ua.user_agent())