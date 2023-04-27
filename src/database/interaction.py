from .connection import (
    connect,
    create_database
)

client = connect(
    "mongodb+srv://rakshithalijol:Rakshithalijol123@cluster0.xuaevf5.mongodb.net/test")
db = create_database(client=client, db_name="TEST-DATABASE")


# --- Create your collections here ---
User = db["User"]

# Write functions which interact with database


def create_user(userData: dict) -> str:
    user = User.insert_one(userData)
    return str(user.inserted_id)
