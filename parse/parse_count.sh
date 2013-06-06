#!/bin/sh

string=""
for ((i=2005; i < 2011; i++)); do
	for file in /data/patentdata/patents/"$i"/*.xml; do
		string+="$file "
	done
done
python parser_ipg.py "$string"
