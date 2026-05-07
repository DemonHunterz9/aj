from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

score = {
    "team1":"India",
    "team2":"Australia",
    "runs":0,
    "wickets":0,
    "balls":0
}

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/score")
def get_score():
    return jsonify(score)


@app.route("/update", methods=["POST"])
def update_score():
    data = request.get_json()

    runs = int(data.get("runs",0))
    wicket = data.get("wicket",False)

    score["runs"] += runs

    if wicket:
        score["wickets"] += 1
    else:
        score["balls"] += 1

    return jsonify({"status":"success"})


@app.route("/teams", methods=["POST"])
def teams():
    data=request.get_json()

    if data.get("team1"):
        score["team1"]=data["team1"]

    if data.get("team2"):
        score["team2"]=data["team2"]

    return jsonify({"status":"updated"})


@app.route("/reset", methods=["POST"])
def reset():
    score["runs"]=0
    score["wickets"]=0
    score["balls"]=0
    return jsonify({"status":"reset"})


if __name__=="__main__":
    app.run(debug=True)