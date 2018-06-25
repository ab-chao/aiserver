from flask import Blueprint, request, json
from .processing import ImgProcess


ocr = Blueprint('ocr', __name__)


@ocr.route('/uploadImg', methods=['POST'])
def upload():
    process = ImgProcess()
    file = request.files['file']
    filename = process.save_img(file)
    text = process.get_img_text(filename)
    return json.dumps({'text': text, 'filename': filename}, ensure_ascii=False)


@ocr.route('/getImg/<filename>')
def get(filename):
    return ImgProcess().send_from_directory(filename)
