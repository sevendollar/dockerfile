# gRPC package generator for Go

# run the docker command below to get what you need
# $docker run --rm -v ${PWD}:/grpc sevendollar/grpc-go


FROM golang:1.14.6
LABEL maintainer="sevendollar@gmail.com"
WORKDIR /grpc


# Protocol buffer compiler
ENV PB_REL="https://github.com/protocolbuffers/protobuf/releases"

RUN curl -LO $PB_REL/download/v3.12.1/protoc-3.12.1-linux-x86_64.zip

RUN apt-get update -y && \
    apt-get install -y unzip && \
    unzip protoc-3.12.1-linux-x86_64.zip && \
    cp bin/protoc /bin/ && \
    rm -rf *

COPY grpc_gen_go.sh .

RUN chmod +x grpc_gen_go.sh && \
    mv grpc_gen_go.sh /bin


# Go plugins for the protocol compiler
ENV GO111MODULE=on

RUN go get github.com/golang/protobuf/protoc-gen-go \
    google.golang.org/grpc/cmd/protoc-gen-go-grpc

ENV PATH="$PATH:$(go env GOPATH)/bin"


# run the shell script to generate gRPC package for Go
CMD [ "grpc_gen_go.sh" ]