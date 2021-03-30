from flask import Flask , jsonify , request , json

todos = [
    { "label": "Simple", "done": True },
]

@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = (request.data) #lo que envia fetch 
    print("Incoming request with the following body", request_body)
    decoded_object = json.loads(request_body) #transcribir de forma Decode el diccionario
    todos.append(decoded_object) #agrega la tarea nueva
    return (jsonify(todos)) #'Response for the POST todo'
 

 @app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
        delete = delete.query.get(1)
    db.session.delete(todos)
    db.session.commit()
    return delete_schema.(jsonify(todos))
    
# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)