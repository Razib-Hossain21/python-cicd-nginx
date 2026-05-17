from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello Mr. Razib, you have successfully deployed. Congratulations..! Python App Running Through NGINX + Docker + Jenkins CI/CD"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
