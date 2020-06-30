from flask import Flask, render_template, url_for
app = Flask(__name__)


abouts = [
    {
        'name': 'Elena Chegibaeva',
        'position': 'Co-founder'
    },
    {
        'name': 'Nazira Sheraly',
        'position': 'Co-founder'
    },
    {
        'name': 'Jazgul',
        'position': 'Coordinator'
    }
]


@app.route('/')
def main_page():
    return render_template('index.html')


@app.route('/news')
def news_page():
    return render_template()


@app.route('/about')
def about_page():
    return render_template()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="800")
