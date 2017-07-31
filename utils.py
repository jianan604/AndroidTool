import time
import os
def getCurrentTime():
    return time.strftime("%m%d%H%M%S")

def clearLog():
    os.system("adb shell logcat -c")

def getLog(logPath):
    logcatPath = os.path.join(logPath, "logcat.log")
    os.system("adb shell logcat -d > %s" % logcatPath)

def getLog(logPath):
    logcatPath = os.path.join(logPath, "logcat.log")
    os.system("adb shell logcat -d > %s" % logcatPath)

def getTraceData(logPath):
    os.system("adb pull /data/anr %s" % logPath)

def getCurrentTime():
    return time.strftime("%m%d%H%M%S")

        #if __name__ == "__main__":
#     compressFolder(r"E:\my_work\auto\RunUtils\src\logs\com.kingsoft.email")
    #print getDeviceInfo()