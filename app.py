from flask import Flask, render_template
# import socket
# socket.getaddrinfo('localhost', 8080)

app = Flask(__name__)

@app.route("/")
def helloWorld():
    return render_template('home.html')

if __name__=='__main__':
    app.run(host='127.0.0.0',debug= True)