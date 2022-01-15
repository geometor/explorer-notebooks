#!/usr/bin/env bash

melt hot-0233-0001.png out=48 \
  hot-0233-0002.png out=44 -mix 22 -mixer luma \
  hot-0233-0003.png out=40 -mix 20 -mixer luma \
  hot-0233-0004.png out=36 -mix 18 -mixer luma \
  hot-0233-0005.png out=32 -mix 16 -mixer luma \
  hot-0233-0006.png out=28 -mix 14 -mixer luma \

