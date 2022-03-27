from flask import Flask, render_template
import json, os, requests

app = Flask(__name__)

url = "http://localhost:8888/apples/byWeight"

@app.route('/api', methods=['GET'])
def api_status():
    try:
        my_request = requests.get(url)
        my_status_code = my_request.status_code    
        
        if my_status_code == 200:
            decoded_contents = my_request.content.decode('UTF-8')
            json_contents = json.loads(decoded_contents)
    except Exception:
        my_status_code = '500'
        json_contents = ''
        print('Exception occured!')
    return render_template("index.html", status_code=my_status_code,
        contents=json_contents)
        

@app.route('/docs', methods=['GET'])
def api_docs():
    return render_template("docs.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5001)))
