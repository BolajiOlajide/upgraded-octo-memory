from flask import Flask, jsonify


app = Flask(__name__)

@app.route("/")
def read_root():
    return jsonify({"Hello": "World"})


# @app.route("/items/{item_id}")
# def read_item(item_id: int, q: str = None):
#     return {"item_id": item_id, "q": q}

if __name__ == "__main__":
    app.run()
