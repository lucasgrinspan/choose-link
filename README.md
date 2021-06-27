# Link Chooser

This tiny script shows a spotlight-esque fuzzy matcher ([choose](https://github.com/chipsenkbeil/choose)) to open a link. It supports a flat list or a list with nestable categories. Check `links.json` for an example of the data structure.

## Installation

Python and homebrew are required to install and use this utility. After cloning this repo, run these commands:

```bash
cd choose-link

# Required to show the choose GUI
brew install choose-gui

# Or the PATH of your choice
cp chooser.py /usr/local/bin/choose-link

# This is where the script checks for the config JSON
mkdir ~/.choose-link
cp links.json ~/.choose-link/
```

Now you'll have to setup an Automator action to run this script with a keybinding. After opening the Automator app, select "New Document". When the option arises, select "Quick Option".

For the value for "Workflow receives current", select "no input" in "any application". In the Actions menu on the left, select "Utilities" > "Run Shell Script" (double click this). In the text box that appears, add the call to the utility. Automator scripts run with a reduced path for some reason, so you'll have to add to it. My script looks like this:

```bash
# This path is for homebrew and where I saved 'choose-link'
export PATH=/usr/local/bin:$PATH
choose-link
```

Once that's configured, save your Automator action and give it a name. Now open "System Preferences" and navigate to "Keyboard" > "Shortcuts". In "Services", when you scroll to the bottom, you'll see the action that you saved with the name that you gave it. Select it and click "Add Shortcut". I chose `option+command+space` (I had to unbind a finder search for this).

After all of this, it should be ready! You can edit the configuration in `~/.choose-link/links.json` to change the links and add more categories.
