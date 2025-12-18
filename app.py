from flask import Flask, render_template, session, redirect
import json, random, qrcode, io, base64

app = Flask(__name__)
app.secret_key = "hitster-kids-secret"  # nodig voor session

with open("songs.json", "r") as f:
    SONGS = json.load(f)

def generate_qr(url):
    qr = qrcode.make(url)
    buf = io.BytesIO()
    qr.save(buf)
    buf.seek(0)
    return base64.b64encode(buf.getvalue()).decode()

@app.route("/")
def index():
    song = random.choice(SONGS)
    session["song"] = song

    qr_base64 = generate_qr(song["spotify_track_url"])
    return render_template(
        "index.html",
        qr=qr_base64,
        song=None
    )

@app.route("/reveal")
def reveal():
    song = session.get("song")
    qr_base64 = generate_qr(song["spotify_track_url"])
    return render_template(
        "index.html",
        qr=qr_base64,
        song=song
    )

@app.route("/next")
def next_song():
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

