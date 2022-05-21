# Modelorama Now
This API is for *Modelorama Now* assesment.

The programming lenguage is Python and use ElasticSearch to storage the cities information and to search the request cities.

You can make a request of the following endpoits:
* POST: `/bulk`
* GET: `/search`
With */search* endpoint you can add parameters.

The url have de default port of Python  `:5000`.

## Run ElasticSearch

To run the API first you need to run the docker compose using the `docker-compose.yml`file which you can find in the attachments. Use the following command in your terminal:

`docker-compose up`

Then you will see that ElasticSearch and Kibana are running.

## Run Python API

You need python3 to run this API.

Next, you can create a virtual environment in the same folder that you downloaded:

   1. `pip3 install virtualenv`
   2. `virtualenv env`. You will now that you are in the environment because in your terminal propmt will have `(env)`.
   3. `source env/bin/activate`
   4. Install libraries:
      * `pip install elasticsearch==7.8`
      * `pip install Flask`
      

Then you can run the API using

`python3 app.py`

## Endpoints

### Bulk cities

* Request HOST: http://localhost:5000/bulk or http://127.0.0.1:5000/bulk
* Method: POST
* Body: Its is a form-data with key `file` and value `cities-canda-usa.json` file.
* Response:

| Status Code | Description |
|    :---:    |    :----   |
| 200         |The file was bulked successfully and the response is a text: Succes bulk cities.  |
| 400         |The user didn't attached a file.                                                  |
| 500         |When an error occurred with the service: ElasticSearch or the API, the response will be a text describing the problem.|

### Search cities

* Request HOST: http://localhost:5000/search or http://127.0.0.1:5000/search
* Method: GET
* Path: ?q={city_name}&latitude={latitude}&longitude={longitude}
* Parameters

| Parameter  | Required    | Description |
|    :---:   |    :---:    |    :----   |
| q          | required    |A word or a incomplete word of the city that you want to search. |
| latitude   | optional    |A number of the latitude of the city that you want to search.    |
| longitude   | optional   |A number of the longitude of the city that you want to search.   |

* Response:

| Status Code | Description |
|    :---:    |    :----   |
| 200         |Returns a json with the found cities            |
| 400         |The user didn't write the required parameters.  |
| 500         |When an error occurred with the service: ElasticSearch or the API, the response will be a text describing the problem.|

* Example

    * Request URL: http://127.0.0.1:5000/search?q=Amherst&latitude=45&longitude=-74
    * Response:

    ```
    {
        "search": [
            {
                "latitude": 42.41037,
                "longitude": -72.53092,
                "name": "North Amherst, MA, US",
                "score": 0.9404064
            },
            {
                "latitude": 42.37537,
                "longitude": -72.51925,
                "name": "Amherst Center, MA, US",
                "score": 0.9389934
            },
            {
                "latitude": 42.97839,
                "longitude": -78.79976,
                "name": "Amherst, NY, US",
                "score": 0.8286036
            },
            {
                "latitude": 41.39782,
                "longitude": -82.22238,
                "name": "Amherst, OH, US",
                "score": 0.57203186
            },
            {
                "latitude": 42.11679,
                "longitude": -83.04985,
                "name": "Amherstburg, 08, CA",
                "score": 0.5350973
            },
            {
                "latitude": 45.83345,
                "longitude": -64.19874,
                "name": "Amherst, 07, CA",
                "score": 0.51135826
            }
        ]
    }
    ```
