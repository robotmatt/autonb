
# autonb-t

Automated way to do NAVBLUE schedule runs

### Fresh install of python3 and selenium on High Sierra

Install homebrew

xcode tools

install python via brew

can be refereced via python3 pip3

https://docs.brew.sh/Homebrew-and-Python

* 1. 1. `brew install --cask chromedriver`
* Install some sort of IDE. CodeRunner via the appstore. Can download
  PyCharm community edition from their website or use homebrew.
  1. `brew install --cask pycharm-ce`

https://www.jetbrains.com/toolbox-app/

**/opt/homebrew/bin/chromedriver**

To run:

change settings in config file
allow securirty
download chrome

Keep homebrew up to date

[](https://github.com/robotmatt/autonb#keep-homebrew-up-to-date)

##### From [https://docs.brew.sh/FAQ](https://docs.brew.sh/FAQ)

[](https://github.com/robotmatt/autonb#from-httpsdocsbrewshfaq)

To update homebrew:
`brew update`

To find out what is out of date:
`brew outdated`

Upgrade everything with:
`brew upgrade`

To list the versions of installed casks:
`brew cask list --versions`

As of December 2017, you can also keep Brew Cask up to date ([per Stack Overflow](https://stackoverflow.com/questions/31968664/upgrade-all-the-casks-installed-via-homebrew-cask))
`brew cask upgrade`

However this will not update casks that do not have
versioning information (version :latest) or applications that have a
built-in upgrade mechanism (auto_updates true). To reinstall these casks
 (and consequently upgrade them if upgrades are available), run the
upgrade command with the --greedy flag like this:
`brew cask upgrade --greedy`
