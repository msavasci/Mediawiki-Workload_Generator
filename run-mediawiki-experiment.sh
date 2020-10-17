#!/bin/bash

#echo Experiment start time : $(date) >> $4

python3 MediawikiWorkloadGenerator.py $1 $2 $3 $4

#echo Experiment finish time : $(date) >> $4
