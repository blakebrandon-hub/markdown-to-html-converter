from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__, static_folder='static')
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

# Optional: Redirect to static readme if needed
@app.route('/readme')
def serve_readme():
    return app.send_static_file('readme_sample.md')

if __name__ == '__main__':
    app.run(debug=True)
