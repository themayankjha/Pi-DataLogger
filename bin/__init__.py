from flask import Flask,render_template
from plotter import histoplotter
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    time=histoplotter()
    return render_template('home.html',time=time)

if __name__ == '__main__':
    app.debug = True
    app.run()