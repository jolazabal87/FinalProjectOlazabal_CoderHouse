
###**Business Project**


El proceso creativo de la APP involucra la intención de poder lograr (en base a los conocimientos adquridos durante el curso)
un playground de un comercio y la posibilidad de escalarlo a un E-commerce (o al menos un cart)
utilizando el lenguaje Python, el framework Django y respetando el patrón de diseño MVT

##*Entrega intermedia*
#Objetivo = cumplir con lo requerido en la consigna (herencias, modelos, creación, busqueda)
Para cumplir con la misma realizamos las siguientes acciones:
- iniciamos el proyecto con Django (startproject)
- iniciamos la aplicación (startapp)
- definimos las clases y modelos
    - la hice de manera plana (sin interconexion entre las tablas cosas que seria necesaria)
- configuramos el archivo settings (INSTALLED APP y el nombre de dB)
- configuramos la dB (makemigrations + migrate)
- configuramos el archivo admin (creamos superuser + password)
- comenzamos a diseñar las vistas y a conectar las urls (aplicación - aplicativo y vistas)
- utilizamos templates y statics (con la libreria BOOTSTRAP)
- la herencia la hacemos desde base_padre.html y los childs la usaran
- despues diseñamos los formularios para la creación y busqueda (CR)
    -para cumplir con la consigan lo hicimos parcialmente

#Pendientes
- escalar lo expuesto arriba a todas las funcionalidades de la app
- darle el diseño definitivo y propio de la app
- incluir imagenes y textos
- crear una navegación sólida a partir de las rutas

#Próximos pasos 
- Implementar finalmente el CRUD con la inclusión del Update y del delete

#Consultas a los profesores y tutores
- como subir una Imagen desde el form y como almacenarla ??
- se puede subir más de 1 ??
- en el caso del checkbox... como se puede hacer para captar el false ??
- en el caso de querer hacer un ecommerce se necesitan sessions y cookies ??
- en el caso de querer conectar los modelos a traves de foreingKey... se puede ??
- se pueden armar middlewares para filtrar las informaciones segun el permiso del usuario ??
- como se pueden administrar los permisos ??
- se puede mandar a una url mas de una vista ??

``Fecha = 27-06-2022``