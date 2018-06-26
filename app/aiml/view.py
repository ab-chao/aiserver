from flask import Blueprint, json
from .processing import AilmProcess

aiml = Blueprint('aiml', __name__)
process = AilmProcess()


@aiml.route('/test')
def test():
    return json.dumps({'a': '用于测试'}, ensure_ascii=False)


@aiml.route('/ask')
def ask():
    return json.dumps({'code': 0, 'text': process.respond('你是 猪')}, ensure_ascii=False)
