# herokuflask
bind heroku app
git commit -am 'is0' && git push heroku master && heroku restart && heroku logs --tail

https://appweb12ago.herokuapp.com/
heroku buildpacks:set heroku/python
git push heroku master
heroku git:remote -a appweb12ago
heroku login
