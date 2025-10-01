# validacion de contraseña
import re

print(f"🔒 INGRESE UNA CONTRASEÑA\n"
      "- Con al menos una mayúscula\n"
      "- Con al menos una minúscula\n"
      "- Con al menos un número\n"
      "- Con al menos un caracter especial\n")

contraseña = input("contraseña: ")
isValid = True

if len(contraseña) >= 8:
    print(contraseña)

    if not re.search(r"[a-z]", contraseña):
        print("❌ No contiene minúsculas")
        isValid = False
    if not re.search(r"[A-Z]", contraseña):
        print("❌ No contiene mayúsculas")
        isValid = False
    if not re.search(r"[0-9]", contraseña):
        print("❌ No contiene números")
        isValid = False
    if not re.search(r"[^A-Za-z0-9]", contraseña): 
        print("❌ No contiene caracter especial")
        isValid = False
else:
    print("❌ La contraseña debe tener mínimo 8 caracteres")
    isValid = False

if isValid:
    print("🔐 CONTRASEÑA VÁLIDA")
else:
    print("CONTRASEÑA INVALIDA")
