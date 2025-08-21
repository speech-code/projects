from flask import Flask, flash, redirect, render_template, request, session, url_for

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Replace with a strong secret key in production

# Dummy database for demonstration
users = {}
posts = []
followers = {}
likes = {}
comments = {}


# Helper function to get current user
def get_current_user():
    user_id = session.get("user_id")
    return users.get(user_id)


@app.route("/")
def index():
    if not get_current_user():
        return redirect(url_for("login"))

    current_user = get_current_user()
    followed_posts = []
    if current_user and current_user["username"] in followers:
        for post in posts:
            if (
                post["username"] in followers[current_user["username"]]
                or post["username"] == current_user["username"]
            ):
                followed_posts.append(post)
    else:
        # If no one is followed, show all posts (or implement a discovery feed)
        followed_posts = posts

    followed_posts.sort(key=lambda x: x["id"], reverse=True)  # Sort by most recent

    return render_template(
        "feed.html",
        posts=followed_posts,
        current_user=current_user,
        likes=likes,
        comments=comments,
    )


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        email = request.form["email"]
        username = request.form["username"]
        password = request.form["password"]

        if username in users:
            flash("Username already exists!", "danger")
            return redirect(url_for("signup"))

        users[username] = {"email": email, "username": username, "password": password}
        flash("Account created successfully! Please login.", "success")
        return redirect(url_for("login"))
    return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = users.get(username)
        if user and user["password"] == password:
            session["user_id"] = username
            flash("Logged in successfully!", "success")
            return redirect(url_for("index"))
        else:
            flash("Invalid username or password!", "danger")
    return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop("user_id", None)
    flash("Logged out successfully!", "info")
    return redirect(url_for("login"))


@app.route("/post", methods=["GET", "POST"])
def create_post():
    if not get_current_user():
        flash("Please login to create a post.", "warning")
        return redirect(url_for("login"))

    if request.method == "POST":
        caption = request.form["caption"]
        # In a real app, you would handle file uploads here
        # For now, we'll use a placeholder for the image URL
        image_url = "https://via.placeholder.com/300"

        post_id = len(posts) + 1
        posts.append(
            {
                "id": post_id,
                "username": get_current_user()["username"],
                "image_url": image_url,
                "caption": caption,
            }
        )
        flash("Post created successfully!", "success")
        return redirect(url_for("index"))
    return render_template("create_post.html")


@app.route("/profile/<username>")
def profile(username):
    user_posts = [post for post in posts if post["username"] == username]
    current_user = get_current_user()
    is_following = False
    if (
        current_user
        and current_user["username"] in followers
        and username in followers[current_user["username"]]
    ):
        is_following = True

    return render_template(
        "profile.html",
        user_posts=user_posts,
        profile_username=username,
        current_user=current_user,
        is_following=is_following,
        likes=likes,
        comments=comments,
    )


@app.route("/follow/<username>")
def follow(username):
    current_user = get_current_user()
    if not current_user:
        flash("Please login to follow users.", "warning")
        return redirect(url_for("login"))

    if username not in users:
        flash("User not found.", "danger")
        return redirect(url_for("index"))

    if current_user["username"] == username:
        flash("You cannot follow yourself.", "warning")
        return redirect(url_for("profile", username=username))

    if current_user["username"] not in followers:
        followers[current_user["username"]] = set()

    followers[current_user["username"]].add(username)
    flash(f"You are now following {username}!", "success")
    return redirect(url_for("profile", username=username))


@app.route("/unfollow/<username>")
def unfollow(username):
    current_user = get_current_user()
    if not current_user:
        flash("Please login to unfollow users.", "warning")
        return redirect(url_for("login"))

    if username not in users:
        flash("User not found.", "danger")
        return redirect(url_for("index"))

    if (
        current_user["username"] in followers
        and username in followers[current_user["username"]]
    ):
        followers[current_user["username"]].remove(username)
        flash(f"You have unfollowed {username}.", "info")
    return redirect(url_for("profile", username=username))


@app.route("/like/<int:post_id>")
def like_post(post_id):
    current_user = get_current_user()
    if not current_user:
        flash("Please login to like posts.", "warning")
        return redirect(url_for("login"))

    if post_id not in likes:
        likes[post_id] = set()

    likes[post_id].add(current_user["username"])
    flash("Post liked!", "success")
    return redirect(url_for("index"))


@app.route("/comment/<int:post_id>", methods=["POST"])
def add_comment(post_id):
    current_user = get_current_user()
    if not current_user:
        flash("Please login to comment.", "warning")
        return redirect(url_for("login"))

    comment_text = request.form["comment_text"]

    if post_id not in comments:
        comments[post_id] = []

    comments[post_id].append(
        {"username": current_user["username"], "text": comment_text}
    )
    flash("Comment added!", "success")
    return redirect(url_for("index"))


@app.route("/search", methods=["GET", "POST"])
def search_users():
    if request.method == "POST":
        query = request.form["query"].lower()
        search_results = [user for user in users if query in user.lower()]
        return render_template(
            "search_results.html", query=query, results=search_results
        )
    return render_template("search.html")


if __name__ == "__main__":
    app.run(debug=True)
