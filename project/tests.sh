#!/bin/bash


echo "Running ETL Pipeline..."
bash ./project/pipeline.sh

echo "Running System Level Test..."
python ./project/test.py

echo "Running unit-test/pytest..."
pytest ./project/test.py
