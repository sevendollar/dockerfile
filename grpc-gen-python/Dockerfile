# gRPC package generator for Python

# run the docker command below to get what you need
# $docker run --rm -v ${PWD}:/grpc sevendollar/grpc-python-generator

FROM python:latest
LABEL maintainer="sevendollar@gmail.com"

WORKDIR /grpc

COPY grpc-gen-python.sh .

RUN python -m pip install --upgrade pip && \
    python -m pip install grpcio && \
    python -m pip install grpcio-tools && \
    \
    chmod +x grpc-gen-python.sh && \
    mv grpc-gen-python.sh /bin

ENTRYPOINT [ "grpc-gen-python.sh" ]