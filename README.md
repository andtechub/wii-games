# wii-games
With the simple script you can download games for the Wii. The prerequisite for this is the homebrew channel of a jailbroken Wii. Only EU games are downloaded in this configuration. For US games, the xml_url for the US file must be adapted.

# How to
- Make sure that Python 3.x is installed on your system. Download the Python files. Create a folder in which the games are to be saved. Then you can execute the Python files. <br>
- To make the games usable for the Wii you need the Wii-Backup-Manager. You can download it <a href="https://wiidatabase.de/downloads/pc-tools/wii-backup-manager/">here.</a> I am uploading the current version of the Wii Backup Manager in case the source does not work.

# Unzip
- The games are downloaded in a zip file. Create the "zip" and "wbfs" folders.
- Then move all zip files into the zip folder.
- Download the unzip.py file and adjust the paths in the file. The files are stored temporarily in the Temp folder. These are deleted when the files are in the target folder.
```
ordner_pfad = "path/to/zip/files" 
entpackungsziel = "/path/to/temp/folder"
zielordner = "/path/to/wbfs/folder"
```
- Then execute the unzip.py file. This will unzip all zip files and move them to the wbfs folder. The files in the zip folder will not be deleted!
- Make sure that you have enough storage space. One to two terabytes should be enough.

# Disclaimer
All games are downloaded from archive.org. Source: <a href="https://archive.org/details/wiieuroperedump">https://archive.org/details/wiieuroperedump</a> <br>
I take no responsibility for copyright infringement and I do not distribute protected content. All content is publicly available via archive.org.

# Info
Source of the XML files of the EU and US versions
**EU**
- `https://ia904707.us.archive.org/2/items/wiieuroperedump/wiieuroperedump_files.xml`
- `https://ia902904.us.archive.org/31/items/wiieuroperedump2/wiieuroperedump2_files.xml`
- `https://ia902903.us.archive.org/27/items/wiieuroperedump3/wiieuroperedump3_files.xml`

**US**
- `https://ia902903.us.archive.org/1/items/wiiusaredump/wiiusaredump_files.xml`
- `https://ia800504.us.archive.org/28/items/wiiusaredump2/wiiusaredump2_files.xml`
- `https://ia600501.us.archive.org/29/items/wiiusaredump3/wiiusaredump3_files.xml`

**Japan**
- `https://ia802904.us.archive.org/4/items/wiijapanredump/wiijapanredump_files.xml`
- ``
