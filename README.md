# Heladería San José - CRUD en Python

Este es un proyecto de aplicación de escritorio desarrollado en **Python** utilizando **Tkinter** para la interfaz gráfica y **MySQL** como sistema de base de datos. La aplicación permite gestionar datos de un catálogo para una heladería, realizando operaciones CRUD (Crear, Leer, Actualizar, Eliminar).

## Requisitos

Asegúrate de tener instalado lo siguiente:

- Python 3.8 o superior
- MySQL Server
- MySQL Connector para Python
- Tkinter 

## Instalación

1. Clona este repositorio:

```bash
git clone https://github.com/NEsSa-08/HeladeriaSanJose.git
cd HeladeriaSanJose
```
2. Crea un entorno virtual
```bash 
python -m venv venv
venv\Scripts\activate
```
3. Instala las librerías necesarias
```bash
pip install -r requirements.txt
```
4. Crea la base de datos en MySQL
```bash
source bd.sql;
```

5. Configura la conexión a la base de datos
En el archivo Catalogo-Crud.py, ubica esta parte:

mydb = mysql.connector.connect(
    host="localhost",
    user="TU_USUARIO",
    password="TU_CONTRASEÑA",
    database="nombre_de_tu_base"
)

Reemplaza "TU_USUARIO", "TU_CONTRASEÑA" y "nombre_de_tu_base" por los datos reales de tu servidor MySQL.

ejecutar el proyecto
```bash
python Catalogo-Crud.py
