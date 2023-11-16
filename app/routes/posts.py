from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from app import db
from app.models import Post
from app.forms import PostForm

posts = Blueprint('posts', __name__)

@posts.route('/create', methods=['GET', 'POST'])
@login_required
def create_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Post created successfully!', 'success')
        return redirect(url_for('index'))

    return render_template('posts/create_post.html', form=form)

@posts.route('/<int:post_id>')
def view_post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('posts/view_post.html', post=post)

@posts.route('/edit/<int:post_id>', methods=['GET', 'POST'])
@login_required
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)

    # Ensure that only the author of the post can edit it
    if current_user != post.author:
        flash('You are not authorized to edit this post.', 'danger')
        return redirect(url_for('posts.view_post', post_id=post.id))

    form = PostForm()

    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Post updated successfully!', 'success')
        return redirect(url_for('posts.view_post', post_id=post.id))

    # Pre-fill the form with the existing post data
    form.title.data = post.title
    form.content.data = post.content

    return render_template('posts/edit_post.html', form=form, post=post)

@posts.route('/delete/<int:post_id>', methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)

    # Ensure that only the author of the post can delete it
    if current_user != post.author:
        flash('You are not authorized to delete this post.', 'danger')
        return redirect(url_for('posts.view_post', post_id=post.id))

    db.session.delete(post)
    db.session.commit()
    flash('Post deleted successfully!', 'success')

    # You can redirect to a specific page after deletion
    return redirect(url_for('index'))