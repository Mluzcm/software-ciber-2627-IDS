from util.pattern_loader import pattern


@pattern("P003")
class Pattern3:
    def __init__(self, parametros_regla, log_file, whitelist):
        self.parametros = parametros_regla
        self.log_file = log_file
        self.whitelist = whitelist

    def run(self):
        print(f"--- Ejecutando {self.parametros['nombre']} (ID: P003) ---")
        print(f"    Riesgo: {self.parametros['severidad']}")
        print(
            f"    Condición: {self.parametros['umbral']} eventos "
            f"en {self.parametros['ventana']} segundos."
        )
        print(f"    Log configurado: {self.log_file}")
        print(f"    IPs ignoradas: {self.whitelist}")
