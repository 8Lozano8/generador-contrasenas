from flask import Flask, render_template, request
import secrets
import string

app = Flask(__name__)

def generate_password(length=12, use_symbols=True):
    # Caracteres básicos
    characters = string.ascii_letters + string.digits
    if use_symbols:
        characters += string.punctuation

    # Generar contraseña
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

@app.route("/", methods=["GET", "POST"])
def index():
    password = None
    if request.method == "POST":
        length = int(request.form.get("length", 12))
        use_symbols = "use_symbols" in request.form
        password = generate_password(length=length, use_symbols=use_symbols)

    return render_template("index.html", password=password)

if __name__ == "__main__":
    app.run(debug=True)
