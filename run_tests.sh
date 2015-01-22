#!/bin/bash

# Validate all the schemas
FAILURES=0

for d in 'nova' 'glance' ; do
    for file in ${d}/*.json ; do
        if [[ ! -d "$file" ]]; then
            echo -n "Validating schema: $file ... "
            python validate.py ${file}; RC=$?
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

for d in 'nova' 'glance' ; do
    for file in 'samples/'${d}/*.json ; do
        if [[ -f "$file" ]]; then
            schemaname=${file%_*}
            schema=$d/${schemaname##*/}'.json'
            echo -n "Validating payload: $file against schema: $schema..."
            python validate_payload.py --payload ${file} --schema ${schema}; RC=$?
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
