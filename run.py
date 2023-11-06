from flask import Flask, request, jsonify, send_file
import os
import ezdxf

app = Flask(__name__)

# 上传文件保存路径
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# 创建上传文件夹（如果不存在）
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# 定义上传文件API端点
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'message': 'No file part'})

    file = request.files['file']

    if file.filename == '':
        return jsonify({'message': 'No selected file'})

    if file:
        # 保存上传文件
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)

        # 处理上传的文件（在此示例中，只将文件名返回）
        return jsonify({'message': 'File uploaded', 'filename': file.filename})

# 定义生成CAD文件API端点
@app.route('/generate_cad', methods=['POST'])
def generate_cad():
    # 接收绘图请求数据
    data = request.json

    # 创建DXF文档
    doc = ezdxf.new()
    msp = doc.modelspace()

    # 在DXF文档中执行绘图操作（这里只是示例，具体绘图逻辑根据需求编写）

    # 保存DXF文件
    dxf_filename = 'output.dxf'
    doc.saveas(dxf_filename)

    # 提供生成的CAD文件下载链接
    return send_file(dxf_filename, as_attachment=True, download_name='output.dxf')

if __name__ == '__main__':
    app.run(debug=True)
