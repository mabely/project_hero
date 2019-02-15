from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('pages/index.html')

@app.route('/properties', method='GET')
def properties_get():
    return render_template('pages/properties.html')

@app.route('/properties', method='POST')
def properties_post():
    return render_template('pages/properties.html')

if __name__ == '__main__':
    app.run()
