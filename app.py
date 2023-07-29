from flask import Flask, render_template

app = Flask(__name__)
name = "M.Abhishekar"
title = "Web Developer"
about_me = "I'm a student at VBIT currently working in app development."
contact_info = {
    "email": "theabhishekar@gmail.com",
    "phone": "9704650854",
    "github": "https://github.com/theabhishekar",
    "linkedin": "https://www.linkedin.com/in/theabhishekar",
}

@app.route("/")
def index():
    return render_template("index.html", name=name, title=title)

@app.route("/about")
def about():
    return render_template("about.html", name=name, title=title, about_me=about_me)

@app.route("/contact")
def contact():
    return render_template("contact.html", name=name, title=title, contact_info=contact_info)

if __name__ == "__main__":
    app.run(debug=True)
