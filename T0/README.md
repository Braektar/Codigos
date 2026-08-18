# 1. CDG Correos

Practica personal de codificación de programa DGCcorreos.

Tiempo esperado de realización: 2 semanas --> 05-07-2026

## 1.1. Pasos requeridos:

- [x] Creación de Menús
  - [x] Menú principal
  - [x] Creación Menú Usuario
  - [x] Creación Menú Administrador
- [ ] Funcionalidades
  - [x] Inicio de sesión
  - [ ] Creación de usuario
  - [ ] Inicio sesión administrador
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

### Inicio de sesión