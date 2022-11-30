from flask import (Flask, send_file, url_for, jsonify, request,render_template)

app = Flask(__name__)
count=0
@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/data', methods=['POST'])
def read_data():
    global count
    datas={}
    datas['count']=count
    return datas

@app.route('/param',methods=['get'])
def parameters():
    global count
    datas =  request.args.get('count')
    count=datas
    #return render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0",port="5000",debug=True)
