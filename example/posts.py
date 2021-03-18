from flask import render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort

from main import app, db


class Posts(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, server_default=db.func.now())
    title = db.Column(db.String())
    content = db.Column(db.String())

    def __init__(self, title, content):
        self.title = title
        self.content = content


def get_post(post_id):
    post = db.session.query(Posts).get(post_id)
    if post is None:
        abort(404)
    return post


@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            db.session.add(Posts(title=title, content=content))
            db.session.commit()
            return redirect(url_for('index'))

    return render_template('create.html')


@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    from comments import get_comments
    return render_template('post.html', post=post, comments=get_comments(post_id))


@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            post.title = title
            post.content = content
            db.session.commit()
            return redirect(url_for('index'))

    return render_template('edit.html', post=post)


@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    post = get_post(id)
    db.session.delete(post)
    db.session.commit()
    flash('"{}" was successfully deleted!'.format(post.title))
    return redirect(url_for('index'))


@app.route('/')
def index():
    posts = db.session.query(Posts).all()
    from comments import get_comment_counts

    return render_template('index.html', posts=posts, comment_counts=get_comment_counts())
