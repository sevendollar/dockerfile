# gRPC package generator for Go

# run the docker command below to get what you need
# $docker run --rm -v ${PWD}:/grpc sevendollar/grpc-go

FROM golang:1.14.6
LABEL maintainer="sevendollar@gmail.com"
WORKDIR /grpc

# Enable module mode
ENV GO111MODULE=on

# install protoc-gen-go
RUN go get github.com/golang/protobuf/protoc-gen-go
ENV PATH="$PATH:$(go env GOPATH)/bin"

# install protoc
ENV PB_REL="https://github.com/protocolbuffers/protobuf/releases"
RUN curl -LO $PB_REL/download/v3.12.1/protoc-3.12.1-linux-x86_64.zip
RUN apt-get update -y && \
    apt-get install -y unzip && \
    unzip protoc-3.12.1-linux-x86_64.zip && \
    cp bin/protoc /bin/ && \
    rm -rf *

COPY generate_grpc.sh .

RUN chmod +x generate_grpc.sh && \
    mv generate_grpc.sh /bin

# run the shell script to generate gRPC package for Go
CMD [ "generate_grpc.sh" ]