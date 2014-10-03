# Sublime CloneFile plugin

Provides "duplicate view" and "clone file/folder in list" functionality.

### Demo

![Demo](https://raw.github.com/shagabutdinov/sublime-clone-file/master/demo/demo.gif "Demo")


### WARNING

It use python "shutil" to clone folders and files so meta-information (e.g.
permissions) of files and folder can be lost after copying.

When you are cloning file in list you should hit "tab" (but not "enter") after
entering a new file name. See "Usage" section below for undestanding usecase.


### Dependencies


### Installation

This plugin is part of [sublime-enhanced](http://github.com/shagabutdinov/sublime-enhanced)
plugin set. You can install sublime-enhanced and this plugin will be installed
automatically.

If you would like to install this package separately check "Installing packages
separately" section of [sublime-enhanced](http://github.com/shagabutdinov/sublime-enhanced)
package.


### Usage

Hit keyboard shortcut or run command to clone current view into the new view. It
will create new view, copy contents of old view to new one, and set cursors into
the new view according to cursors in old one.

If you are browsing file through "FileList" plugin you can copy file here with
keyboard shortcut. You need to hit keyboard shortcut for "Clone file in list"
(see below) than navigate to preferred folder, type name of file and hit
keyboard shortcut for "Complete cloning file in list" ("tab" by default). Note
that it'll use "tab" for cloning completion but not "enter" (sublime does not
allow "enter" remap in quick search panel). "Enter" will open selecter folder or
file.


### Commands

| Title                         | Keyboard shortcuts | Command palette  |
|-------------------------------|--------------------|------------------|
| Clone view                    | ctrl+alt+shift+d   | CloneFile: Clone |
| Clone file in list            | ctrl+alt+c         |                  |
| Complete cloning file in list | tab                |                  |