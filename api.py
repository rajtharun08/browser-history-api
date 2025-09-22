from flask import Flask, request, jsonify
from browser_history.history import BrowserHistory
import os
import json

#name of our save file
HISTORY_FILE = "browser_history.json"
from browser_history.history import Node 

def save_history(history):
    """Saves the entire linked list and current position to a JSON file."""
    urls = []
    current_index = 0
    index = 0
    
    # Start at the beginning
    node = history.head
    
    # traverse
    while node:
        urls.append(node.url)
        if node == history.current_page:
            current_index = index
        
        node = node.next
        index += 1
        
    # Prepare the data- save
    data = {
        "history": urls,
        "current_index": current_index
    }
    
    # write the data to file
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def load_history():
    """Loads the history from the JSON file when the app starts."""
    if not os.path.exists(HISTORY_FILE):
        return BrowserHistory("homepage.com") 

    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        if not data["history"]:
            return BrowserHistory("homepage.com")

        # recreate BrowserHistory object
        homepage = data["history"][0]
        loaded_history = BrowserHistory(homepage)
        temp_node = loaded_history.head

        #  rest of the linked list
        for i in range(1, len(data["history"])):
            new_node = Node(data["history"][i])
            temp_node.next = new_node
            new_node.prev = temp_node
            temp_node = new_node
            
            # set the pointer
            if i == data["current_index"]:
                loaded_history.current_page = temp_node
        
        print(f"History loaded. Current page is: {loaded_history.current_page.url}")
        return loaded_history
         
    except (IOError, json.JSONDecodeError, KeyError):
        # file is empty
        print("Error loading history file. Starting fresh.")
        return BrowserHistory("homepage.com")
    
# Set up 
app = Flask(__name__)

history = load_history()
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
    
    save_history(history)
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