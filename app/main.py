from app import app
import view
import os

host = os.getenv('IP','0.0.0.0')
port = int(os.getenv('PORT',8080))

if __name__ == '__main__':
    app.run(host=host,port=port, debug=True)
