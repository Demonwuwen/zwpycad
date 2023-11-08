import os
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/xtocad/index',methods=['GET'])
def index():
    data = request.args.get("t1")
    print("data=", data)

    d1 = request.get_json()
    print(d1)
    return jsonify("'message': 'index successfully'")

@app.route('/xtocad/upload', methods=['POST'])
def upload_files():
    uploaded_files = request.files.getlist('files')

    if len(uploaded_files) == 0:
        return jsonify({'error': 'No files uploaded'})

    for file in uploaded_files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    return jsonify({'message': 'Files uploaded successfully'})



if __name__ == '__main__':
    app.run(debug=True)
