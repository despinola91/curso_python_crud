PASSWORD = '12345'


def password_required(func): #el decorador recibe como parámetro la función principal
    def wrapper():
        password = input('Cual es tu password?')

        if password == PASSWORD:
            return func()
        else:
            print('La password no es correcta')
    
    return wrapper

@password_required #la funcion tiene un decorador que nos permite ejecutar lógica ANTES y DESPUÉS de la funcion principal
def needs_password():
    print('La contraseña es correcta')


def upper(func): #el decorador recibe como parámetro la función principal
    def wrapper(*args, **kwargs): #el wrapper que ejecuta la función principal también recibe *args y **kwargs representando a los parámetros que recibe la función principal para poder enviarlos también
        result = func(*args, **kwargs)
        return result.upper()

    return wrapper

@upper #la función tiene un decorador que nos permite ejecutar lógica ANTES y DESPUES de la función principal
def say_my_name(name):
    return 'Hola {}'.format(name)


if __name__ == '__main__':
    print(say_my_name('Dario'))
    #needs_password() #llamamos a la funcion principal
