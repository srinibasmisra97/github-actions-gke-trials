from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/", methods=['GET'])
def root():
    return jsonify({
        'success': True,
        'github_commit_id': "GITHUB_SHA"
    }), 200

if __name__=="__main__":
    app.run(host='0.0.0.0', port=8080, debug=False)