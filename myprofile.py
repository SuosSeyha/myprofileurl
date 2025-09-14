from flask import Flask, render_template
import requests

app = Flask(__name__)

# GitHub raw JSON link (replace with your repo link)
GITHUB_PROFILE_URL = "https://raw.githubusercontent.com/SuosSeyha/profileme/main/profile.json"

def fetch_profile():
    try:
        response = requests.get(GITHUB_PROFILE_URL)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print("⚠️ Error fetching profile:", e)
        # fallback in case GitHub fails
        return {
            "name": "Error User",
            "bio": "Could not fetch profile",
            "avatar": "https://via.placeholder.com/150",
            "links": []
        }

@app.route("/")
def home():
    profile = fetch_profile()
    return render_template("index.html", profile=profile)

if __name__ == "__main__":
    app.run()
