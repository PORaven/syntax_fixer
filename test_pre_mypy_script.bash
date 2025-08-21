#!/bin/bash

ERRORS=$(mypy "$@" 2>&1)
RESULT=$?

if [ $RESULT -ne 0 ]; then
    echo "mypy find types errors."
    echo "$ERRORS"
    exit 1
fi

exit 0
