def loginUsuario(user):
    if user.isalnum()==False:
        print("'El usuario solo puede contener letras y numeros'")
    elif 6 > len(user):
        print("'El nombre de usuario debe poseer un minimo de 6 caracteres'")     
    elif 12 < len(user):
        print("'El nombre no debe de contener mayor a 12 caracteres'")
    elif 6 <= len(user) <=12:
        print("'USUARIO VALIDO'")
    return

def loginContraseña(password):
    if 8 > len(password):
        print("'La contraseña debe contener un maximo de 8 caracteres'") 
    elif password.count(" ")>0:
        print("'La contraseña no debe tener espacios en blancos'")

    elif 8 == len(password):
        print("'CONTRASEÑA VALIDA'") 

    return