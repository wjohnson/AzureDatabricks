import json
import sys

from dbrlint.dbrlinter import DBRLinter

if __name__ == "__main__":
    job_path = sys.argv[1]
    rules_path = sys.argv[2]

    with open(job_path, 'r') as fp:
        job_definition = json.load(fp)
    
    linter = DBRLinter(rules_path)

    errors = linter.evaluate(job_definition)

    if len(errors) > 0:
        print("Validation Failed:")
        for err in errors:
            print(err)
        sys.exit(1)
    else:
        print("Completed Successfully!  No errors in job definition.")
        sys.exit(0)
