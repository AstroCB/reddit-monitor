# External deps
import fbchat
import requests

# Stdlib deps
import json
import pickle
import os
import time

# Local deps
from config import *

def login():
    try:
        with open("session.txt", "r") as session:
            session_cookies = json.loads(session.read())
    except FileNotFoundError:
        session_cookies = None

    session = fbchat.Session.from_cookies(session_cookies)
    with open("session.txt", "w") as session_file:
        session_file.write(json.dumps(session.get_cookies()))

    return session

def send_msg(msg):
    session = login()
    thread = receiver_type(session=session, id=thread_id)
    thread.send_text(msg)

def get_latest_post(username):
    url = f"https://www.reddit.com/user/{username}.json"
    res = requests.get(url, headers={
        "User-Agent": user_agent
    })

    if res.status_code == 200:
        data = res.json()
        posts = data["data"]["children"]
        return posts[0]

def get_pickled_data():
    if os.path.exists(stored_filename):
        with open(stored_filename, "rb") as f:
            return pickle.load(f)

    return {}

def pickle_data(user, latest_id):
    data = get_pickled_data()
    data[user] = latest_id
    
    with open(stored_filename, "wb") as f:
        pickle.dump(data, f)
    
def notify(user, latest):
    post_data = latest["data"]

    # Extract the post data
    is_comment = (latest["kind"] == "t1")
    post_type = "comment" if is_comment else "post"
    link = f"https://reddit.com{post_data['permalink']}"
    title_sep = " in " if is_comment else ": "
    title = post_data["link_title"] if is_comment else post_data["title"]
    content_sep = ":" if is_comment else ""
    content = post_data["body"] if is_comment else ""
    
    # Insert > at the beginning of every line to quote
    quoted_content = "\n> ".join(content.split("\n"))
    body = f"> {quoted_content}\n" if is_comment else ""
    
    # Send the notification message
    send_msg(f"New {post_type} from {user}{title_sep}\"{title}\"{content_sep}\n{body}\n{link}")

def check_and_notify():
    stored_data = get_pickled_data()
    for user in monitored_users:
        print(f"Checking for new posts from {user}...")
        stored_id = stored_data.get(user)
        latest = get_latest_post(user)
        latest_id = latest["data"]["id"]

        if stored_id != latest_id:
            # Update id in data store and notify if user already exists
            # (if it doesn't, probably the first time running the script)
            if stored_id is not None:
                notify(user, latest)
            pickle_data(user, latest_id)

while True:
    check_and_notify()
    time.sleep(sleep_interval)