from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return "I am Flask,Hello World!"

@app.route('/<par>')
def home(par):
    return(f'i am {par}')
if __name__ == '__main__':
    app.run(debug=True)
