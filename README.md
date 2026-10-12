
## Tarea HW-04 - Publicación de una página web con CDN

### Descripción

Para esta tarea realicé una página web sencilla utilizando Vite,
HTML, CSS y JavaScript. Después utilicé los servicios de AWS
para poder publicarla en internet.

Primero creé un bucket en Amazon S3 para almacenar los archivos
de la página. Luego configuré CloudFront para que cualquier
persona pueda ingresar por medio de un enlace.

También utilicé GitHub Actions para que, al subir cambios al
repositorio, la página se compile y se actualice automáticamente.

### Herramientas utilizadas

- Visual Studio Code
- Vite
- HTML, CSS y JavaScript
- GitHub Actions
- Amazon S3
- AWS CloudFront

### Enlace de mi página web

https://d1by0rb1as7vvj.cloudfront.net

### Funcionamiento de GitHub Actions

Para automatizar la publicación configuré un archivo deploy.yml
que realiza tres pasos importantes:

1. Build: genera los archivos de la página utilizando Vite.
2. Upload: sube los archivos generados al bucket de S3.
3. Invalidate: limpia la caché de CloudFront para mostrar los cambios.

Después de corregir un problema con los permisos de AWS,
el pipeline se ejecutó correctamente y la página quedó
disponible desde el enlace de CloudFront.

### Evidencias

#### Compilación del proyecto con Vite

<img width="895" height="312" alt="Build de Vite" src="https://github.com/user-attachments/assets/a694a1c1-ae73-4da8-af4f-ff9b940dbd52" />

#### Proyecto funcionando de forma local

<img width="1057" height="860" alt="Pagina local" src="https://github.com/user-attachments/assets/68dd95bd-5a77-4bda-9fdd-629b78d262f6" />

#### Pipeline de GitHub Actions ejecutado correctamente

<img width="1856" height="1022" alt="Pipeline exitoso" src="https://github.com/user-attachments/assets/7a39bc49-8d31-4072-aa5a-b54927795a3a" />

#### Página publicada en CloudFront

<img width="1837" height="782" alt="Pagina publicada" src="https://github.com/user-attachments/assets/0fba13dd-524e-4fa3-b30a-630a42a4b188" />

### Resultado

Al finalizar la tarea logré publicar mi primera página web
utilizando un CDN. También pude comprobar que los cambios
se pueden publicar automáticamente desde GitHub Actions,
sin necesidad de subir los archivos manualmente a S3.
