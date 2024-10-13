import subprocess
import time
import sys
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)


def check_adb_installed():
    try:
        subprocess.run(["adb", "version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except FileNotFoundError:
        answer = input(f"{Fore.YELLOW}¿Deseas instalar ADB y las dependencias necesarias? (Y/N): {Style.RESET_ALL}").strip().upper()
        if answer == 'Y':
            install_dependencies()
        return False
    
def check_python_installed():
    try:
        version = sys.version
        print(f"{Fore.GREEN}Python está instalado: {version}{Style.RESET_ALL}")
        return True
    except Exception as e:
        print(f"{Fore.RED}Python no está instalado o no se está ejecutando correctamente: {e}{Style.RESET_ALL}")
        return False

def install_dependencies():
    try:
        print(f"{Fore.CYAN}Instalando dependencias desde requirements.txt...{Style.RESET_ALL}")
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], check=True)
        print(f"{Fore.GREEN}Dependencias instaladas con éxito.{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Error al instalar dependencias: {e}{Style.RESET_ALL}")


def check_device_connected():
    try:
        if check_adb_installed():
            result = subprocess.run(["adb", "devices"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output = result.stdout.decode('utf-8').strip().splitlines()

            devices = [line for line in output[1:] if line.strip()]
            if devices:
                for device in devices:
                    if "device" in device and "unauthorized" not in device:
                        print(f"{Fore.GREEN}Dispositivo conectado y en modo depuración USB.{Style.RESET_ALL}")
                        return True
        return False
    except Exception as e:
        print(f"{Fore.RED}Error al verificar el dispositivo: {e}{Style.RESET_ALL}")
        return False

def wait_for_device():
    waiting_message_shown = False
    while True:
        if check_device_connected():
            break
        if not waiting_message_shown:
             print(f"{Fore.YELLOW}Esperando que el dispositivo se conecte o se active la depuración USB...{Style.RESET_ALL}")
             waiting_message_shown=True;
        time.sleep(2);

colorama.deinit()