import sublime
import sublime_plugin
import shutil
import os

try:
  from FolderFiles.folder_files import FolderFiles
  from QuickSearchEnhanced import quick_search
except ImportError as error:
  sublime.error_message("Dependency import failed; please read readme for " +
   "CloneFile plugin for installation instructions; to disable this " +
   "message remove this plugin; message: " + str(error))
  raise error

class CloneView(sublime_plugin.TextCommand):
  def run(self, edit):
    view = sublime.active_window().new_file()
    view.insert(edit, 0, self.view.substr(sublime.Region(0, self.view.size())))
    view.set_syntax_file(self.view.settings().get('syntax'))

    selections = []
    for selection in self.view.sel():
      selections.append(selection)

    view.sel().clear()
    view.sel().add_all(selections)

class CloneFile():
  def __init__(self, file_name):
    self.file_name = file_name
    self.folder = FolderFiles(os.path.dirname(file_name), None, False,
      '♽', {'text': os.path.basename(file_name)}, [['clone', self]])

  def get_path(self):
    return self.path

  def show(self):
    self.folder.show()

  def clone(self, file_name):
    try:
      path = self.folder.get_current_path() + '/' + file_name
      if os.path.isdir(self.file_name):
        shutil.copytree(self.file_name, path)
      else:
        shutil.copy(self.file_name, path)

    except Exception as error:
      sublime.error_message('Error while copying file: {0}'.format(error))
      return None

    return path

class PromptCloneFileInList(sublime_plugin.TextCommand):
  def run(self, edit):
    panel = quick_search.panels.get_current()
    file_list = panel.get_caller('file_list')
    if file_list == None:
      return

    CloneFile(panel.get_current_value()).show()

class CloneFileInListComplete(sublime_plugin.TextCommand):
  def run(self, edit):
    panel = quick_search.panels.get_current()
    clone = panel.get_caller('clone')
    if clone == None:
      return

    panel.hide()
    new_path = clone.clone(panel.get_current_text())
    if new_path == None:
      panel.show()
      return

    panel.close(None, False)