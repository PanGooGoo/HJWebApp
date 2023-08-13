
from flask import Flask, render_template, request
import pandas as pd
import os
import time

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    if request.method == "POST":
        file = request.files["file"]
        is_param_one = request.form['is_param_one']
        df = pd.read_csv(file)
        filename = time.strftime("%Y%m%d%H%M%S") + ".csv"
        df.to_csv(os.path.join(os.getcwd(), "staticFiles", filename))
        db = df[str(is_param_one)]
        return render_template("show_data.html", DataFrame=db)

if __name__ == "__main__":
    app.run(debug=True)
