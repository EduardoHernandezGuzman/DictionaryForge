import sys
import time
import os

# Colores
yellow = "\033[93m"
green = "\033[92m"
cyan = "\033[96m"
pink = "\033[95m"
red = "\033[91m"
b = "\033[1m"
reset = "\033[0m"


def print_progress_bar(progress):
    bar_length = 20
    filled_length = int(bar_length * progress / 100)
    bar = "█" * filled_length + "░" * (bar_length - filled_length)
    print(f"\r{green}[{bar}] {progress}%{reset}", end="", flush=True)
    time.sleep(0.4)


def print_stats(total, tiempo, nombre):
    print("\n" + "═" * 50)
    print(f"{cyan}█ Estadísticas del Diccionario{reset}")
    print("═" * 50)
    print(f"{yellow}► Total de contraseñas: {reset}{total}")
    print(f"{yellow}► Tiempo de generación: {reset}{tiempo:.2f} segundos")
    print(f"{yellow}► Velocidad: {reset}{int(total/tiempo)} contraseñas/segundo")
    print(f"{yellow}► Archivo: {reset}{nombre}")
    print("═" * 50 + "\n")


# Banner
print(
    red
    + b
    + """
╔══════════════════════════════════════════════════════════════════════════════╗
║ ██████╗ ██╗ ██████╗████████╗██╗ ██████╗ ███╗   ██╗ █████╗ ██████╗ ██╗   ██╗  ║
║ ██╔══██╗██║██╔════╝╚══██╔══╝██║██╔═══██╗████╗  ██║██╔══██╗██╔══██╗╚██╗ ██╔╝  ║
║ ██║  ██║██║██║        ██║   ██║██║   ██║██╔██╗ ██║███████║██████╔╝ ╚████╔╝   ║
║ ██║  ██║██║██║        ██║   ██║██║   ██║██║╚██╗██║██╔══██║██╔══██╗  ╚██╔╝    ║
║ ██████╔╝██║╚██████╗   ██║   ██║╚██████╔╝██║ ╚████║██║  ██║██║  ██║   ██║     ║
║ ╚═════╝ ╚═╝ ╚═════╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝     ║
║     ███████╗ ██████╗ ██████╗  ██████╗ ███████╗                               ║
║     ██╔════╝██╔═══██╗██╔══██╗██╔════╝ ██╔════╝                               ║
║     █████╗  ██║   ██║██████╔╝██║  ███╗█████╗                                 ║
║     ██╔══╝  ██║   ██║██╔══██╗██║   ██║██╔══╝                                 ║
║     ██║     ╚██████╔╝██║  ██║╚██████╔╝███████╗                               ║
║     ╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝                               ║
║                                                        By Edo - Version 1.0  ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""
    + reset
)

comienzo = time.time()


def ayuda():
    print(
        "\nManual de uso de generador.py: \n\n generador.py requiere un mínimo de 3 argumentos para su ejecución. \n Si deseas omitir alguno, sustitúyelo por '-e'. \n\n Ejemplo: python generador.py casa -e cocodrilo \n\n-Parámetros-\n  -a: Permite agregar una conjunción en tu idioma para combinar las contraseñas.\n      Debe ir seguido de la conjunción (python generador.py coche pedro rata -a y)\n  -e: Omite el argumento correspondiente a su posición\n  -h: Despliega este mensaje de ayuda\n  -n: Agregado después del tercer argumento, indica a generador.py que incluya números en las contraseñas resultantes\n  -b: Busca coincidencias en un diccionario preexistente\n      que DEBE ubicarse en la carpeta 'Generated'.\n      Si el nombre del diccionario contiene espacios, debe encerrarse entre comillas.\n      (Ej: python generador.py -b casa \"Dictionary-Mon Dic 13 21:14:22 2024\"). \n\nPrograma creado por Edo\n"
    )


def busca(secuencia, arch):
    if secuencia == "" or arch == "":
        return "e"
    try:
        os.chdir("Generated")
        archivo = open(nmb, "r")
        lineas = archivo.readlines()
        coincidencia = False
        i = 0
        for x in lineas:
            i += 1
            if secuencia in x and len(x) == len(secuencia) + 1:
                coincidencia = str(i)
                break

        if coincidencia != False:
            return coincidencia
        else:
            return "no"
    except:
        return "e"


class Diccionario:
    def __init__(self, pri, seg, ter, num, conjun, fecha):

        self.palabra = [pri, seg, ter]

        for x in range(3):
            if len(self.palabra[x]) <= 1:
                print(
                    "\n¡Los parámetros deben tener mínimo 2 caracteres! \nEscribe 'python generador.py -h' para ayuda\n"
                )
                exit()
            if self.palabra[x] == "-e":
                self.palabra[x] = ""

        if (
            self.palabra[0] == self.palabra[1]
            or self.palabra[0] == self.palabra[2]
            or self.palabra[1] == self.palabra[2]
        ):
            i = 0
            for x in range(3):
                if self.palabra[x] == "":
                    i += 1
            if x >= 2:
                pass
            else:
                print(
                    "\n¡No puedes usar la misma palabra dos veces! \nEscribe 'python generador.py -h' para ayuda\n"
                )
                exit()

        self.num = num
        self.fecha = fecha
        self.conj = conjun
        if os.path.exists("Generated") == False:
            os.mkdir("Generated")
        os.chdir("Generated")

        self.nombre = "Dictionary-" + self.fecha
        self.archivo = open(self.nombre, "a")

    def pumayus(self, clave):
        return clave.title()[:-1] + clave[-1].upper()

    def umayus(self, clave):
        return clave[:-1] + clave[-1].upper()

    def pmayus(self, clave):
        return clave.title()

    def mayus(self, clave):
        return clave.upper()

    def vocales(self, clave):
        resultado = clave.replace("a", "4")
        resultado = resultado.replace("A", "4")
        resultado = resultado.replace("e", "3")
        resultado = resultado.replace("E", "4")
        resultado = resultado.replace("o", "0")
        resultado = resultado.replace("O", "0")

        return resultado

    def guionbajo(self, clave):
        resultado = "_" + clave
        return resultado

    def getArchivo(self):
        return self.archivo

    def escribe(self, clave):
        archivo = self.archivo
        if len(clave) > 0:
            k = False
            claveNumerica = self.vocales(clave)
            for j in range(2):
                archivo.write(clave + "\n")
                archivo.write(self.mayus(clave) + "\n")
                archivo.write(self.pmayus(clave) + "\n")
                archivo.write(self.umayus(clave) + "\n")
                archivo.write(self.pumayus(clave) + "\n")

                archivo.write(self.guionbajo(clave) + "\n")
                archivo.write(self.mayus(self.guionbajo(clave)) + "\n")
                archivo.write(self.pmayus(self.guionbajo(clave)) + "\n")
                archivo.write(self.umayus(self.guionbajo(clave)) + "\n")
                archivo.write(self.pumayus(self.guionbajo(clave)) + "\n")

                archivo.write(claveNumerica + "\n")
                archivo.write(self.mayus(claveNumerica) + "\n")
                archivo.write(self.pmayus(claveNumerica) + "\n")
                archivo.write(self.umayus(claveNumerica) + "\n")
                archivo.write(self.pumayus(claveNumerica) + "\n")

                archivo.write(self.guionbajo(self.guionbajo(claveNumerica)) + "\n")
                archivo.write(self.mayus(self.guionbajo(claveNumerica)) + "\n")
                archivo.write(self.pmayus(self.guionbajo(claveNumerica)) + "\n")
                archivo.write(self.umayus(self.guionbajo(claveNumerica)) + "\n")
                archivo.write(self.pumayus(self.guionbajo(claveNumerica)) + "\n")

                if k != True:
                    clave = clave + "A"
                    claveNumerica = claveNumerica + "A"
                    k = True

            clave = clave[0:-1]
            claveNumerica = claveNumerica[0:-1]
            k = False

            if self.num == True:
                for n in range(10000):
                    if n < 10:
                        n = "0" + str(n)
                        k = False
                        for j in range(2):
                            archivo.write(clave + n + "\n")
                            archivo.write(self.mayus(clave) + n + "\n")
                            archivo.write(self.pmayus(clave) + n + "\n")
                            archivo.write(self.umayus(clave) + n + "\n")
                            archivo.write(self.pumayus(clave) + n + "\n")

                            archivo.write(clave + n + "\n")
                            archivo.write(self.mayus(self.guionbajo(clave)) + n + "\n")
                            archivo.write(self.pmayus(self.guionbajo(clave)) + n + "\n")
                            archivo.write(self.umayus(self.guionbajo(clave)) + n + "\n")
                            archivo.write(
                                self.pumayus(self.guionbajo(clave)) + n + "\n"
                            )

                            archivo.write(self.vocales(clave) + n + "\n")
                            archivo.write(self.mayus(self.vocales(clave)) + n + "\n")
                            archivo.write(self.pmayus(self.vocales(clave)) + n + "\n")
                            archivo.write(self.umayus(self.vocales(clave)) + n + "\n")
                            archivo.write(self.pumayus(self.vocales(clave)) + n + "\n")

                            archivo.write(
                                self.vocales(self.guionbajo(clave)) + n + "\n"
                            )
                            archivo.write(
                                self.mayus(self.vocales(self.guionbajo(clave)))
                                + n
                                + "\n"
                            )
                            archivo.write(
                                self.pmayus(self.vocales(self.guionbajo(clave)))
                                + n
                                + "\n"
                            )
                            archivo.write(
                                self.umayus(self.vocales(self.guionbajo(clave)))
                                + n
                                + "\n"
                            )
                            archivo.write(
                                self.pumayus(self.vocales(self.guionbajo(clave)))
                                + n
                                + "\n"
                            )

                            if k != True:
                                n = str(n) + "A"
                                k = True

                        n = n[:-1]
                        k = False
                    for j in range(2):
                        archivo.write(clave + str(n) + "\n")
                        archivo.write(self.mayus(clave) + str(n) + "\n")
                        archivo.write(self.pmayus(clave) + str(n) + "\n")
                        archivo.write(self.umayus(clave) + str(n) + "\n")
                        archivo.write(self.pumayus(clave) + str(n) + "\n")

                        archivo.write(self.guionbajo(clave) + str(n) + "\n")
                        archivo.write(self.mayus(self.guionbajo(clave)) + str(n) + "\n")
                        archivo.write(
                            self.pmayus(self.guionbajo(clave)) + str(n) + "\n"
                        )
                        archivo.write(
                            self.umayus(self.guionbajo(clave)) + str(n) + "\n"
                        )
                        archivo.write(
                            self.pumayus(self.guionbajo(clave)) + str(n) + "\n"
                        )

                        archivo.write(self.vocales(clave) + str(n) + "\n")
                        archivo.write(self.mayus(self.vocales(clave)) + str(n) + "\n")
                        archivo.write(self.pmayus(self.vocales(clave)) + str(n) + "\n")
                        archivo.write(self.umayus(self.vocales(clave)) + str(n) + "\n")
                        archivo.write(self.pumayus(self.vocales(clave)) + str(n) + "\n")

                        archivo.write(
                            self.vocales(self.guionbajo(clave)) + str(n) + "\n"
                        )
                        archivo.write(
                            self.mayus(self.vocales(self.guionbajo(clave)))
                            + str(n)
                            + "\n"
                        )
                        archivo.write(
                            self.pmayus(self.vocales(self.guionbajo(clave)))
                            + str(n)
                            + "\n"
                        )
                        archivo.write(
                            self.umayus(self.vocales(self.guionbajo(clave)))
                            + str(n)
                            + "\n"
                        )
                        archivo.write(
                            self.pumayus(self.vocales(self.guionbajo(clave)))
                            + str(n)
                            + "\n"
                        )

                        if k != True:
                            n = str(n) + "A"
                            k = True

                    n = n[:-1]
                    k = False

    def simple(self):
        for i in range(3):
            self.escribe(self.palabra[i])

    def plano(self):
        resultado = self.palabra[0] + self.palabra[1] + self.palabra[2]
        self.escribe(resultado)

    def inverso(self):
        resultado = self.palabra[2] + self.palabra[1] + self.palabra[0]
        self.escribe(resultado)

    def silabas(self):
        si1 = self.palabra[0][:2]
        si2 = self.palabra[1][:2]
        si3 = self.palabra[2][:2]

        resultado = si1 + si2 + si3
        self.escribe(resultado)

    def conjuncion(self):
        if self.conj != "":
            for i in range(0, 3):
                mezcla = (
                    self.palabra[i]
                    + self.conj
                    + self.palabra[i]
                    + self.conj
                    + self.palabra[i]
                )
                self.escribe(mezcla)
                mezcla = self.palabra[i] + self.conj + self.palabra[i]
                self.escribe(mezcla)
            for i in range(0, 2):
                mezcla = (
                    self.palabra[i]
                    + self.conj
                    + self.palabra[i + 1]
                    + self.conj
                    + self.palabra[i + 1]
                )
                self.escribe(mezcla)

                mezcla = (
                    self.palabra[i + 1]
                    + self.conj
                    + self.palabra[i]
                    + self.conj
                    + self.palabra[i + 1]
                )
                self.escribe(mezcla)

                mezcla = (
                    self.palabra[i + 1]
                    + self.conj
                    + self.palabra[i]
                    + self.conj
                    + self.palabra[i]
                )
                self.escribe(mezcla)

                mezcla = (
                    self.palabra[i]
                    + self.conj
                    + self.palabra[i]
                    + self.conj
                    + self.palabra[i + 1]
                )
                self.escribe(mezcla)

                mezcla = (
                    self.palabra[i]
                    + self.conj
                    + self.palabra[i + 1]
                    + self.conj
                    + self.palabra[i]
                )
                self.escribe(mezcla)

                mezcla = (
                    self.palabra[i + 1]
                    + self.conj
                    + self.palabra[i + 1]
                    + self.conj
                    + self.palabra[i]
                )
                self.escribe(mezcla)

                mezcla = self.palabra[i] + self.conj + self.palabra[i + 1]
                self.escribe(mezcla)

                mezcla = self.palabra[i + 1] + self.conj + self.palabra[i]
                self.escribe(mezcla)

    def juntar(self):
        n = 0
        while n <= 2:
            for i in range(0, 3):
                resultado = self.palabra[n] + self.palabra[i]
                self.escribe(resultado)
            n += 1

    def contar(self):
        self.archivo.close()
        archivo = open(self.nombre, "r")
        lineas = list(archivo)
        return len(lineas)


numeros = False
conjun = ""

if len(sys.argv) >= 3:
    if sys.argv[1] == "-b":
        busqueda = sys.argv[2]
        nmb = sys.argv[3]
        rsult = busca(busqueda, nmb)
        if rsult == "e":
            print(
                "Comprueba los parámetros de búsqueda. Usa 'python generador.py -h' para ayuda."
            )
        elif rsult == "no":
            print("No se encontraron coincidencias para '") + busqueda + "'."
        else:
            print("¡Coincidencia encontrada! Línea ") + rsult
        exit()

if len(sys.argv) >= 5:
    if sys.argv[4] == "-n":
        numeros = True
    elif sys.argv[4] == "-a":
        conjun = sys.argv[5]

    if len(sys.argv) == 7:
        if sys.argv[5] == "-a":
            conjun = sys.argv[6]
        elif sys.argv[4] == "-a" and sys.argv[6] == "-n":
            conjun = sys.argv[5]
            numeros = True

elif len(sys.argv) == 2:
    if sys.argv[1] == "-h":
        ayuda()

try:
    dicc = Diccionario(
        sys.argv[1], sys.argv[2], sys.argv[3], numeros, conjun, time.strftime("%c")
    )
    print(cyan + "Generando tu diccionario..." + reset)
    dicc.simple()
    print_progress_bar(13)
    dicc.plano()
    print_progress_bar(31)
    dicc.inverso()
    print_progress_bar(49)
    dicc.silabas()
    print_progress_bar(75)
    dicc.conjuncion()
    print_progress_bar(100)
    dicc.juntar()
    print("\n")
    print(green + "\n\n\a¡Diccionario creado!" + reset)
    fin = time.time()
    tiempo_total = fin - comienzo
    total_passwords = dicc.contar()
    print_stats(total_passwords, tiempo_total, dicc.nombre)
except:
    ayuda()

    exit()