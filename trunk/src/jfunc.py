import platform, os, commands, glob

osname=platform.uname()[0].lower()
print "Your os is:%s"%osname
if osname=="darwin":
	brew_prefix=commands.getstatusoutput('brew --prefix')[1]
	sitepackagesLocations=[
		os.path.expanduser("~/Library/Python/2.7/lib/python/site-packages"),
		"/usr/local/lib/python2.7/site-packages/",
		"/Library/Python/2.7/site-packages"
		]
elif osname=="linux":
	sitepackagesLocations=[
		os.path.expanduser("~/.local/lib/python2.7/site-packages"),
		"/usr/local/lib/python2.7/dist-packages",
		"/usr/lib/python2.7/dist-packages",
		"/usr/lib/python2.7/site-packages",
		]
elif osname=="windows":
	sitepackagesLocations=[
		os.path.expanduser("~\\appdata\\roaming\\python\\python27\\site-packages"),
		"C:\\Python27\\Lib\\site-packages"
		]
def runCmd4Files(pwd,cmd,mfiles):
	for mfile in mfiles:
		#print mfile
		mfile=os.path.join(pwd,mfile)
		mfiles=glob.glob(mfile)
		for mfile in mfiles:
			#if "*" in mfile or os.path.exists(mfile):
			if os.path.exists(mfile):
				rmStr='%s %s'%(cmd,mfile)
				print rmStr
				os.system(rmStr)
			else:
				print "%s cannot be removed"%mfile

def runRm4Dirs(pwd,mfiles):
	if osname != "windows":
		rmDirCmd="rm -rf"
	else:
		rmDirCmd="rd /S /Q"

	runCmd4Files(pwd,rmDirCmd,mfiles)

def runRm4Files(pwd,mfiles):
	if osname != "windows":
		rmFileCmd="rm -rf"
	else:
		rmFileCmd="del /S /Q"

	runCmd4Files(pwd,rmFileCmd,mfiles)

if __name__ == "__main__":
	print "os is %s"%osname