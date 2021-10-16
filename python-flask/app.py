from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app) 

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(20), nullable=False, default='N/A')
    data_posted = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return "Blog Post " + str(self.id)
        

# all_posts = [
#         {
#             'title': 'Why do we use it?',
#             'content': 'It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout.'
#         },
#         {
#             'title': 'Where can I get some?',
#             'content': 'There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomice words which don\'t look even slightly believable.',
#             'author': 'lipsum.com'
#         }
#         ]

@app.route('/')
def index():
    return  render_template('index.html')

@app.route('/posts', methods=['GET', 'POST'])
def posts():
    if request.method == 'POST':
        post_title = request.form['title']
        post_content = request.form['content']
        post_author = request.form['author']
        new_post = BlogPost(title=post_title, content=post_content, author=post_author)
        db.session.add(new_post)
        db.session.commit( )
        return redirect('/posts')
    else:
        all_posts = BlogPost.query.order_by(BlogPost.data_posted).all()
        return render_template('posts.html', posts=all_posts)

@app.route('/posts/delete/<int:id>')
def delete_post(id):
    post = BlogPost.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    print(post.title + " Deleted")
    return redirect('/posts')
 
@app.route('/posts/edit/<int:id>', methods=['GET', 'POST'])
def edit_post(id):
    post = BlogPost.query.get_or_404(id)
    print(post.author)

    if request.method == 'POST':
        post.title = request.form['title']
        post.content = request.form['content']
        post.author = request.form['author']
        print(post.author + " IF")
        db.session.commit()
        return redirect('/posts')
    else:
        print(post.author + " ELSE")
        return render_template('edit.html', post=post) 


@app.route('/home/user/<string:name>/<int:id>')
def hello(name, id):
    return "Hello World, " + name + " the id is: " + str(id)

@app.route('/get', methods=['GET'])
def get_request():
    return "You only can get this webpage."

if __name__ == "__main__":
    app.run(host= "localhost", port=8000, debug=True)