# gRPC package generator for Python

# run the docker command below to get what you need
# $docker run --rm -v ${PWD}:/grpc sevendollar/grpc-python-generator

FROM python:latest
LABEL maintainer="sevendollar@gmail.com"
WORKDIR /grpc
COPY generate_grpc.sh .
RUN python -m pip install --upgrade pip && \
    python -m pip install grpcio && \
    python -m pip install grpcio-tools && \
    \
    chmod +x generate_grpc.sh && \
    mv generate_grpc.sh /bin
ENTRYPOINT [ "generate_grpc.sh" ]