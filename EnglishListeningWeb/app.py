from flask import Flask, render_template

app = Flask(__name__)

data = {
    1: ["Lesson 1", "Lesson 2", "Lesson 3"],
    2: ["Lesson 4", "Lesson 5"],
    3: ["Lesson 6"]
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/level/<int:level>")
def level_page(level):
    lessons = data.get(level, [])
    return render_template(
        "lessons.html",
        level=level,
        lessons=lessons
    )

@app.route("/lesson/<int:lesson_id>")
def lesson_page(lesson_id):
    return render_template(
        "lesson.html",
        lesson_id=lesson_id
    )
if __name__ == "__main__":
    app.run(debug=True)