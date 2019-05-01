from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>

      <!-- create your form here -->
      <form method="POST" >
        <label>
            Rotate by
            <input type="text" name="rot" value=0></input>
        </label>
            <textarea name="text">{0}</textarea>
            <input type="submit" value="Submit">
      </form>

    </body>
</html>
 """

@app.route("/")
def index():
    return form.format(...)

@app.route("/", methods=["POST"])
def encrypt():
    rotation = int(request.form["rot"])
    input_text = request.form["text"]
    encrypted = rotate_string(input_text, rotation)
    return form.format(encrypted)
#The request forms gets the information from their respected tags that have those names.
#In order for the "form.format" to work properly with CSS make sure the the curely brances are doubled.

app.run()