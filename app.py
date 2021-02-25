from flask import Flask
from flask import jsonify
from flask import request
from flask import json

app = Flask(__name__)

gloceryItems=[{"gname": "Potato","gcost": "25$"},
	          {"gname": "Tomato","gcost": "20$"},
              {"gname": "Beans","gcost": "30$"},
              {"gname": "Carrot","gcost": "20$"}
              ]

@app.route('/', methods=['GET'])
def gloceryHome():
    return jsonify(gloceryItems)

@app.route('/gloceryItems', methods=['GET'])
def returnAllGlocery():
    gloceryItem = json.dumps(gloceryItems)
    print('gloceryItems ' +str(gloceryItems))
    return gloceryItem

@app.route('/gloceryItems/<string:name>', methods=['GET'])
def returnOneGlocery(name):
    oneGlocery = gloceryItems[0]
    for index, item in enumerate(gloceryItems):
        if item['gname']==name:
            oneGlocery = gloceryItems[index]
        else:
            abort(404, message=f"{q} is Not Available in the list ")
    return jsonify({'gloceryItems' : oneGlocery})


@app.route('/gloceryItems', methods=['POST'])
def addOne():
    new_gloceryItems = request.get_json(gloceryItems)
    gloceryItems.append(new_gloceryItems)
    return jsonify({'gloceryItems' : gloceryItems})

@app.route('/gloceryItems/<string:name>', methods=['PUT'])
def editOne(name):
    new_gloceryItems = request.get_json(gloceryItems)
    print('new' +new_gloceryItems)
    for i,q in enumerate(new_gloceryItems):
      if q['gname'] == name:
        new_gitems = new_gloceryItems[i]  
        gloceryItems.append(new_gitems)
      else:
          abort(404, message=f"{q} is Not Available in the list ")
    #gloceryItem = request.get_json(gloceryItems)
    return jsonify({'gloceryItems' : gloceryItems})
    

@app.route('/gloceryItems/<string:name>', methods=['DELETE'])
def deleteOne(name):
    for i,q in enumerate(gloceryItems):
      if q['gname'] == name:
        del gloceryItems[i]
      else:
          abort(404, message=f"{q} is Not Available in the list ")  
    return jsonify({'gloceryItems' : gloceryItems})

if __name__ == "__main__":
    app.run(debug=True)
