FROM python


WORKDIR /usr/src/myapp

RUN pip install Flask

COPY . /usr/src/myapp/


COPY . .

EXPOSE 5000
CMD ["python", "app.py"]