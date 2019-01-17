'''
main is defines the logic for the cli, it is a router 
for SUB_COMMANDs and OPTIONS.
'''

import sys
import mold
import mold.commands.core as core
import mold.commands.sync as sync
import mold.commands.help as help
import mold.commands.root as root
import mold.commands.list as list
import mold.commands.version as version
import mold.commands.complete as complete

# TODO migrate colors into context

# INTERFACE
def handle_context(ctx):
    # The ordering of the command_chain array is important
    command_chain = [
        complete.handle_context, # priority 1 because any other logging  will break completion
        version.handle_context,  # priority 2 because --version should allways be supported
        help.handle_context,     # priority 3 because help should allways be available
        root.handle_context,     # priorigy 4 because it asserts a mold root is installed 
        # below this point order does not matter and a mold_root is garinteed
        core.handle_context,     
        list.handle_context,
        sync.handle_context,
    ]
    
    for command in command_chain:
        result = command(ctx)
        if result != ctx.NEXT_COMMAND:
            return result

    print(f'{ctx.red}doh!{ctx.reset} mold {ctx.command} isn\'t a feature yet.')
    return ctx.OK

