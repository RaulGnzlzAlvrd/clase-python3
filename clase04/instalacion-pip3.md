# Instalación de pip3

Primero se debe verificar si está instalado `pip3` en el sistema:

```
pip3 --version
```

Al ejecutar el comando anterior nos debe aparecer algo como lo siguiente:

```
pip 20.0.2 from /usr/lib/python3/dist-packages/pip (python 3.8)
```

Si no aparece lo anterior se tiene que instalar con el comando `apt`:

```
sudo apt install python3-pip
```

Ahora para instalar paquetes de forma global en el sistema se usa el comando:

```
sudo pip3 install nombre-del-paquete
```
