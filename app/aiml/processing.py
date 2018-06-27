from app.aiml.core import Kernel
import os
import jieba


class AilmProcess(Kernel):

    CURR_PATH = os.path.dirname(__file__) + '/'

    def __init__(self):
        Kernel.__init__(self)
        if os.path.isfile(self.CURR_PATH + "bot_brain.brn"):
            self.bootstrap(brainFile=self.CURR_PATH + "bot_brain.brn")
        else:
            self.bootstrap(learnFiles=self.CURR_PATH + "std-startup.xml", commands="ABC")
            self.saveBrain(self.CURR_PATH + "bot_brain.brn")


if __name__ == "__main__":
    bot = AilmProcess()
    print('模拟输入：你好啊，机器人')
    print('机器人回答：' + bot.respond('你好啊，机器人'))
    print('模拟输入：有一次我吃了好多')
    print('机器人回答：' + bot.respond('有一次我吃了好多'))
    print('模拟输入：我有一只狗叫旺财')
    print('机器人回答：' + bot.respond('我有一只狗叫旺财'))
    print('模拟输入：我的狗叫什么？')
    print('机器人回答：' + bot.respond('我的狗叫什么？'))

    # print(os.path.dirname(__file__))
