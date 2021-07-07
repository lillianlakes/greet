# Put your app in here.

from flask import Flask

app = Flask(__name__)

@app.route('/welcome')

def say_welcome():
    """Return simple 'Welcome' greeting"""

    html = """<html>
                    <body>
                        <h1>Welcome</h1>
                    </body>
                </html>"""

    return html

@app.route('/welcome/<word>')
def say_welcome_with_word(word):
    """Return simple 'Welcome' greeting with custom word"""

    html = f"""<html>
                    <body>
                        <h1>Welcome {word}</h1>
                    </body>
                </html>"""

    return html