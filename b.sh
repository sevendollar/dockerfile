#!/bin/bash

for((b=0;b<=999999;b++)); do echo $b && curl -sL http://10.5.1.65 && clear> /dev/null; done
