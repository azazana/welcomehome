# Backend for site for pregnant women or people with small children.
API for welcome home site

for deploying

```
docker-compose -f docker-compose-deploy.yml up
```

override database
```
docker exec -it welcomehome-app-1 bash

python download_db.py
'''