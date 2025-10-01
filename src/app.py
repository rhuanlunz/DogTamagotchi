from flask import Flask

app = Flask(__name__)

@app.route("/api/dog/show_status", methods=["GET"])
def show_dog_status():
    return "show status"

@app.route("/api/dog/wake_up", methods=["GET"])
def wake_up_dog():
    return "wake up"

@app.route("/api/dog/feed", methods=["GET"])
def feed_dog():
    return "feed"

@app.route("/api/dog/play", methods=["GET"])
def play_with_dog():
    return "play"

@app.route("/api/dog/sleep", methods=["GET"])
def sleep_dog():
    return "sleep"

if __name__ == "__main__":
    app.run(debug=True)
