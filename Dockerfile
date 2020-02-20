FROM python:3.7.6
MAINTAINER Vishal Ravi Shankar "mail@vshl.me"
ENV FLASK_APP "api.py"
ENV FLASK_ENV "development"
ENV FLASK_DEBUG True
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["flask", "run", "--host=0.0.0.0"]
