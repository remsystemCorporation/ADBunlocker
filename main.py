import colorama
from colorama import Fore, Style
from checkDevices.check_devices import check_python_installed, wait_for_device
from checkPackage.check_package import check_package

colorama.init(autoreset=True)

def main():
    if check_python_installed():
        print(f"{Fore.GREEN}Verificación de Python completada.{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}Error en la verificación de Python.{Style.RESET_ALL}")
        return
    
    print(f"{Fore.CYAN}Esperando conexión de dispositivo...{Style.RESET_ALL}")
    wait_for_device()

    print(f"{Fore.GREEN}¡Dispositivo detectado!{Style.RESET_ALL}")

    if check_package():
        print(f"{Fore.CYAN}Buscando paquetes...{Style.RESET_ALL}")
        

if __name__ == "__main__":
    main()

colorama.deinit()
