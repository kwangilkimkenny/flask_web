from flask import Flask, jsonify, request, render_template

app = Flask(__name__) #Flask 모듈을 가져와서 app에 담아 인스턴스를 생성한다.



@app.route('/') #접속 URL
def home():
    return render_template('index.html')

stores = [
    {
        "name": "my store",
        "item":[
            {
            "name":"my item",
            "price": 15.99
            }
        ]
    }
]

# post - receive data
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store ={
        'name': request_data['name'],
        'items':[]
    }
    store.append(new_store)
    return jsonify(new_store)

# get - send data
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'store not found'})
# get - send data
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores })

@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            new_item ={
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'store not found'})


@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items':store['items']})
    return jsonify({'message': 'store not found'})

app.run(port=5000)