"""

# prerequisites
pip install quart

# command to start the production like flask server
uwsgi --socket 0.0.0.0:5000 --protocol=http -w flask_app:app

"""

from quart import Quart, websocket

app = Quart(__name__)


@app.route('/')
async def hello_world():
    return {"message": "hello"}


@app.websocket('/ws')
async def ws():
    while True:
        await websocket.send('hello')


if __name__ == "__main__":
    app.run()
