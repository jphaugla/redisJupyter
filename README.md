# redisJupyter
redis Jupyter notebooks covering redis concepts
## Initial project setup
Get this github code
```bash 
git clone https://github.com/jphaugla/redisJupyter.git
```
## docker compose startup
```bash
cd compose
docker-compose up -d --build
cd ..
```
### run the requirements script
```bash
docker exec -it jupyter bash -c "pip install -r demo/requirements.txt"
```
### open jupyter
http://localhost:8888
### open redisinsights
http://localhost:8001
