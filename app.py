from flask import flask

app= Flask(___name___)

@app.roue('/')
def home():
    return "Student Result System is Live and Running"
if __name__== '__main__':
    app.run(host='0.0.0', port=10000)