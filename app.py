from flask import Flask, render_template, send_file

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/graph')
def graph():
    return render_template('graph.html')

@app.route('/graph2')
def graph2():
    return render_template('graph2.html')

@app.route('/hello/<name>')
def hello(name):
    return render_template('page.html', name=name)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    
    
