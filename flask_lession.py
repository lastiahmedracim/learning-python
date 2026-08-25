from flask import Flask, render_template

skills_app = Flask("__name__")

my_skills = [("html", 80),("css", 65),("python",95),("MySql", 70)]

@skills_app.route("/")
def homepage():

    return render_template("homepage.html",
                            title="home",
                            custom_css="home")

@skills_app.route("/add")
def add():

    return render_template("add.html",
                            title="add", 
                            custom="add")

@skills_app.route("/skills")
def skills():

    return render_template("skills.html", 
                           title="skills", 
                           page_head="My skills", 
                           description="This is my skills", 
                           skills=my_skills,
                           custom_css="skills")

@skills_app.route("/about")
def aboutpage():

    return render_template("aboutpage.html",
                            title="about", 
                            custom_css="about")

if __name__ == "__main__":

    skills_app.run(debug=True, port=9000)