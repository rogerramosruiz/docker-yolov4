FROM nvidia/cuda:11.4.1-cudnn8-devel-ubuntu20.04
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update
RUN apt-get install -y git pkg-config libopencv-dev
WORKDIR /yolov4

COPY darknet ./darknet 
WORKDIR /yolov4/darknet
RUN make
