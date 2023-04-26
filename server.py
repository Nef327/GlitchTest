from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    title = "Клуб любителей помидор"
    return render_template('index.html', title=title)


@app.route("/training/<prof>")
def training(prof):
    title = "Клуб любителей помидор"
    return render_template('training.html', title=title, prof=prof)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')