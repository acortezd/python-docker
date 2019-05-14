# Manual de instalación Alpine Linux

### ***primer paso:***
entrar como usuario ```root```
### ***segundo paso:***

ejecutar el comando ```setup-alpine```
 
### El script de instalación pasa por los diferentes pasos de configuración:

- teclado: ```es```
- variacion de teclado: ```es-cat```
- nombre del equipo: ```alpine```
- inicializar interfaz: ```eth0```
- configuración de IP: ```dhcp```
- ***¿quieres realizar alguna configuración de red manual?:*** ```no```
- ***establecer el password del root:***
- zona horaria: ```CET```
- Proxy: ```none```
- Elección del mirror: ```f``` *(se selecciona el más rápido)*
- instalación de servidor de SSH: ```openssh``` *(opción por defecto)*
- cliente NTP: ```chrony``` *(opción por defecto)*
- selección de disco: ```sda```
- uso del disco: ```sys``` *(selecciona ? para ver las diferencias entre las opciones presentadas)*
- confirmar el borrado del disco: ```y```



# Instalación Docker

- *ejecutamos el comando* ```apk add docker```

si el comando falla con ***unsatisfiable constraints***  debemos editar en la ruta ***/etc/apk/repositories***

- agregamos la siguiente línea descomentada:

 http://dl-cdn.alpinelinux.org/alpine/latest-stable/community 

- *ejecutamos el comando* ```service docker start```