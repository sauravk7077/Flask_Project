from flask import Blueprint, render_template, request
from flask_site.models import Post

main = Blueprint('main', __name__)


@app.route('/')
@app.route('/home')
def home_page():
    page = request.args.get('page',default=1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=10)
    return render_template('home.html', posts=posts)


@app.route('/about')
def about_page():
    return render_template('about.html', title='About')