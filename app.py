from flask import Flask, request, redirect, render_template, url_for
import uuid

app = Flask(__name__)

# Dictionary to store messages by user IDs
confessions = {}


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/create', methods=['POST'])
def create_link():
    user_id = str(uuid.uuid4())  # Generate a unique ID
    confessions[user_id] = []  # Create an empty list for storing messages
    return redirect(url_for('view_messages', user_id=user_id))


@app.route('/<user_id>', methods=['GET', 'POST'])
def view_messages(user_id):
    if user_id not in confessions:
        return "Invalid link!", 404

    if request.method == 'POST':
        message = request.form.get('message')
        if message:
            confessions[user_id].append(message)

    return render_template('confession_page.html', user_id=user_id, messages=confessions[user_id])


if __name__ == '__main__':
    app.run(debug=True)
