# Módulo 2 · IDS/NIDS ligero

- **Equipo propietario:** `equipo-02-ids`
- **Puerto:** `8002`

## Qué expone
Publica los eventos de seguridad que detecta hacia el SIEM.
- `POST /events` (hacia el SIEM, formato común de evento)

## Qué consume
Nada obligatorio (opcionalmente puede validar sesión de su panel de administración contra Identidad).

## Estado
El motor del IDS se encuentra en `src/`. La configuración se define en
[`src/ids.conf`](src/ids.conf) con un formato sencillo:

```text
CONFIG, LOG_FILE, ./logs_simulados.txt
CONFIG, WHITELIST, 127.0.0.1, 192.168.1.0/24
P001, ON, 5, 60, ALTA, Fuerza Bruta SSH
```

Al ejecutar `python src/main.py`, solo se cargan las reglas con estado `ON`.
Cada regla recibe sus parámetros, el fichero de logs y la lista de IPs
permitidas. Las reglas se registran automáticamente mediante
`src/util/pattern_loader.py`.

El módulo `src/log_parser.py` transforma cada línea válida de un archivo `.log`
en un objeto JSON. `main.py` lee temporalmente `logs/1.log` según la ruta de
`ids.conf` y le pasa sus líneas al parser. Los eventos quedan en memoria y no
se escriben en otro archivo ni se envían a las reglas todavía. Por ejemplo:

```json
{"timestamp":"Apr 20 13:51:02","service":"sshd","event_type":"failed_login","username":"root","source_ip":"122.5.240.60","source_port":54874}
```
