#!/bin/bash

for file in /home/hariharan/Code/PS-1/prj/keras_frcnn/test_images/*
do
	python /home/hariharan/Code/PS-1/prj/keras_frcnn/predict_banana.py -p "/home/hariharan/Code/PS-1/prj/keras_frcnn/test_images/$file"
done