from flask import Flask, request, send_from_directory


app = Flask(__name__)

@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run(debug=True)
