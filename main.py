from flask import Flask
import requests
import os


app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    """try:
        if requests.get('http://internal.dest-project.delfos').status_code == 200:
            return 'Request arrived to the destination project'
        else:
            return f'Error. Response with status code != 200'
    except:
        return 'Error. DNS not found'"""
    resp = f"""Hello, World. This is a Delfos app! V1
    Checking some environment variables...
    * ENV: {os.getenv('ENV')}
    * VERSION: {os.getenv('VERSION')}"""
    return resp


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)

