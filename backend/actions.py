import platform
import subprocess


def verificar_windows():
    if platform.system() != "Windows":
        raise Exception("Esta función solo está disponible en Windows.")


def ejecutar_comando(comando: str):
    subprocess.run(comando, shell=True, check=True)


def vaciar_papelera():
    verificar_windows()
    comando = 'PowerShell -Command "Clear-RecycleBin -Force"'
    ejecutar_comando(comando)


def abrir_limpieza_disco():
    verificar_windows()
    ejecutar_comando("cleanmgr")


def abrir_administrador_tareas():
    verificar_windows()
    ejecutar_comando("taskmgr")


def abrir_config_inicio():
    verificar_windows()
    ejecutar_comando("start ms-settings:startupapps")
