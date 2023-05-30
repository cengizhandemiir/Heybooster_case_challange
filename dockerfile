FROM python:3.9-slim-buster

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc


COPY requirements.txt /heybooster_my_case/
RUN pip install --no-cache-dir -r /heybooster_my_case/requirements.txt

COPY . /heybooster_my_case
WORKDIR /heybooster_my_case


CMD ["python", "api.py"]
