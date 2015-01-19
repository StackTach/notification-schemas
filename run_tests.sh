#!/bin/bash

# Validate all the schemas
FAILURES=0

for d in 'nova' 'glance' ; do
    for file in $d/*.json ; do
        if [[ ! -d "$file" ]]; then
            echo -n "Validating: $file ... "
            python validate.py $file; RC=$?
            if [ "$RC" != "0" ]
            then
                echo "Fail"
                FAILURES=$((FAILURES + 1))
            else
                echo "Pass"
            fi
        fi
    done
done

exit $FAILURES
