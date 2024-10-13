# ADBUnlocker

Este script permite eliminar el paquete de bloqueo de los teléfonos de **Telcel** que han sido adquiridos a crédito o prepago y corren riesgo de ser bloqueados por falta de pago. El paquete es parte del sistema de Telcel y no puede desinstalarse con aplicaciones convencionales.

## Requisitos previos

1. **ADB**: Debes tener ADB instalado en tu sistema.
   - Si no lo tienes instalado, sigue estas instrucciones:
     - **Windows**: [Descargar ADB desde Android Developers](https://developer.android.com/studio/releases/platform-tools).
     - **Linux (Debian/Ubuntu)**: `sudo apt install adb`
     - **MacOS**: `brew install android-platform-tools`
   - Verifica la instalación ejecutando `adb version` en la terminal.

2. **Python**: Asegúrate de tener **Python** instalado.
   - Verifica la instalación ejecutando `python --version` o `python3 --version` en la terminal.

3. **Modo administrador**: Para evitar problemas de permisos, ejecuta el script en **modo administrador**.

4. **Teléfono conectado**: Solo debe haber **un teléfono conectado en modo depuración USB** al sistema para evitar errores.

   - Activa la depuración USB en tu teléfono:
     - Ve a **Configuración** -> **Acerca del teléfono** -> **Número de compilación** (toca varias veces para activar las opciones de desarrollador).
     - Ve a **Opciones de desarrollador** -> **Activar depuración USB**.

## ¿Cómo funciona?

Este script está diseñado específicamente para teléfonos de **Telcel** adquiridos bajo **plan de crédito** o **prepago** que contienen una aplicación del sistema que bloquea el dispositivo en caso de impago. El paquete a eliminar es `co.sitic.pp`.

### Casos en los que puedes usar este script:

1. **Teléfonos adquiridos a crédito en Telcel**: Si tu teléfono fue adquirido a crédito en Telcel, es posible que contenga el paquete `co.sitic.pp`, que puede bloquear tu dispositivo si hay pagos pendientes.
   
2. **Teléfonos de prepago de Telcel**: Algunos teléfonos de prepago también incluyen este paquete.

3. **Teléfonos bloqueados por falta de pago**: Si tu dispositivo está bloqueado o cerca de ser bloqueado, este script puede desinstalar el paquete de bloqueo.

### Casos en los que no necesitas usar el script:

- Si el teléfono fue **comprado de contado** y no tiene pagos pendientes con Telcel, no es necesario desinstalar este paquete, ya que no te afectará.

## Advertencias importantes

1. **No evitarás el bloqueo de IMEI**: Este método **no evita** que Telcel pueda colocar tu IMEI en la lista negra.
2. **Si el teléfono ya está bloqueado**: Si el teléfono ya está bloqueado, sigue estos pasos:
   1. Reinicia el teléfono de fábrica.
   2. Configura el teléfono **sin conexión a Internet**.
   3. Activa el **modo desarrollador** y la **depuración USB**.
   4. Conecta el teléfono al sistema y ejecuta este script para eliminar el paquete de bloqueo.
   5. Una vez eliminada la app, puedes volver a conectar el teléfono a Internet.
   
   **Importante**: Si conectas el teléfono a Internet sin eliminar el paquete, el dispositivo volverá a bloquearse.

## Uso del script

### Pasos:

1. **Clona este repositorio**:

   ```bash
   git clone https://github.com/tuusuario/ADBUnlocker.git
   cd ADBUnlocker
   pip install -r requirements.txt
   python main.py

### Sigue las instrucciones en pantalla:

El script te guiará para verificar si el paquete de bloqueo co.sitic.pp está instalado en el dispositivo.
Si está instalado, te preguntará si deseas desinstalarlo.
Si el paquete es encontrado y decides desinstalarlo, el script intentará eliminarlo automáticamente.

*Notas adicionales*
Este script solo funcionará en teléfonos de Telcel.
Asegúrate de que tu dispositivo esté conectado correctamente y en modo depuración USB antes de ejecutar el script.
*Autor*
# Este proyecto fue creado por Remsystem Corporation ®.
### Video tutorial forma manual.

[Descargar el video](video.mp4)
