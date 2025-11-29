from flask import Flask, request, render_template_string

app = Flask(__name__)

# Example "database"
DATA_TABLE = {
    "123": "Apple",
    "456": "Banana",
    "789": "Orange"
}

HTML = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Password Lookup</title>
  <style>
    body { font-family: system-ui, -apple-system, Roboto, Arial; padding: 2rem; max-width: 600px; margin: auto; }
    input[type="text"] { padding: .6rem; font-size: 1rem; width: 60%; }
    button { padding: .6rem 1rem; font-size: 1rem; margin-left: .5rem; }
    .result { margin-top: 1.25rem; font-weight: 600; }
    .error { margin-top: 1.25rem; color: #b00020; font-weight: 700; }
  </style>
</head>
<body>
  <h1>Password Lookup</h1>
  <form method="post" action="/check">
    <label for="password">Enter password (string):</label><br/>
    <input id="password" name="password" type="text" required autocomplete="off" />
    <button type="submit">Submit</button>
  </form>

  {% if result %}
    <div class="result">Your word is: {{ result }}</div>
  {% elif error %}
    <div class="error">{{ error }}</div>
  {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET"])
def index():
    return render_template_string(HTML)

@app.route("/check", methods=["POST"])
def check():
    pwd = (request.form.get("password") or "").strip()
    if not pwd:
        return render_template_string(HTML, error="Please enter a password.")
    if pwd in DATA_TABLE:
        return render_template_string(HTML, result=DATA_TABLE[pwd])
    return render_template_string(HTML, error="Incorrect password")

if __name__ == "__main__":
    # Development server (not used on Render)
    app.run(host="0.0.0.0", port=5000, debug=True)
