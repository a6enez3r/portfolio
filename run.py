import sys
sys.path.insert(0, './app/')

from main import app
import config

app.config.from_object('config.ProductionConfig')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4999)
