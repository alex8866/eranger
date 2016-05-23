+ set hidden files
+ search
+ color theme
+ command
+ file operator
+ vim like
+ tabs


commands.py: self.fm.thisdir, self.fm.thisfile
cf.path -
# self.fm: A reference to the "fm" object which contains most information
#      about ranger.
# self.fm.notify(string): Print the given string on the screen.
# self.fm.notify(string, bad=True): Print the given string in RED.
# self.fm.reload_cwd(): Reload the current working directory.
# self.fm.thisdir: The current working directory. (A File object.)
# self.fm.thisfil/e: The current file. (A File object too.)
# self.fm.thistab.get_selection(): A list of all selected files.
# self.fm.execute_console(string): Execute the string as a ranger command.
# self.fm.open_console(string): Open the console with the given string
#      already typed in for you.
# self.fm.move(direction): Moves the cursor in the given direction, which
#      can be something like down=3, up=5, right=1, left=1, to=6, ...
#
# File objects (for example self.fm.thisfile) have these useful attributes and
# methods:
#
# cf.path: The path to the file.
# cf.basename: The base name only.
# cf.load_content(): Force a loading of the directories content (which
#      obviously works with directories only)
# cf.is_directory: True/False depending on whether it's a directory.
#
# For advanced commands it is unavoidable to dive a bit into the source code
# of ranger.
# ===================================================================

ranger/gui/widgets/browsercolumn.py:    def _draw_directory_color(self, i, drawn, copied):
ranger/gui/widgets/browsercolumn.py:        this_color = []
ranger/gui/widgets/browsercolumn.py:            this_color.append('selected')
ranger/gui/widgets/browsercolumn.py:            this_color.append('marked')
ranger/gui/widgets/browsercolumn.py:            this_color.append('tagged')
ranger/gui/widgets/browsercolumn.py:            this_color.append('directory')
ranger/gui/widgets/browsercolumn.py:            this_color.append('file')
ranger/gui/widgets/browsercolumn.py:                this_color.append('executable')
ranger/gui/widgets/browsercolumn.py:                this_color.append('fifo')
ranger/gui/widgets/browsercolumn.py:                this_color.append('socket')
ranger/gui/widgets/browsercolumn.py:                this_color.append('device')


# 
1. Add tab 1 to open file1, alt+1 switch to file1, alt+2: switch to file2, reload file
2. Add view shotkeys
3. add options -d for direcoty diff, may remove as_dire configure, git commit first
