import os
from flask import Flask, request, redirect, jsonify
from DocService import DocService
# import urllib.request
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = "input"

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/match")
def match():
    doc = DocService("./input/sample_1.pdf","./input/sample_2.pdf")
    per = doc.compare()
    return 'Match Percentage is :'+ str(per)+'% for the given documents'

@app.route('/file-upload', methods=['POST'])
def upload_file():
	# check if the post request has the file part
	if 'file' not in request.files:
		resp = jsonify({'message' : 'No file part in the request'})
		resp.status_code = 400
		return resp
	file = request.files['file']
	if file.filename == '':
		resp = jsonify({'message' : 'No file selected for uploading'})
		resp.status_code = 400
		return resp
	if file and allowed_file(file.filename):
		filename = secure_filename(file.filename)
		# file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		file.save(filename)
		resp = jsonify({'message' : 'File successfully uploaded'})
		resp.status_code = 201
		return resp
	else:
		resp = jsonify({'message' : 'Allowed file types are txt, pdf, png, jpg, jpeg, gif'})
		resp.status_code = 400
		return resp