import subprocess
import re
import sys
import os

# Things to support
## Create a branch / folder on Databricks under /User/me/branch_name
## Upload all files in selected folder to /User/me/branch_name

def get_current_branch():
    entries = subprocess.check_output(["git", "branch"]).strip().decode("utf-8").split("\n")

    results = [ branch for branch in entries if re.match("\\* ", branch) ]
    return results[0][1:].strip()

def get_username():
    if "DATABRICKS_USERNAME" in os.environ:
        return os.environ.get("DATABRICKS_USERNAME")

def get_user_branch_folder():
    current_branch = get_current_branch()
    user = get_username()
    return "/Users/{}/{}".format(user, current_branch)

def make_branch_folder():
    user_branch_folder = get_user_branch_folder()
    print(user_branch_folder)
    results = subprocess.call(["databricks", "workspace", "mkdirs", user_branch_folder ])
    return results

def upload_directory(local_folder, cloud_folder = None):
    if cloud_folder is None:
        cloud_folder = get_user_branch_folder()
    
    results = subprocess.call(["databricks", "workspace", "import_dir", local_folder, cloud_folder, "--overwrite" ])
    return results

def download_directory(local_folder, cloud_folder = None):
    if cloud_folder is None:
        cloud_folder = get_user_branch_folder()
    
    results = subprocess.call(["databricks", "workspace", "export_dir", cloud_folder, local_folder, "--overwrite" ])
    return results

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--setup", action='store_true')
    parser.add_argument("--upload", action='store_true')
    parser.add_argument("--download", action='store_true')
    parser.add_argument("-s", "--source")
    parser.add_argument("-t", "--target")

    args = parser.parse_args()
    
    if args.setup:
        results = make_branch_folder()
        if results == 0:
            print("Successfully set up the feature folder")
        else:
            print(results)
            sys.exit()
    
    if args.source and args.upload:
        target = get_user_branch_folder()
        if args.target:
            target = args.target
        
        upload_directory(local_folder = args.source, cloud_folder= target)
        sys.exit()
    
    if args.target and args.download:
        source = get_user_branch_folder()
        if args.source:
            source = args.source
        
        download_directory(cloud_folder = source, local_folder = args.target)
        sys.exit()
