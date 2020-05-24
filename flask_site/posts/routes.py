from flask import (Blueprint, request, render_template, 
                   url_for, flash, abort, redirect)
from flask_login import current_user, login_required
from flask_site.models import Post
from flask_site.posts.forms import PostForm
from flask_site import db

posts = Blueprint('posts', __name__)


@posts.route('/post/new', methods=['GET','POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title= form.title.data, content= form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash("Your post has been created!", 'success')
        return redirect(url_for('main.home_page'))
    return render_template('create_post.html', title='New Post',
                        form=form, legend="Create a new Post")


@posts.route("/post/<int:post_id>")
def view_post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)


@posts.route("/post/<int:post_id>/update", methods=['GET','POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash("Your post has been updated!", 'success')
        return redirect(url_for('main.home_page'))
    elif request.method == 'GET': 
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title='Upate Post',
                           form=form, legend="Update Post")


@posts.route("/post/<int:post_id>/delete", methods=['GET','POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('main.home_page'))


@posts.route('/user/<string:username>', methods=['GET','POST'])
def user_posts(username):
    page = request.args.get('page',default=1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(author=user)\
        .order_by(Post.date_posted.desc())\
        .paginate(page=page, per_page=10)
    return render_template('user_post.html', posts=posts, user=user)