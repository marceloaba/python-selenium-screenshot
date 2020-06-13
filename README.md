# python-selenium-screenshot
Taking a screenshot using a python, selenium and chrome

#### You can use this docker container to run everything headless without the need of a GUI, just use the docker image below:
###### marceloaba/python-chromedriver-headless [Docker Hub Repository](https://hub.docker.com/repository/docker/marceloaba/python-chromedriver-headless)


#### How to run the container and script:
```
docker run -dit -w /script -v ${PWD}:/script marceloaba/python-chromedriver-headless
docker exec -it entercontainerid sh
python3 screenshot.py
```
