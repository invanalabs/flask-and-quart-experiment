"""

# prerequisites
pip install quart

# command to start the production like hypercorn server
hypercorn quart_app:app
"""

from quart import Quart, websocket

app = Quart(__name__)


@app.route('/')
async def hello_world():
    return {"message": "hello"}


if __name__ == "__main__":
    app.run()
