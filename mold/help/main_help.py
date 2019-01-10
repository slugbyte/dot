text = '''
{green}{mold.__description__}{reset}

USAGE: mold [COMMAND] [TASK] [OPTIONS]

ABOUT:
    mold uses a git repository to store and track system configuration
    files. It splits the files in to the following classifications.
        conf: -- conf files are the dotfiles that will be hard linked to 
                the $HOME directory. e.g. mold load ~/.bashrc
        plug: -- plug files are shell scripts that will be sourced each time
                you create a new shell. e.g. mold plug make alias.sh
        exec: -- exec files will be added to a directory that will be in 
                the $PATH. e.g. exec load ./my-program 
        drop: -- drop files are file asset templates that you want add to 
                future projects. e.g. mold drop MIT-LICENSE.md
        fold: -- a fold is a project directory scaffold template, its like
                drop but its a whole directory. mold fold react-starter

INSTALL:
    To install a $MOLD_ROOT for the first time run `mold --install` 
    The $MOLD_ROOT directory will be set to ~/.mold and it will
    use $EDITOR or nano as the text editor.

    For custom installation see the mold github repository.

INSTALL FROM REPOSITORY:
    To install from an existing remote run `mold --clone [git uri]`

CONFIGURATION:
    GIT REMOTE:
    You can either manualy change the MOLD_ROOT git remote, or you can 
    also run `mold --set-origin [https://github.com/user/example.git]` 
    to reset the git remote.

    TEXT EDITOR:
    To change the text editor use bash to $EDITOR to point to the 
    a text editor executable.
    e.g. In the shell config write 'export EDITOR = /usr/local/bin/vim'

HELP: 
    mold and each of the mold comands have -h, --help, and help options for 
    color_printing help.

COMMANDS: 
    TASKLESS:
    help:    show this help  

    WITH TASKS (auto and many more)
    sync:    sync git with remote and system config

    WITH TASKS (make load edit nuke) 
    fold:    manage project scaffolding templates (+ dump task)
    drop:    manage file asset templates (+ dump task) 
    conf:    manage configuration files 
    exec:    manage executables
    plug:    manage bash pugins 

<3 Bug reports are much appreciated {mold.__url__}/issues
    '''.strip()