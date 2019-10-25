from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/yogurt')
def yogurt():
    return 'Frozen yogurt my favourite!'

@app.route('/chocolateBrownies')
def chocolateBrownies():
    return render_template('chocolateBrownies.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')