# Anime Search Engine
![image](https://user-images.githubusercontent.com/60008262/143714952-a18bd1d7-9126-4e45-937b-c80579b7cbdb.png)


## Project set up

**Prerequites:**

* python
* node.js

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

