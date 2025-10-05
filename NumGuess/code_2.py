import pickle

print("Hello, what is your name?")
username = input(" > ").strip()
user_file = f"{username}.dat"           # per-user file

# try load per-user data (dict with name/highscore/lastscore)
try:
    with open(user_file, "rb") as file:
        data = pickle.load(file)
    print(f"Welcome back, {data.get('name', username)}!")
except FileNotFoundError:
    print(f"Nice to meet you, {username}!")
    data = {"name": username, "highscore": 0, "lastscore": 0}
    with open(user_file, "wb") as file:
        pickle.dump(data, file)

# show scores
print(f"High score:  {data['highscore']}")
print(f"Your score: {data['lastscore']}")

# --- game runs here, produce new scores ---
# example: new scores from game
new_high = 10
new_last = 20

# update and save back to the same per-user file
data["lastscore"] = new_last
if new_high > data["highscore"]:       # or use lower-is-better logic if needed
    data["highscore"] = new_high

with open(user_file, "wb") as file:
    pickle.dump(data, file)