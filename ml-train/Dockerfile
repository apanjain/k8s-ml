FROM python

WORKDIR /home

RUN pip3 install sklearn pandas pyArango

COPY train.py ./

CMD python3 train.py
