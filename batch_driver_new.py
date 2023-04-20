import json
from flask import Flask, jsonify
app = Flask(_name_)
@app.route('/', methods=['GET'])
def query_records():
    name = request.args.get('name')
    return jsonify({'name':name})

app.run(debug=True)
