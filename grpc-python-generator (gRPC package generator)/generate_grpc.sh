#!/bin/bash
python -m grpc_tools.protoc  --python_out=. --grpc_python_out=. *.proto -I .