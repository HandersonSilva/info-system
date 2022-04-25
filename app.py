import os, sys
import platform,socket,psutil
from tkinter import *

 
def verificarSistema():
    info={}
    info['platform']=platform.system()
    info['platform-release']=platform.release()
    info['platform-version']=platform.version()
    info['architecture']=platform.machine()
    info['hostname']=socket.gethostname()
    info['processor']=platform.processor()
    info['ram']=str(round(psutil.virtual_memory().total / (1024.0 **3)))
    info['ram-percent']=str(round(psutil.virtual_memory().percent))
    info['cpu']=str(psutil.cpu_count())
    info['cpu-freq']=str(round(psutil.cpu_freq().current))
    info['cpu-freq-max']=str(round(psutil.cpu_freq().max))
    info['cpu-freq-min']=str(round(psutil.cpu_freq().min))
    info['cpu-percent']=str(round(psutil.cpu_percent()))     
    info['ip']=socket.gethostbyname(socket.gethostname())
    info['serial']=getMachine_addr()
   
    text = f'''
    platform: {info['platform']}
    platform-release: {info['platform-release']}
    platform-version: {info['platform-version']}
    architecture: {info['architecture']}
    hostname: {info['hostname']}
    processor: {info['processor']}
    ram: {info['ram']} GB
    ram-percent: {info['ram-percent']} %
    cpu: {info['cpu']}
    cpu-freq: {info['cpu-freq']} MHz
    cpu-freq-max: {info['cpu-freq-max']} MHz
    cpu-freq-min: {info['cpu-freq-min']} MHz
    cpu-percent: {info['cpu-percent']} %
    ip: {info['ip']}
    serial: {info['serial']}
    '''
    text_info["text"] = text


def getMachine_addr():
	os_type = sys.platform.lower()
	if "win" in os_type:
		command = "wmic bios get serialnumber"
	elif "linux" in os_type:
		command = "dmidecode -s baseboard-serial-number"
	elif "darwin" in os_type:
		command = "ioreg -l | grep IOPlatformSerialNumber"
	return os.popen(command).read().replace("\n","").replace("	","").replace(" ","")

window = Tk()
window.title("Get Info")
window.geometry("500x400")

text_button = Label(window, text="Informação do Sistema Operacional")
text_button.grid(column=0, row=0, padx=135, pady=0)

button = Button(window, text="Verificar", command=verificarSistema)
button.grid(column=0, row=1, padx=135, pady=10)

text_info = Label(window, text="")
text_info.grid(column=0, row=2)

window.mainloop()
