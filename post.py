from flask import Flask, request 
import json

app = Flask(__name__)

@app.route('/test', methods=['POST'])
def post():
    try:
        string_to_cut = request.json['string_to_cut']
    except:
        print('POST failure')
    result = parse_string(string_to_cut)
    return_json = {
        "return_string": result,
    }
    return json.dumps(return_json)

def parse_string(string):
    i = 0
    new_string = []
    for char in string:
        i += 1
        if i % 3 == 0:
            new_string.append(char)
    return "".join(new_string)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
