from flask import Blueprint, json, request
from .processing import ChatProcess

nlp = Blueprint('nlp', __name__)


@nlp.route('/cut', methods=['POST'])
def participle():
    text = json.loads(request.data)['text']

    process = ChatProcess()
    if text.startswith('setdict:'):
        result = process.setdict(text)
    else:
        cut = process.cut(text)
        result = "【分词结果】:" + ','.join(cut)
        print(result)
        tags = process.extract_tags(text)
        result += "\n\t【关键词】:" + ','.join(tags)
        print(result)

    return json.dumps({'code': 0, 'text': result}, ensure_ascii=False)

