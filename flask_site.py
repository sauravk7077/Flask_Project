from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author':'Saurav',
        'title':'My travel',
        'content':'first post content',
        'date_posted':'April 20, 2020'
    },
    {
        'author':'Joe',
        'title':'Other doc',
        'content':'First post content',
        'date_posted':'April 20, 2017'
    }
]

@app.route('/')
@app.route('/home')
def hello_world():
    return render_template('home.html',posts=posts)


@app.route('/about')
def about_page():
    return render_template('about.html', title='About')


if __name__ == "__main__":
    app.run(debug=True)