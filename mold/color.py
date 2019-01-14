_ansi_colors = {
    "reset" : '\033[39m',
    "red" : '\033[31m',
    "blue" : '\033[94m', 
    "cyan" : '\033[36m',
    "grey" : '\033[38m',
    "green" : '\033[32m',
    "yellow" : '\033[33m',
    "magenta"  : '\033[35m',
    "lightgrey" : '\033[37m',
}

def get_color(ctx, name):
    if not ctx.check_color_mode_set():
        return ''
    try:
        return _ansi_colors[name]
    except:
        return ''
