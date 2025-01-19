from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Initial state of the buckets
state = {"x": 8, "y": 0, "z": 0, "capacities": [8, 5, 3]}


@app.route("/")
def index():
    """
    Render the main page.
    """
    return render_template("index.html")


@app.route("/get_state")
def get_state():
    """
    API endpoint to get the current state of the buckets.
    """
    return jsonify(state)


@app.route("/pour", methods=["POST"])
def pour():
    """
    API endpoint to pour water from one bucket to another.
    """
    global state
    data = request.json
    from_bucket = data["from"]
    to_bucket = data["to"]

    # Current bucket levels
    buckets = [state["x"], state["y"], state["z"]]
    capacities = state["capacities"]

    # Calculate how much can be poured
    pour_amount = min(buckets[from_bucket], capacities[to_bucket] - buckets[to_bucket])
    buckets[from_bucket] -= pour_amount
    buckets[to_bucket] += pour_amount

    # Update the state
    state["x"], state["y"], state["z"] = buckets

    # Check for the goal
    is_goal = any(bucket == 4 for bucket in buckets)

    return jsonify({"success": True, "state": state, "goal": is_goal})


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=10000)
