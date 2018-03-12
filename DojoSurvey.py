# pylint: disable=print-statement

from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = "Secret"

@app.route("/", methods = ["GET"])
def DojoSurvey():
    return render_template("DojoSurvey.html")

@app.route("/results", methods=["POST"])
def results():
    print "POST data"
    if len(request.form["name"]) < 1 and len(request.form["comment"]) < 1:
        flash("Name cannot be Blank!")
        flash("Please enter a Comment!")
        return redirect("/")
    elif len(request.form["name"]) < 1:
        flash("Name cannot be Blank!")
        return redirect("/")
    elif len(request.form["comment"]) < 1:
        flash("Comment cannot be Blank!")
        return redirect("/")
    else:
        flash("Kudos for entering your name!")
    name = request.form["name"]
    dojolocations = request.form["dojolocations"]
    favoritelanguages = request.form["favoritelanguages"]
    if len(request.form["comment"]) > 120:
        flash("Comment cannot not be longer than 120 characters. Please shorten your comment")
        return redirect("/")
    else:
        flash("Thank you for your comment!")
    comment =  request.form["comment"]
    print "Hello:", name, "Dojo Location:", dojolocations, "Favorite Language:", favoritelanguages, "Comment:", comment
    return render_template("/results.html", name = name, dojolocations = dojolocations, favoritelanguages = favoritelanguages, comment = comment)


app.run(debug=True)