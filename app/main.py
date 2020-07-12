from flask import Flask, render_template
import os

app = Flask(__name__, template_folder=os.path.dirname(__file__))

@app.route('/',methods = ['POST', 'GET'])
def index():
    return render_template('jogo.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)