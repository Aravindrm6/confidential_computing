FROM ubuntu:20.04
WORKDIR /work
COPY.
RUN env DEBIAN FRONTEND-noninteractive apt-get update \
&& env DEBIAN_FRONTEND=noninteractive apt-get install -y python3.8 python3-pip #RUN python3 -m pip install --upgrade pip
RUN pip install -r requirements.txt
CMD [ "python3", "creditcard_inference.py"]
