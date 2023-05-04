from flask import send_from_directory


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run(debug=True)
