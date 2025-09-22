from flask import Flask, request, jsonify
from browser_history.history import BrowserHistory

# Set up 
app = Flask(__name__)

# single instance of our browser history
history = BrowserHistory("homepage.com")
print("API is up, history is initialized.")

# 3. Define our API routes (endpoints)

@app.route("/visit", methods=["POST"])
def visit_page():
    """
    Visits a new page
    Expects a JSON body like: {"url": "google.com"}
    """
    # Get the JSON data from the request
    data = request.get_json()

    if not data or "url" not in data:
        return jsonify({"error": "Missing 'url' in JSON body"}), 400

    url_to_visit = data["url"]
    history.visit(url_to_visit)

    return jsonify({
        "message": "Page visited successfully",
        "current_page": url_to_visit
    }), 200

@app.route("/back", methods=["GET"])
def go_back():
    """
    goes back in history
    expects a query parameter like: /back?steps=1
    """
    # Get the steps from URL (e.g., /back?steps=2)
    steps_str = request.args.get("steps", default="1")

    try:
        steps = int(steps_str)
    except ValueError:
        return jsonify({"error": "'steps' must be an integer"}), 400

    new_url = history.back(steps)

    return jsonify({
        "message": f"Moved back {steps} step(s).",
        "current_page": new_url
    })

@app.route("/forward", methods=["GET"])
def go_forward():
    """
    goes forward in history
    expects a query parameter like: /forward?steps=1
    """
    steps_str = request.args.get("steps", default="1")

    try:
        steps = int(steps_str)
    except ValueError:
        return jsonify({"error": "'steps' must be an integer"}), 400

    new_url = history.forward(steps)

    return jsonify({
        "message": f"Moved forward {steps} step(s).",
        "current_page": new_url
    })

@app.route("/current", methods=["GET"])
def get_current_page():
    """
    simple endpoint to check the current page
    """
    return jsonify({
        "current_page": history.current_page.url
    })


#run the app
if __name__ == "__main__":
    # debug=True  = auto-reload when you save the file
    app.run(debug=True, port=5000)