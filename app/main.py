from flask import Flask
from app.aiml.view import aiml
from app.nlp.view import nlp
from app.ocr.view import ocr

app = Flask(__name__)


app.register_blueprint(nlp, url_prefix='/ai/py/nlp')
app.register_blueprint(ocr, url_prefix='/ai/py/ocr')
app.register_blueprint(aiml, url_prefix='/ai/py/aiml')


@app.route('/')
def root():
    return "hello"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8002)
