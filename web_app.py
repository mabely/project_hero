from flask import Flask, render_template, request
import main

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
    return render_template('pages/index.html')

@app.route('/about')
def about():
    return render_template('pages/about.html')

@app.route('/contact')
def contact():
    return render_template('pages/contact.html')

@app.route('/properties', methods=['GET'])
def properties_get():
    properties = main.return_db()
    return render_template('pages/properties.html', properties=properties)

# @app.route('/properties', methods=['POST'])
# def properties_post():
#     return render_template('pages/properties.html')

if __name__ == '__main__':
    app.run()
