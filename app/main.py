from flask import Flask, render_template
import os

app = Flask(__name__, template_folder=os.path.dirname(__file__))

@app.route('/',methods = ['GET'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')