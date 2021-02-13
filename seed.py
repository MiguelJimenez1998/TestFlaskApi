from flask import Flask

app = Flask(__name__)

@app.route('/test', methods=['GET'])
def test():
    return "hola"

if __name__ == '__main__':
    app.run(port=88)
