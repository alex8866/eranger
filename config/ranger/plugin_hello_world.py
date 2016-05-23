# Compatible with ranger 1.6.0 through 1.7.*
#
# This is a sample plugin that displays "Hello World" in ranger's console after
# it started.

# We are going to extend the hook "ranger.api.hook_ready", so first we need
# to import ranger.api:
import ranger.api

# Save the previously existing hook, because maybe another module already
# extended that hook and we don't want to lose it:
old_hook_ready = ranger.api.hook_ready

# Create a replacement for the hook that...
import sys
def hook_ready(fm):
    # ...does the desired action...
    print ranger.arg.targets
    fm.notify("Hello World")
    # ...and calls the saved hook.  If you don't care about the return value,
    # simply return the return value of the previous hook to be safe.

    # Do some basic compare
    from ranger.diff import diff
    from time import sleep

    # test
    import traceback
    try:
        # init curses screen
        stdscr = curses.initscr( )

        curses.start_color()
        # stdscr.use_default_colors()
        curses.start_color()
        curses.init_pair(1, curses.COLOR_RED, 0)
        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_GREEN)
        COLOR_RED    = curses.color_pair(1)
        COLOR_GREEN  = curses.color_pair(2)

        dir_diff = diff.DirDiff(ranger.arg.targets[0], ranger.arg.targets[1], '')
        os.system('rm -rf /tmp/ddir && mkdir -p /tmp/ddir')
        var = os.path.basename(ranger.arg.targets[0])
        os.system('cp -a %s /tmp/ddir/%s' % (ranger.arg.targets[1], var))
        os.system('rsync -a %s/* %s/' % (ranger.arg.targets[0], '/tmp/ddir/%s' % var))
        diff.showMessageDialog(message=dir_diff.print_summary(), title='Summary of changes')
    except:
        curses.endwin( )
        traceback.print_exc()

    var = os.path.basename(ranger.arg.targets[0])
    ranger.arg.targets = []
    ranger.arg.targets.append('/tmp/ddir/%s/' % var)


    return old_hook_ready(fm)

# Finally, "monkey patch" the existing hook_ready function with our replacement:
ranger.api.hook_ready = hook_ready


# Save the original filter function
import ranger.gui.widgets.browsercolumn
old_draw_directory = ranger.gui.widgets.browsercolumn.BrowserColumn._draw_directory

# Define a new one
def new_draw_directory(self):
    """Draw the contents of a directory"""
    pass

import ranger.gui.widgets.browsercolumn
ranger.gui.widgets.browsercolumn.BrowserColumn._draw_directory = old_draw_directory
