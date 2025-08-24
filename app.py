from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/manifest.json")
def manifest():
    return app.send_static_file("manifest.json")

@app.route("/service-worker.js")
def service_worker():
    return app.send_static_file("service-worker.js")

if __name__ == "__main__":
    app.run(debug=True)


