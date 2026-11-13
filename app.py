from flask import Flask

app= Flask(___name___)

@app.route('/')
def home():
    return "Student Result System is Live and Running"
if __name__== '__main__':
    app.run(host='0.0.0', port=10000)