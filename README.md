# DiamondBack
A backup utility written in python and uses the tar for compression.

### Features:
- Configuration is managed via json file
- Uses flat text files to manage the files and directories for backup as well as being ignored
- Uses a set log file to keep track of progress of backups
- Contains section to allow for redunant backups
- Has a hard coded section to purge files

### Purge Files:
- This section is hard coded at the time being.  
- For right now, I keep a cron set to run every day that determines if it is the last day of the month.  If it is, then run the script.
*0 5 * * * [[ "$(date --date=tomorrow +\%d)" == "01" ]] && python3 /home/curtis/Scripts/DiamondBack/DiamondBack.py*
- Before the backup starts, it will check the mtime of the files and find the files that are of the same year, the same month and are less than current day.  If they are, then delete them.  After the files are purged, the backup resumes.

- This is done so that at the end of the month, any backup files for that month previously created will be delted and then a new backup is done.  Cuts down on previous backups.
