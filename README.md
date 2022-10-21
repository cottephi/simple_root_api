Simple Flask API taht can be used to get the root of a real number.

To start the api, cd in the directory of containing this file and run in a terminal :

```bash
flask run
```

To query the API, open another terminal anywhere and run

```bash
curl "localhost:5000/racine?x=X"
```

Where you replace *X* by the real number you need the square root of.