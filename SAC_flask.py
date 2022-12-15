from flask import Flask, render_template, request
from songartist_comp import get_songs

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    # Retrieve values from the two input fields
    input1 = request.form["input1"]
    input2 = request.form["input2"]

    # Calculate the result based on input values
    result = get_songs(input1, input2)
    
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run()
