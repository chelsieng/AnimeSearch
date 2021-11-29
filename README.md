# Anime Search Engine
![image](https://user-images.githubusercontent.com/60008262/143714952-a18bd1d7-9126-4e45-937b-c80579b7cbdb.png)

# Demo
#### 1. Enter keywords and filter search by Status, Genre or Source
![image](https://user-images.githubusercontent.com/60008262/143719610-147399cd-a19f-47fd-b68a-2e962156c6cd.png)

#### 2. See results
![image](https://user-images.githubusercontent.com/60008262/143719622-521eb035-c258-481a-8348-84ff5af96837.png)

## Project set up

**Prerequites:**

* [python](https://www.python.org/downloads/)
* [node.js](https://nodejs.org/en/download/)
* [elasticsearch](https://www.elastic.co/downloads/elasticsearch)
* [kibana](https://www.elastic.co/downloads/kibana)

### Set up elasticsearch index
1. Run elasticsearch
2. Run Kibana
3. Open Kibana at http://localhost:5601/app/home#/tutorial_directory
4. Go to "Upload file" tab
5. Drop file [animes.ndjson](server/data/animes.ndjson)
6. Click on Import
7. Set index name to animes
8. Click on Import again

### Set up python's virtual environment

```
$ virtualenv -p python3 venv
$ source venv/bin/activate
$ pip install -r server/requirements.txt
```

### Set up vue cli

```
$ sudo npm install -g @vue/cli
```

## How to run project

### Run server

```
$ cd server
$ python app.py 
```

### Run client

```
$ cd client
$ npm install
$ npm run serve
```

Vue server will be listening on http://localhost:8080/

