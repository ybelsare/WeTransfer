import random
import time

from flask import Flask

app = Flask(__name__)


@app.route('/success')
def success_endpoint():
    return {
               "msg": "Success.."
           }, 200


@app.route('/failure')
def faulty_endpoint():
    r = random.randint(0, 1)
    if r == 0:
        time.sleep(2)

    return {
               "msg": "Failure.."
           }, 500


@app.route('/random')
def fail_randomly_endpoint():
    r = random.randint(0, 1)
    if r == 0:
        return {
                   "msg": "Success..."
               }, 200

    return {
               "msg": "Failure..."
           }, 500


if __name__ == '__main__':
    app.run()
