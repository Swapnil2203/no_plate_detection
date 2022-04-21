import flask
from flask import send_file
import werkzeug
import base64
import time
import os
import magic

app = flask.Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def handle_request():
    app.config['UPLOAD_FOLDER'] = './'

    path="a"
    files_ids = list(flask.request.files)
    for file_id in files_ids:
        imagefile = flask.request.files[file_id]
        filename = werkzeug.utils.secure_filename(imagefile.filename)
        # time_stamp = time.strftime("%Y%m%d-%H%M%S")
        path = os.path.join(app.config['UPLOAD_FOLDER'],filename)
        imagefile.save(path)
    if path!="a":    
        msg= magic.call_fun(path)
        print("msg: ",msg)
    # return msg
    # data_uri = base64.b64encode(open('anything.jpg', 'rb').read()).decode('utf-8')
    # print(data_uri)
        return msg
    else:
        return "responding...."    
    # return "Image Uploaded Successfully."


app.run(host="192.168.0.6", port=5000, debug=True)