from flask import Flask, render_template, url_for
app = Flask(__name__)
home_data = {
    "page_title": "My Blog",
    "main_article_title": "Hacking in the Modern Age: A Guide to Modern Tools" 
}
@app.route("/")
def hello():
    title = "My Blog"
    return render_template("index.html", data=home_data)

if __name__ == "__main__":
    app.run(debug=True)