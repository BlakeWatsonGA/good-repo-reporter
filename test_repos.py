#!/usr/bin/env python3

import os, sys
import subprocess
import fnmatch

def get_repos(top_path):
    repos = []
    for path, subdirs, files in os.walk(top_path):
        if os.path.exists(path+"/.git"):
            repos.append(path)
    return repos

def get_cmd_out(this_cmd):
    p = subprocess.Popen(this_cmd.split(),
                     stdout=subprocess.PIPE)
    preprocessed, _ = p.communicate()
    return str(preprocessed)


def run_branch_test(this_repo, these_branches):
    
    print(f' \t Looking for required branches...', end = '') 
    
    out_str = get_cmd_out(f'git --git-dir={this_repo}/.git branch -a')
    
    passes_btest = True
    
    missing_branches = []
    
    for b in these_branches:
        if b not in out_str:
            passes_btest = False
            missing_branches.append(b)
    if passes_btest:
        print('PASS')
    else:
        print('FAIL')
        for mb in missing_branches:
            print(f"\t\t Missing required branch: {b}")
    return False
    
    
def list_branches(this_repo):
    os.system(f'git --git-dir={this_repo}/.git branch -a')
    return 

def list_tags(this_repo):
    os.system(f'git --git-dir={this_repo}/.git tag -l')
    return 

def pull_all_tags(this_repo):
        os.system(f'git --git-dir={this_repo}/.git fetch --tags')

        
input_path =  input("Enter the directory path containing the git repositories: ")
required_branches = ['remotes/origin/main', 'remotes/origin/dev','remotes/origin/test']

for r in get_repos(input_path):
    print(f'Checking Repository {r}') 
    list_branches(r)
    list_tags(r)
    run_branch_test(r, required_branches)
    pull_all_tags(r)


