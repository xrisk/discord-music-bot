#!/usr/bin/env bash

set -e

docker build --build-arg CACHE_DATE=$(date +%Y-%m-%d:%H:%M:%S) -t musicbot .
docker run musicbot