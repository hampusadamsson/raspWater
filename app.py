from flask import Flask, render_template, send_file

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/moisture_1')
def moisture1():
    return render_template('moisture_1.html')
@app.route('/moisture_2')
def moisture2():
    return render_template('moisture_2.html')
@app.route('/temperature')
def temperature():
    return render_template('temperature.html')
@app.route('/humidity')
def humidity():
    return render_template('humidity.html')

@app.route('/hello/<name>')
def hello(name):
    return render_template('page.html', name=name)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    
    
