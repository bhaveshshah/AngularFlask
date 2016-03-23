# Run a test server.
from app import app
from distutils.command.config import config

app.run(host='localhost', port=8055, debug=True)