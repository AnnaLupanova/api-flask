from flask import Flask, request, Response, jsonify, render_template
from pymongo import MongoClient
import json
from bson import json_util, ObjectId

app = Flask(__name__)

client = MongoClient('mongodb://root:pass@mongodb:27017')

db = client['demo']
collection = db['data']


@app.route('/add', methods=['POST'])
def add_data():
    data = dict(request.args)
    resp = list(collection.find(data))
    if resp:
        return Response('Object already exist', 400)
    collection.insert_one(data)
    return Response('Object created', 201)


@app.route('/', methods=['GET'])
def get_data():
    try:
        data = list(collection.find())
        print(data)
        data = json.dumps(data, default=json_util.default)
        return Response(data, 200)
    except Exception:
        return Response('Have error', 400)


@app.route('/<id>/edit', methods=['PUT'])
def update_data(id):
    data = dict(request.args)
    resp = list(collection.find({'_id': ObjectId(id)}))
    if resp:
        try:
            collection.update_one(
                {'_id': ObjectId(id)}, {'$set': data})
            return Response('Object updated', 200)
        except Exception:
            return Response('Have error', 400)
    return Response('Object not found', 404)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
