# GitHub Backup Python Script

Yet another backup script for GitHub repositories. 

## How it works

Downloads every repository under a user's name using GitHub API in a very lazy manner:

*https://api.github.com/users/<user_name>/repos*

The configuration parameters are set up on the [config file](config_file_sample/config.json), that should be located alongside the backup script.


## Why ?

Whilst open source for all intent and porpuses rocks! The companies that support them need a source of income and are a bound by the laws and politics of their respective countries. In a hipotetical scenario where repositories are no longer acessible for any reason, I would like to be able o revert to a alternaive backup source however simple it may be.
With that in mind, I needed a simple script that could be run before my pre exising backup solution and that could be written very fast wihout much trouble. The plan is to add as many functions as possible as soon as they are needed.

## Prerequisites

1. Install Python Wget library
```
pip install wget
```
2. Copy the file script [gitbackup.py](gitbackup.py) 

3. Set up the config JSON file with your custom parameters copying the file under [config_file_sample](config_file_sample/config.json) to the same folder of the script

```JSON
{
    "git_user":"thethales",
    "destination_folder":"E:/_backup/github_temp",
    "use_git_clone": 0
}
```
