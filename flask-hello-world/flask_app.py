"""

# prerequisites
pip install flask
pip install uwsgi

# command to start the production like flask server
uwsgi --socket 0.0.0.0:5000 --protocol=http -w flask_app:app --processes=8 --enable-threads

"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return {"message": "hello"}


if __name__ == "__main__":
    app.run()