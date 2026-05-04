#!/usr/bin/env python3
"""health check script for local dockerized services
Tries each service first on localhost:PORT and, if that fails, on service-name:PORT
This is useful both when running on the host and when running inside a container
connected to the same Docker network.

Exit code: 0 = all up, 1 = some down
"""
import sys
import urllib.request
import urllib.error
import socket

# List of services as (service_name, port)
SERVICES = [
    ("generador", 3000),
    ("usuario", 5173),
    ("plantillas", 8080),
    ("infraestructura", 80),
]

TIMEOUT = 3.0


def check(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "health-check"})
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            return True, resp.getcode()
    except urllib.error.HTTPError as e:
        return True, e.code
    except (urllib.error.URLError, socket.timeout, ConnectionRefusedError) as e:
        return False, str(e)
    except Exception as e:
        return False, str(e)


def main():
    print("Health check - servicios locales\n")
    all_ok = True
    for name, port in SERVICES:
        # Try localhost first
        local_url = f"http://localhost:{port}/"
        ok_local, info_local = check(local_url)
        if ok_local:
            print(f"{name} (localhost:{port}): UP (HTTP {info_local})")
            continue

        # Then try service name (works from inside Docker network)
        service_url = f"http://{name}:{port}/"
        ok_service, info_service = check(service_url)
        if ok_service:
            print(f"{name} ({name}:{port}): UP (HTTP {info_service})")
            continue

        # Both attempts failed
        print(f"{name}: DOWN (localhost error: {info_local}; service error: {info_service})")
        all_ok = False

    print("\nResumen:")
    if all_ok:
        print("Todos los servicios responden correctamente.")
        return 0
    else:
        print("Al menos un servicio no respondió. Revisa los contenedores y logs.")
        return 1


if __name__ == '__main__':
    sys.exit(main())
