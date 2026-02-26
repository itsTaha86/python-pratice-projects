from flask import Flask, render_template, request, redirect, url_for
import uuid
import json
import os


data_path = "form-web/data/users_data.json"


def load_data():
    if os.path.exists(data_path):
        try:
            with open(data_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    else:
        return []


users_data = load_data()

app = Flask(__name__, template_folder="templates")


@app.route("/", methods=["GET"])
def index():

    return render_template("index.html", users=users_data)


@app.route("/submit", methods=["POST"])
def get_data():
    id = str(uuid.uuid4())
    name = request.form.get("name")
    age = request.form.get("age")
    interest = request.form.get("interest")
    level = request.form.get("level")
    description = request.form.get("description")

    if name and age.isdigit():
        users_data.append(
            {
                "id": id,
                "name": name,
                "age": age,
                "interest": interest,
                "level": level,
                "description": description,
            }
        )

    with open(data_path, "w") as f:
        json.dump(users_data, f, indent=4)

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
