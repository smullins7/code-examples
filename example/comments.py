from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
import sqlite3

from main import app


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def db_get_comment(comment_id):
    conn = get_db_connection()
    comment = conn.execute('SELECT * FROM comments WHERE id = ?',
                        (comment_id,)).fetchone()
    conn.close()
    if comment is None:
        abort(404)
    return comment

@app.route('/comments/<int:comment_id>')
def get_comment(comment_id):
    comment = db_get_comment(comment_id)
    return render_template('comment.html', comment=comment)


def get_comments(post_id):
    conn = get_db_connection()
    comments = conn.execute('SELECT * FROM comments where post_id = ?', (post_id, )).fetchall()
    conn.close()
    return comments

def get_comment_counts():
    conn = get_db_connection()
    rows = conn.execute('SELECT post_id, count(*) FROM comments').fetchall()
    counts_by_post_id = dict([(r[0], r[1]) for r in rows])
    conn.close()
    return counts_by_post_id