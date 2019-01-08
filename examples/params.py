def sayHi(hi="Hola", who="Mundo"):
    print(hi,who)

sayHi() # Asigna por default los valores hi y who

sayHi('Hi') # Asigna por default el valor de who

sayHi(,'Michelle') # Esto no funciona

sayHi(who='Michelle') # Usando keywords para los parametros
