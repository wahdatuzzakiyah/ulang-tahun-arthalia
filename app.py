from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/puisi')
def puisi():
    return send_from_directory('static', 'puisi.pdf')

if __name__ == '__main__':
    app.run(debug=True)