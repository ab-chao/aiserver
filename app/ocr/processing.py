import pytesseract
from flask import send_from_directory, app
from werkzeug.utils import secure_filename
from PIL import Image


class ImgProcess(object):

    ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
    FILE_SAVE_PATH = 'D:\\WorkSpace\\img\\'

    def if_file_allowed(self, filename):
        return '.' in filename and filename.rsplit('.', 1)[1] in self.ALLOWED_EXTENSIONS

    def save_img(self, file):
        if file and self.if_file_allowed(file.filename):
            filename = secure_filename(file.filename)
            filename = self.FILE_SAVE_PATH + filename
            # =========
            print(filename)
            # =========
            file.save(filename)
            return file.filename
        return False

    def get_img_text(self, filename):
        image = Image.open(self.FILE_SAVE_PATH + secure_filename(filename))

        # =========用于windows start=========
        pytesseract.pytesseract.tesseract_cmd = 'D:\\devSft\\Tesseract-OCR\\tesseract'
        text = pytesseract.image_to_string(image, lang='chi_sim',
                                           config='--tessdata-dir "D:\\devSft\\Tesseract-OCR\\tessdata"')
        # =========用于windows end=========

        # =========用于linux start=========
        # text = pytesseract.image_to_string(image, lang='chi_sim')
        # =========用于linux end=========

        # =========
        print(text)
        # =========
        return text

    def send_from_directory(self, filename):
        return send_from_directory(self.FILE_SAVE_PATH, filename)
