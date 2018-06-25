from flask import Blueprint, json
from .processing import AilmProcess

aiml = Blueprint('aiml', __name__)
aiKernel = AilmProcess.get_ai_kernel()

@aiml.route('/test')
def test():
    return json.dumps({'a': '用于测试'}, ensure_ascii=False)


@aiml.route('/ask')
def ask():
    print(aiKernel.respond('HELLO'))
    # return json.dumps({'code': 0, 'text': process.get_ai_kernel_resp('hi')}, ensure_ascii=False)
