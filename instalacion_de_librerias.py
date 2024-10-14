import subprocess

with open("requirements.txt") as f:
    for package in f:
        package = package.strip()
        if package:
            try:
                subprocess.check_call([f"pip", "install", package])
            except subprocess.CalledProcessError:
                print(f"Error al instalar {package}, omitiendo...")


