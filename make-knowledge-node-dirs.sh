#!/bin/bash
SCRIPTDIR=$(dirname $0)
find -type f -name '*.md' -a -not -name 'README.md' | while read filename; do
title=$(basename $filename .md)
dir=$(dirname $filename)
outputdir="$dir/$title"
mkdir "$outputdir"
mv "$filename" "$outputdir"
(cd "$outputdir";
python3 $SCRIPTDIR/wikipedia-attribution-gen.py "$title"
)
done
