tell application "Terminal"
	do shell script "source ~/.bash_profile;echo $PATH;conda activate base;python ~/code/gui.py"
end tell
