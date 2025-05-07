from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    print("Request:", req)

    intent = req.get('queryResult').get('intent').get('displayName')

    if intent == "Your Intent Name":
        return jsonify({'fulfillmentText': 'Your response text'})

    return jsonify({'fulfillmentText': 'Fallback response'})

if __name__ == '__main__':
    app.run(port=5000)
