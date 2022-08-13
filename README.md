# herokuflask man page:
heroku git:remote -a appweb12ago
git commit -am 'is0' && git push heroku master && heroku restart && heroku logs --tail
heroku login
bind heroku app
https://appweb12ago.herokuapp.com/
heroku buildpacks:set heroku/python
git push heroku master

heroku open