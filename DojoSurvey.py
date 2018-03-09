# pylint: disable=print-statement

from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route("/")
def DojoSurvey():
    return render_template("DojoSurvey.html")

@app.route("/results", methods=["POST"])
def results():
    print "POST data"
    name = request.form["name"]
    dojolocations = request.form["dojolocations"]
    favoritelanguages = request.form["favoritelanguages"]
    comment =  request.form["comment"]
    print "Hello:", name, "Dojo Location:", dojolocations, "Favorite Language:", favoritelanguages, "Comment:", comment
    return render_template("/results.html", name = name, dojolocations = dojolocations, favoritelanguages = favoritelanguages, comment = comment)


app.run(debug=True)