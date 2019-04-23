#!/bin/bash

CWD=$(pwd)

cd $CWD

git clone https://github.com/jeffreylancaster/game-of-thrones.git /tmp/gt

rm  -rf gameofthrones/data/*

cp /tmp/gt/data/*.json gameofthrones/data/.
