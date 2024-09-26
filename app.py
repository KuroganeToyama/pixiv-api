from flask import Flask, jsonify, request
from tag_map import *
from fetch import fetch_url

app = Flask(__name__)
    
@app.route('/image', methods=['GET'])
def image():
    tag = request.args.get('tag')
    if not tag:
        return jsonify({"error": "tag is required"}), 400
    if tag not in TAG_DICT:
        return jsonify({"error": "tag not found"}), 404

    try:
        pixiv_url = fetch_url(tag)
        data = {"url": pixiv_url}
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
if __name__ == "__main__":
    app.run(debug = True)