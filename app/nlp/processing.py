import os
import jieba
import jieba.analyse

jieba.load_userdict(os.path.dirname(os.path.realpath(__file__)) + "\\aidict.txt")


class ChatProcess(object):

    def cut(self, text):
        return jieba.cut(text)

    def setdict(self, cmd):
        arr = cmd.split(':')
        if len(arr) == 3:
            if arr[1] == 'add':
                jieba.add_word(arr[2])
                return '添加词典【' + arr[2] + '】成功！'
            elif arr[1] == 'del':
                jieba.del_word(arr[2])
                return '删除词典【' + arr[2] + '】成功！'
            else:
                return '错误的命令！'
        else:
            return '错误的命令！'

    def extract_tags(self, sentence):
        return jieba.analyse.extract_tags(sentence)





