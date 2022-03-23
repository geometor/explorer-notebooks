#!/usr/bin/env bash


sxiv -g 1920x1080+0+768 -bf *.png
find ranges -name '*.png' | grep -v zoom | sort | sxiv -bfi -g 1920x1080+0+768 
sxiv -g 1920x1080+0+768 -bf ranges/*.png
