import ctypes

# Charger le fichier DLL
lib = ctypes.CDLL("./demos/18_demo_c/demo_c.dll")

# Utilisation des fonctions
print(lib.add(10, 5))

x = ctypes.c_int(42)
lib.increment(ctypes.byref(x))
print(x.value)

arr = (ctypes.c_int * 4)(1,2,3,4)

lib.print_message(b'Hello from python')