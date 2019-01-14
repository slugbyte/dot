# MOLD  
> A CLI for managing dotfiles, shell scripts, executables, project scaffolds, and file templates  

![breakfast grool](https://assets.slugbyte.com/github/github-header-00011.png)  


## WARNING UNSTABLE
mold is under active development and not ready for production use.
### INSTALL
First you need to install the mold CLI and then use the mold cli to create a mold-root. A mold-root is 
a git repository that mold uses for storing all of your system configuration, shell scripts, and templates.
By default the installers will install your mold-root to **~/.mold**. mold uses the environment vairable 
$MOLD\_ROOT to determine where your mold-root has been installed.

##### INTERACTIVE INSTALLER
1. `pip3 install mold`
1. run `mold --install` and follow the instructions
    * you can optional add `--set-remote git://github.com:user/example.git` to initialize a git remote

##### QUICK INSTALL
The quick install does the same thing as the interactive installer without any prompting  
**WARNING** The quick install will overwrite the $MOLD\_ROOT if it all ready exists.  
1. `pip3 install mold`
1. run `mold --quick-install` and follow the output instructions
    * you can optional add `--set-remote git://github.com:user/example.git` to initialize a git remote

##### CREADING CUSTOM MOLD\_ROOT DIRECTORY
To change the MOLD\_ROOT from ~/.mold set the environment variable $MOLD\_ROOT before you run the installer
1. `export MOLD_ROOT=$HOME/path/to/your/mold_root`
2. `mold --quick-install --set-remote git://github.com:user/example.git`

##### CLONE AN EXISTING MOLD ROOT 
If you want to install an existing mold-root on another computer you can use `--clone`
* run `mold --clone git://github.com/user/mold-root.git` and follow the output instructions
    * if you want to overwrite the $MOLD\_ROOT if it exists add `--force`

## FEATURES
` USAGE: mold [--flags] [command] [task] [options]`  

TODO: write a nice about mold here.

## SMART HELP 
`-h`, `--help`, and `help` can be applied to anything in mold and their order does not matter

### COMMANDS
* `conf` -- manage dotfiles (CRUD + link to $HOME)
* `plug` -- manage shell scripts aka. plugins  (CRUD + sourced every new shell)
* `exec` -- manage executable files (CRUD + add them in a dir on $PATH)
* `file` -- manage file templates (CRUD + export to anywhere you want to use them)
* `fold` -- manage project scaffolds (CRUD + export to anywhere you want to use them)
* `sync` -- mangae the MOLD\_ROOT git repository

#### CORE -- MOLD\_ROOT file management 
The core commands are `conf`, `plug`, `exec`, `drop`, and `fold`. 

##### CORE TASKS
These tasks are applied to commands, and have suddly different behaviors based on the 
commands. e.g. if `mold conf make` will crate a file and then link it to $HOME, or 
`mold fold load` will load only directory instead of a file.
* `make` -- create new content 
* `load` -- import  content 
* `list` -- list the contents 
* `edit` -- edit contents 
* `drop` -- Delete contents 
* `take` -- (only for `fold` and `drop`) Export content into the current directory 

#### SYNC -- MOLD\_ROOT git management
##### SYNC TASKS
* `auto` -- pull add commit push (commit message from argv or text editor) 
* git wrappers for mold root
    * `log` 
    * `add -A` 
    * `commit` 
    * `pull` 
    * `push`  
    * `diff`  
    * `status`  
    * `branch`  
    * `remote`  
    * `--soft-reset`  
    * `--hard-reset`  
    * `--new-branch`  
    * `--checkout`  
    * `--force-push`  
    * `--merge`  
    
#### OTHER -- arbitrary tasks
* `--install` -- interactive installer 
   * `--remote-uri` automatically set the git remote origin with out prompting the user 
* `--quick-install` install without prompting 
* `--clone` -- create mold root from existing repo 
  * `--force` will delete a moldroot without prompting
* `--set-remote` -- set mold root's git origin remote 
* `--verson ` -- print mold version 
* `--color | MOLD_COLOR=true` -- force color when piping 
* `--complete` -- generate smart tab completion for a posix shell like bash or zsh  

### ENV
* `MOLD_ROOT` -- sets the directory that mold will use to install and manage everything 
* `MOLD_DEBUG` -- allow errors to be thrown without being cought 
* `MOLD_COLOR` -- force mold to print color even when piped into other programs

## NON-GOALS 
* Adding support for os or hostname specic detection
    * My [old mold like tools](https://github.com/slugbyte/mold/wiki/mold-prequels-and-their-lessons) had this feature, and I felt it over complicated the maintnece of my system configuration. 
    * Instead plugs, confs, and execs can implament their own condional logic [example](https://github.com/slugbyte/config/blob/master/config/.bashrc) or you can have more than one MOLD\_ROOT repository
    * Instead plugs, confs, and execs can implament their own condional logic [example](https://github.com/slugbyte/config/blob/master/config/.bashrc)
* Having the base install add premade configurration files
    * I don't follow the belief that systyem configurations can't be shared, because systems like [oh-my-zsh](https://ohmyz.sh/) work great for many people. However, molds goal is to help myself and others maintain their **personal** system configurations.
    * There is an option to Install from an existing mold_root on github, and I plan to make a *lite* oh-my-zsh like starter-kit mold_root repository at some point.

## IDEAS?
* create a `name` task to rename content 
* `-v | --verbose` -- make logging more verbose
* create a mold --shell-activate that will return a shell script for loading plugins (could be smart about which shell to use)
* make a tool to publish a new version to PyPi, brew, apt, and the arch-aur 
* write a markdown parser/transformner for tui output so that the help logs can be written in markdown
* (drop, plug, conf, exec) load -- suport for urls 
* fold load -- suport for github repositorys ? -> submodule support? 
* Build a start mold_root for beginners to using a shell (a oh-my-zsh/bash lite)
* Detect [fish](https://github.com/fish-shell/fish-shell) and return a differnt plug loader from --install
* Create a prety Documentation website
  * Maby add a feature for hosing files that people can `mold [command] load URL`
