# Databricks CLI Helper
A little CLI helper for working with Azure Databricks and Git Integration

The Databricks CLI Helper requires the `databricks-cli` pypi package and for you to have [configured the CLI](https://docs.microsoft.com/en-us/azure/databricks/dev-tools/cli/?toc=https%3A%2F%2Fdocs.microsoft.com%2Fen-us%2Fazure%2Fazure-databricks%2FTOC.json&bc=https%3A%2F%2Fdocs.microsoft.com%2Fen-us%2Fazure%2Fbread%2Ftoc.json#set-up-the-cli).

You'll need to add one more environment variable to your system path: **DATABRICKS_USERNAME** and set it to however your name appears in the databricks User workspace folder.

This tool has three paths:

## --setup

`python dbr-helper.py --setup`

* Creates a user folder in your Azure Databricks workspace with the **current git branch name**.
* The --setup flag can be combined with the commands below.

## --upload --source (optional: --target)

`python dbr-helper.py --source ./notebooks --upload`
OR
`python dbr-helper.py --source ./notebooks --target "/Shared/Some/Path" --upload`

* Uploads a set of files from your local file system (--source) to your Databricks workspace.
* --target is optional.  By Default, it will assume your User folder with the **current git branch name** as the target folder.

## --download --target (optional: --source) 
`python dbr-helper.py --target ./notebooks --download`
OR
`python dbr-helper.py --target ./notebooks --source "/Shared/Some/Path" --download`

* Downloads a set of files from your Databricks workspace to your local file system (--target).
* --source is optional.  By Default, it will assume your User folder with the **current git branch name** as the source folder.

## Example Workflows

### Using Databricks as your editor

    git checkout -b MyFeatureX
    python dbr-helper.py --setup
    python dbr-helper.py --upload --source ./notebooks
    # Do some work in Databricks
    python dbr-helper.py --download --target ./notebooks
    git add *
    git commit -m "Made some changes"
    git push origin

Alternaively, you could combine --setup and --upload.  --setup will run first and then perform the upload.

    python dbr-helper.py --setup --upload --source ./notebooks


## Grab a subset of files to change from another folder in Databricks

    git checkout -b MyFeatureY
    python dbr-helper.py --download --target ./notebooks/processX --source /processX
    # Do some work locally
    git add *
    git commit -m "Made some changes"
    git push origin
