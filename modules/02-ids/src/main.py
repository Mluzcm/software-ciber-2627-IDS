from pathlib import Path

from util.pattern_loader import pattern_dict


def cargar_configuracion(ruta_archivo):
    """Carga la configuración sencilla del IDS."""
    config = {
        "log_file": "",
        "whitelist": [],
        "reglas_activas": {},
    }

    ruta = Path(ruta_archivo)
    with ruta.open(encoding="utf-8") as archivo:
        for numero_linea, linea in enumerate(archivo, start=1):
            linea = linea.strip()
            if not linea or linea.startswith("#"):
                continue

            partes = [parte.strip() for parte in linea.split(",")]
            if partes[0] == "CONFIG":
                if len(partes) < 3:
                    raise ValueError(
                        f"Configuración incompleta en {ruta}:{numero_linea}"
                    )
                if partes[1] == "LOG_FILE":
                    config["log_file"] = partes[2]
                elif partes[1] == "WHITELIST":
                    config["whitelist"] = partes[2:]
                continue

            if len(partes) != 6:
                raise ValueError(f"Regla inválida en {ruta}:{numero_linea}")

            id_regla, estado, umbral, ventana, severidad, nombre = partes
            if estado == "ON":
                try:
                    umbral = int(umbral)
                    ventana = int(ventana)
                except ValueError as error:
                    raise ValueError(
                        f"Umbral o ventana inválidos en {ruta}:{numero_linea}"
                    ) from error

                config["reglas_activas"][id_regla] = {
                    "umbral": umbral,
                    "ventana": ventana,
                    "severidad": severidad,
                    "nombre": nombre,
                }

    return config


def main(ruta_configuracion=None):
    ruta_configuracion = ruta_configuracion or Path(__file__).with_name("ids.conf")
    config = cargar_configuracion(ruta_configuracion)

    print(f"[*] Log a procesar: {config['log_file']}")
    print(f"[*] Whitelist: {config['whitelist']}")
    print(f"[*] Reglas activas: {list(config['reglas_activas'])}\n")

    for id_regla, parametros in config["reglas_activas"].items():
        clase_patron = pattern_dict.get(id_regla)
        if clase_patron is None:
            print(f"[!] Aviso: la regla {id_regla} está ON pero no está registrada")
            continue

        instancia = clase_patron(
            parametros,
            config["log_file"],
            config["whitelist"],
        )
        instancia.run()

if __name__ == "__main__":
    main()
