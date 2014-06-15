from main import Main
import sublime, sublime_plugin
#import os

class LogAnalyzerCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        #self.view.insert(edit, 0, "Hello, World!")
        file_name = sublime.active_window().active_view().file_name()

        log_analyzer = Main(file_name, sublime.packages_path() + "/settings.json", sublime.packages_path() + '/modified_file.log')
        log_analyzer.perform_analysis()
        #sublime.status_message("current_dir:" + os.path.abspath(os.curdir))

        sublime.active_window().open_file(log_analyzer.output_filename)

        sublime.active_window().active_view().settings().set("syntax", "log_analyzer.tmLanguage")
        #sublime.active_window().active_view().settings().set("syntax", "Python/Python.tmLanguage")
        #sublime.status_message(str(sublime.active_window().settings().get("syntax")))