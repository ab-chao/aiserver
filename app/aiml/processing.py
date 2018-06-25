import aiml
import os


class AilmProcess(object):

    @classmethod
    def get_ai_kernel(cls):
        aiKernel = aiml.Kernel()
        if os.path.isfile("bot_brain.brn"):
            aiKernel.bootstrap(brainFile="bot_brain.brn")
        else:
            aiKernel.bootstrap(learnFiles="./aiml/std-startup.xml", commands="load aiml b")
            aiKernel.saveBrain("bot_brain.brn")
        return aiKernel

    # @classmethod
    # def get_ai_kernel_resp(cls, text):
    #     return aiKernel.respond(text)
