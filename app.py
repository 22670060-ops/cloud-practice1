from flask import Flask, jsonify, redirect
import datetime
import os

app = Flask(__name__)

# Redirigir la raíz a /status
@app.route('/')
def home():
    return redirect('/status')

@app.route('/status')
def status():
    return jsonify({
        "service": "demo-cloud", 
        "version": "1.0",
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z"
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
