import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/actuate', methods=['POST'])
def actuate():
    data = request.json
    action = data.get("action")
    params = data.get("params")

    if action == "rename_folder":
        old_path = params.get("old_path")
        new_name = params.get("new_name")
        parent_dir = os.path.dirname(old_path)
        new_path = os.path.join(parent_dir, new_name)
        
        try:
            os.rename(old_path, new_path)
            return {"status": "success", "message": f"Renamed to {new_name}"}
        except Exception as e:
            return {"status": "error", "message": str(e)}
    return {"status": "ignored"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
