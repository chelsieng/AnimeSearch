from flask import Flask, request
from flask_cors import CORS, cross_origin
from elasticsearch import Elasticsearch
import json

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
es = Elasticsearch(HOST="http://localhost", PORT=9200)


@app.route('/hello')
@cross_origin()
def hello_world():  # put application's code here
    return "Hello World!"


@app.route('/search/<words>', methods=['GET'])
@cross_origin()
def searchAnime(words):
    if words == "":
        return
    else:
        query = {"multi_match": {
            "query": words,
            "fields": ["description", "English Title", "Japanese Title"]
        }}
        res = es.search(index="animes", query=query)
        print("Got %d Hits:" % res['hits']['total']['value'])
        hits = []
        for hit in res['hits']['hits']:
            hits.append(hit["_source"])
            # print(hit["_source"])
        # print(hits)
        response = app.response_class(
            response=json.dumps(hits),
            mimetype='application/json'
        )
    return response


def checkAndGetNumber(num):
    if str(num).isdigit and str(num) != "Unknown" and str(num) != "/A":
        return int(num)
    else:
        return 0


@app.route('/initialize_data')
def connect_elastic():
    if es.indices.exists(index="animes"):
        es.indices.delete(index="animes")
    es.indices.create(index="animes")
    with open('data/anime_data.json', 'r') as f:
        print(f.readlines())
        data = json.load(f)
    for i in range(0, len(data)):
        anime_ID = data[i]["anime_ID"]
        jap_title = data[i]["Japanese Title"]
        eng_title = data[i]["English Title"]
        image_url = data[i]["Image_url"]
        status = data[i]["Status"]
        popularity = checkAndGetNumber(data[i]["popularity"])
        number_episodes = checkAndGetNumber(data[i]["number_episodes"])
        start_airing = str(data[i]["started_airing"])
        end_airing = str(data[i]["end_airing"])
        source = str(data[i]["Source"])
        duration = checkAndGetNumber(data[i]["duration_per_eps(min)"])
        rating = float(data[i]["rating"])
        ranked = checkAndGetNumber(data[i]["ranked"])
        description = str(data[i]["description"])
        doc_ = {"anime_ID": anime_ID, "jap_title": jap_title, "eng_title": eng_title, "image_url": image_url,
                "status": status, "popularity": popularity, "number_episodes": number_episodes,
                "start_airing": start_airing, "end_airing": end_airing, "source": source, "duration": duration,
                "rating": rating, "ranked": ranked, "description": description}
        es.index(index="animes", doc_type="animes", id=i, body=doc_)
    return ''
    # res = es.search(index="english", body=body)
    # return res


if __name__ == '__main__':
    app.run(debug=True)
