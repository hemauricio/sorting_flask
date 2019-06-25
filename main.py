from flask import Flask, request, jsonify

app = Flask("sorting_flask")

@app.route("/")
def hello():
    return "Hello, World!\n"

@app.route("/quicksort", methods=["POST"])
def quicksort():
    return jsonify({
        "data":{
            "original":request.json,
            "sorted":request.json # Temporal
        }
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True, threaded=True)
