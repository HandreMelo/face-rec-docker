FROM python:3
LABEL maintainer="ANDRE F.C. MELO"

RUN pip install cmake
RUN pip install dlib
RUN pip install gunicorn
RUN pip install Flask
RUN pip install Jinja2
RUN pip install Werkzeug
RUN pip install numpy
RUN pip install face-recognition
# Add our code
ADD ./webapp /opt/webapp/

WORKDIR /opt/webapp

CMD gunicorn --bind 0.0.0.0:$PORT wsgi