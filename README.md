# herokuflask man page:
APP name: appweb12ago

heroku git:remote -a appweb12ago
git commit -am 'is0 ' && git push && heroku restart
heroku logs --tail
heroku login
bind heroku app
https://appweb12ago.herokuapp.com/
heroku buildpacks:set heroku/python
git push heroku master

heroku open
Flask:
<pre>
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True)
</pre>