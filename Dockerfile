FROM python:3.7
WORKDIR /usr/src/app

# ensure local python is preferred over distribution python
ENV PATH /usr/local/bin:$PATH

# Install pipenv so that we can use it to install the dependencies.
RUN pip install --user pipenv

# Copies pipfiles from the local directory to the image. The . means the current working directory.
COPY Pipfile Pipfile.lock ./

# Install pip packages ("you usually don’t need to add a virtual environment inside the container. Instead, you can
# run pip directly to install the necessary packages - https://realpython.com/python-versions-docker/#building-your-own-images-using-dockerfiles)
# See pipenv install --help for what these options mean, but it will NOT install using a virtualenv, but to the system.
RUN python -m pipenv install --deploy --system

EXPOSE 5000

# Copies file from local directory to the image.
COPY . /usr/src/app
CMD ["python3", "word_pyramid.py"]