from flask import Flask, jsonify, request
import bestdori

app = Flask(__name__)


@app.route('/bestdori/check', methods=['GET', 'POST'])
def create_task():
    result = bestdori.tracker_data('291', '1000')
    return result


if __name__ == '__main__':
    app.run(debug=True)
