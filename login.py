usuario_correcto = "admin"
contrasena_correcta = "12345"

usuario = input("Usuario: ")
contrasena = input("Contraseña: ")

if usuario == usuario_correcto and contrasena == contrasena_correcta:
    print("¡Bienvenido!")
else:
    print("Usuario o contraseña incorrectos.")