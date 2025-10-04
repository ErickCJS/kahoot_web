from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # O puedes usar return "Hola Flask"

if __name__ == '__main__':
    app.run(debug=True)
