Word Pyramid Exercise
============

Dependencies
---

### Docker
If you don't have docker installed, you can use pipenv.
See Dockerfile for details on installing and setting up
a pipenv environment.

Running w/ Docker
----

### Build the docker image
`docker build -t fetch_rewards .`

### Run the docker image
`docker run -p 5000:5000 fetch_rewards`

### Run the tests
`docker run fetch_rewards python -m pytest tests/test_pyramid.py`