import sys
sys.path.insert(0, './app/')

from main import app
app.secret_key = 'saphirawasbondedtoeragon'

if __name__ == '__main__':
    app.run()
