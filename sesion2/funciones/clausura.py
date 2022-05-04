def outerFunction(texto): 
    text = texto
    
    def innerFunction():
        print(text)
    
    return innerFunction
    
if __name__ == '__main__':
    myFunction = outerFunction("Python3") 
    myFunction()

