import sys

if len(sys.argv)<3:
    print "Usage:"+" addhttp.py "+"filename"+" savefile"
    sys.exit()
wf=open(sys.argv[2],"r+")
def addhttp(filepath):
    f=open(filepath,"r")
    for url in f.readlines():
        url=url.strip("\r\n")
        if not url.startswith("http"):
            url="http://"+url
            wf.writelines(url+'\n')
        else:
            wf.writelines(url+"\n")



if __name__=="__main__":
    addhttp(sys.argv[1])