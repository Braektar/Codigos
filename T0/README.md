# 1. CDG Correos

Practica personal de codificación de programa DGCcorreos.

Tiempo esperado de realización: 2 semanas --> 05-07-2026

## 1.1. Pasos requeridos:

- [x] Creación de Menús
  - [x] Menú principal
  - [x] Creación Menú Usuario
  - [x] Creación Menú Administrador
- [x] Funcionalidades
  - [x] Inicio de sesión
  - [x] Creación de usuario
  - [x] Inicio sesión administrador
- [ ] Menu Usuario
  - [ ] Ingresar encomienda
  - [ ] Revisar estado de encomienda
  - [ ] Realizar reclamo
  - [ ] Ver estado de pedidos personales
  - [ ] Cerrar sesión
- [ ] Menu administrador
  - [ ] Actualizar encomiendas
  - [ ] Revisar reclamos
  - [ ] Cerrar sesión

# 2. Especificos

## 2.1. Menús de usuario

Se creará un modulo que contenga unicamente los menús, sin incluir su funcionalidad esperada (por el momento)

### 2.1.1. Menú principal

![alt text](image.png)
> Ejemplo de menú de inicio

### 2.1.2. Menú Usuario

![alt text](image-1.png)
> Ejemplo de menú de usuario

### 2.1.3. Menú administrador

![alt text](image-2.png)
> Ejemplo de menú de administrador

## Funcionalidades

Generaré una función que se dedique a verificar si el input escogido está dentro de las opciones.

### Menu principal

La gestión de Menus se llevará a cabo a traves de un contador, el cual tendrá el siguiente formato para identificar que menú debe mostrar:

- 0: Menu principal
- 1: menu iniciar sesión
- 11: Menu de usuario | opción 1
- 12: Menu de usuario | Opción 2
- 2: Menu registrar usuario
- etc...

## Modulo funciones.py

### get_input(op)

La función recibe el mayor valor numerico y solicita un valor. Verifica que el valor se encuentre dentro del rango [1, valor]. De encontrarse en el rango, devuelve el número.

### DatosUsuarios

La función recibe un diccionario y una ruta. Los valores predeterminados son un diccionario vacío y la ruta de usuarios.csv, el cual debe encontrarse en una carpeta llamada Codigo.

La función devuelve un diccionario con los datos de usuario y contraseña.

### IniciarSesion

La función recibe un diccionario de usuarios con el formato [usuario] = Contraseña.

La función pide un nombre de usuario y verifica que se encuentre dentro del diccionario. Si no existe, se devuelve al menu principal.

Si el usuario existe, se le solicita la contraseña. La función da 3 intentos para ingresar correctamente.

Si falla, vuelve al menu principal. Si ingresa correctamente la contraseña, avanza al menú de usuario.

### CrearUsuario

La función recibe la ruta del archivo csv y devuelve un diccionario [Usuario] = contraseña.

La función solicita un nombre de usuario y contraseña.

Si el nombre de usuario ya existe, devuelve el diccionario original.

Si el nombre no existe, confirma que el nombre tenga el minimo de caracteres permitido.

Si tiene el minimo de caracteres, solicita contraseña, el cual revisa si tiene el minimo de caracteres permitidos.

Si se cumplen todas las funciones, se actualiza el diccionario y se agrega la información al archivo usuarios.csv

### InicioAdmin

La función no recibe datos.

La función solicita la contraseña de administrador. Si esta es incorrecta, consulta si quiere reintentar o volver al menú.

Si la contraseña es correcta, se avanza al siguiente menú.