# build environment for Golang

# build stage
FROM golang:1.14.6 AS build-env
ENV GO111MODULE=on
WORKDIR /app
COPY go.mod .
COPY go.sum .
RUN go mod download
COPY . .
RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -o go

# final stage
FROM scratch
LABEL maintainer="sevendollar@gmail.com"
COPY --from=build-env /app/go /go
# EXPOSE 8080
ENTRYPOINT ["/go"]