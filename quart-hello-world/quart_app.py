"""

# prerequisites
pip install quart

# command to start the production like hypercorn server
 hypercorn quart_app:app --workers 12 --debug
"""

from quart import Quart, websocket
# import uvloop
# import asyncio

app = Quart(__name__)

# asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

@app.route('/')
async def hello_world():
    return {"message": "hello"}


if __name__ == "__main__":
    app.run()
