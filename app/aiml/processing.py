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
    print('机器人回答：' + bot.respond('你是猪'))

    # print(os.path.dirname(__file__))
