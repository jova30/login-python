usuario_correcto = "admin"
contrasena_correcta = "12345"

intentos = 0

while intentos < 3:

    usuario = input("Usuario: ")
    contrasena = input("Contraseña: ")

    if usuario == usuario_correcto and contrasena == contrasena_correcta:
        print("¡Bienvenido!")
        break
    else:
        intentos += 1
        print("Usuario o contraseña incorrectos.")
        print("Intentos restantes:", 3 - intentos)

if intentos == 3:
    print("Cuenta bloqueada.")