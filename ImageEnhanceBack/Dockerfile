FROM python:3.12.3

COPY . /www/

WORKDIR /www

RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

RUN pip install uwsgi -i https://pypi.tuna.tsinghua.edu.cn/simple

RUN mkdir -p /data/log
RUN mkdir -p /data/sock

EXPOSE 8000

ENTRYPOINT python manage.py makemigrations; \
python manage.py migrate; \
uwsgi --ini uwsgi.ini