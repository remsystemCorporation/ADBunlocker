import subprocess
import sys
import colorama
from colorama import Fore, Style
from checkDevices.check_devices import wait_for_device

colorama.init(autoreset=True)

def check_package():
    try:
        result = subprocess.run(["adb", "shell", "pm", "list", "packages", "-f"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = result.stdout.decode('utf-8')
        package_name = "co.sitic.pp"

        if package_name in output:
            print(f"{Fore.GREEN}Paquete '{package_name}' encontrado.{Style.RESET_ALL}")
            answer = input(f"{Fore.YELLOW}¿Desea desinstalar el paquete de bloqueo? (Y/N): {Style.RESET_ALL}").strip().upper()
            if answer == "Y":
                uninstall_result = subprocess.run(["adb", "shell", "pm", "uninstall", "--user", "0", package_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                print(uninstall_result)
                if uninstall_result.returncode == 0:
                    print(f"{Fore.GREEN}Paquete de bloqueo eliminado correctamente.{Style.RESET_ALL}",f"{uninstall_result.stdout}")
                    return True
                else:
                    print(f"{Fore.RED}Error al desinstalar el paquete.{Style.RESET_ALL}")
                    return False
            else:
                print(f"{Fore.CYAN}No se desinstaló el paquete de bloqueo.{Style.RESET_ALL}")
                return False
        else:
            print(f"{Fore.RED}No se encontró el paquete de bloqueo.{Style.RESET_ALL}")
            return False

    except Exception as e:
        print(f"{Fore.RED}Error al buscar o eliminar paquetes: {e}{Style.RESET_ALL}")
        return False
colorama.deinit()
