import sublime, sublime_plugin, re

class CssGroupsCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.groups = []
        self.view.find_all("@group.*(?=\*)", 0, "$0", self.groups)
        self.view.window().show_quick_panel(self.groups, self.goto_group, sublime.MONOSPACE_FONT)

    def goto_group(self, choice):
        if choice == -1:
            return

        group = self.groups[choice]
        jump_location = self.view.find(re.escape(group), 0)

        self.view.sel().clear()
        self.view.sel().add(jump_location)
        self.view.show_at_center(jump_location)