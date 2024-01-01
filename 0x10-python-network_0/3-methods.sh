#!/bin/bash
#display HTTP methods the server of given URL
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
