import sys
 
def getSistemaOperativo():
    plataforma = sys.platform
 
    if plataforma == "linux" or plataforma[:5] == "linux":
        return "linux"
    elif plataforma == "darwin":
        return "apple"
    elif plataforma == "win32":
        return "windows"
    else:
        # Para otros sistemas y variantes de Unix
        return "otro: "+plataforma
 
print("Mi sistema operativo es: "+getSistemaOperativo())
