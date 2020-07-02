"""
Update this file with your own info and remove ".example" from the file name.
"""

from fbchat import User, Group

# User(s) to monitor
monitored_users = ["test_user1", "test_user2"]
# Thread to notify on new posts/comments
thread_id = "1234567890"
# Type of chat given above by thread_id (change this to Group for group chats)
receiver_type = User
# User agent used to request data from Reddit (won't work unless spoofing a browser)
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
# Path to file where most recent post IDs will be stored to determine when new ones have been posted
stored_filename = "history.pickle"
# Time in seconds to wait between checks of the user's account (shouldn't need to do this too often)
sleep_interval = 60