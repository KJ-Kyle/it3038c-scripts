#!/bin/bash

DATA=$(curl https://api.covidtracking.com/v1/us/current.json)
POSITIVE=$(echo $DATA | jq '.[0].positive')
TODAY=$(date)
NEGATIVE=$(echo $DATA | jq '.[0].negative')
STATES=$(echo $DATA | jq '.[0].states')
DEATHS=$(echo $DATA | jq '.[0].death')
TESTS=$(echo $DATA | jq '.[0].totalTestResults')

echo "On $TODAY, there were $POSITIVE positive COVID cases, $NEGATIVE negative cases, $DEATHS total deaths, with $TESTS taken in $STATES states. How are there that many states?"
