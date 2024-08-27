usuarios = []
reservas = []

def registrar_usuario():
    nombre_usuario = input('Ingrese el nombre de usuario para registrarse: ').strip()

    if nombre_usuario in usuarios:
        print('El nombre de usuario ya está registrado.')
        return

    usuarios.append(nombre_usuario)
    print(f'Usuario registrado con éxito: {nombre_usuario}')


def reservar_viaje():
    nombre_usuario = input('Ingrese tu nombre de usuario: ').strip()


    if nombre_usuario not in usuarios:
        print('El usuario no está registrado. Por favor regístrate primero.')
        if input('¿Deseas registrarte ahora? (s/n): ').strip().lower() == 's':
            registrar_usuario()
        else:
            return

    destino = input('Ingrese el destino del viaje: ').strip()
    fecha = input('Ingrese la fecha del viaje (YYYY-MM-DD): ').strip()


    if not fecha_valida(fecha):
        print('Fecha no válida. Por favor usa el formato YYYY-MM-DD.')
        return

    reservas.append({'usuario': nombre_usuario, 'destino': destino, 'fecha': fecha})
    print(f'Reserva añadida: {nombre_usuario} viaja a {destino} el {fecha}')

def ver_reservas():
    nombre_usuario = input('Ingrese el nombre de usuario para ver tus reservas: ').strip()

    if nombre_usuario not in usuarios:
        print('El usuario no está registrado.')
        return

    print(f'Reservas para {nombre_usuario}:')
    reservas_usuario = [r for r in reservas if r['usuario'] == nombre_usuario]

    if not reservas_usuario:
        print('No tienes reservas.')
        return

    for reserva in reservas_usuario:
        print(f'Destino: {reserva["destino"]}, Fecha: {reserva["fecha"]}')

def cancelar_reserva():
    nombre_usuario = input('Ingrese el nombre de usuario para cancelar una reserva: ').strip()

    if nombre_usuario not in usuarios:
        print('El usuario no está registrado.')
        return

    reservas_usuario = [r for r in reservas if r['usuario'] == nombre_usuario]

    if not reservas_usuario:
        print('No tienes reservas para cancelar.')
        return

    print('Tus reservas:')
    for idx, reserva in enumerate(reservas_usuario, start=1):
        print(f'{idx}. Destino: {reserva["destino"]}, Fecha: {reserva["fecha"]}')

    seleccion = input('Selecciona el número de la reserva que deseas cancelar: ').strip()

    if seleccion.isdigit():
        seleccion = int(seleccion)
        if 1 <= seleccion <= len(reservas_usuario):
            reserva_a_cancelar = reservas_usuario[seleccion - 1]
            reservas.remove(reserva_a_cancelar)
            print(f'Reserva cancelada: {reserva_a_cancelar["usuario"]} viaja a {reserva_a_cancelar["destino"]} el {reserva_a_cancelar["fecha"]}')
        else:
            print('Selección no válida.')
    else:
        print('Entrada no válida. Por favor introduce un número.')

def fecha_valida(fecha):
    if len(fecha) != 10 or fecha[4] != '-' or fecha[7] != '-':
        return False

    año = fecha[0:4]
    mes = fecha[5:7]
    día = fecha[8:10]

    if not (año.isdigit() and mes.isdigit() and día.isdigit()):
        return False

    año = int(año)
    mes = int(mes)
    día = int(día)

    if año < 1900 or año > 2100:
        return False
    if mes < 1 or mes > 12:
        return False
    if día < 1 or día > 31:
        return False

    if mes in [4, 6, 9, 11] and día > 30:
        return False
    if mes == 2:
        if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
            if día > 29:
                return False
        else:
            if día > 28:
                return False

    return True


def menu():
    while True:
        print('\nSistema de Reservas')
        print('1. Registrar un usuario')
        print('2. Reservar un viaje')
        print('3. Ver reservas')
        print('4. Cancelar una reserva')
        print('5. Salir')
        opcion = input('Selecciona una opción: ').strip()

        if opcion == '1':
            registrar_usuario()
        elif opcion == '2':
            reservar_viaje()
        elif opcion == '3':
            ver_reservas()
        elif opcion == '4':
            cancelar_reserva()
        elif opcion == '5':
            print('Saliendo...')
            break
        else:
            print('Opción no válida. Inténtalo de nuevo.')

if __name__ == '__main__':
    menu()