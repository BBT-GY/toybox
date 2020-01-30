import os
from flask import Flask
import os.path

if os.path.isfile("setenv.py"):
    print "I found it. I must be LOCAL"
    import setenv
else:
    print "I must be running in PWS"

app = Flask(__name__)

@app.route('/')
def mainmenu():

    return """
    <html>
    <body>
    <center><h1>This is dummy app to use MySQL</h1><br/>
    </body>
    </html>"""

if __name__ == "__main__":
	app.run(debug=False,host='0.0.0.0', port=int(os.getenv('PORT', '5000')))
