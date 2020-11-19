from app import manager
from app import app as application
from app.settings import APP_PORT, APP_HOST

if __name__ == "__main__":
    manager.run()
    application.run(host=APP_HOST, port=APP_PORT)