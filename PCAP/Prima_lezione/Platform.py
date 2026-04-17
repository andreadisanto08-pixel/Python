import platform

print(platform.platform())
print(platform.platform(0,1)) #mostra (prima parola,seconda parola)
print(platform.machine())
print(platform.system())
print(platform.processor())
print(platform.version())

print(platform.python_implementation()) 
for i in platform.python_version_tuple(): #stampa la tua version in fila
    print(i);

