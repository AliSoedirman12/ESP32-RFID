from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/endpoint', methods=['POST'])
def receive_data():
    data = request.json
    print(f"Received data: {data}")

    # Process received UID
    if data and 'uid' in data:
        response = {
            'status': 'success',
            'uid_received': data['uid']
        }
    else:
        response = {
            'status': 'failed',
            'message': 'No UID received'
        }

    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)