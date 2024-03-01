from flask import Flask

# Create a Flask application
app = Flask(__name__)

# Define a route that returns "Hello, Flask!"
@app.route('/')
def hello_flask():
    return 'Hello, Flask!'

if __name__ == '__main__':
    # Run the Flask application on localhost at port 5000
    app.run(debug=True)
