
#**Business Project**

El objetivo de nuestra APP es generar un espacio para que la comunidad de gente amante del cine clásico
pueda compartir sus films, videos, records que tenga a disposición y que pueda ofrecerla dentro de la comunidad (compra/venta) además de compartir sus opiniones a traves del blog y/o hacer consultas a traves de una sección específica.
Es una suerte de "NETFLIX VINTAGE" con entrega de la pelicula (NO streaming)
Y en la comunidad todos se conocen y se pueden ver en la sección Usuarios.
Es en cierta manera un dashboard con estas funcionalidades.

Esta comunidad esta abierta para todo público que desee visitar la APP.
Las funcionalidades requieren de que el usuario este registrado.
A su vez (si el usuario tiene el permiso admin) puede acceder a las funcionalidades de Crear, Editar y Eliminar nuevos géneros y nuevos titulos.
Cualquiera (admin, user o simplemente guest) que navegue por la pagina puede usar la funcionalidad de la busqueda para buscar su pelicula favorita o aquella de la que desee tener info.
Quizá la funcionalidad más importante (y la esencia del sitio) es la sección Ticket, dónde un usuario registrado y logueado puede hacer compra de uno o varios titulos disponibles en el sitio.

``Tecnologia de la APP``

Nuestra aplicación ha sido creada con base Python y utilizando el frameWork Django.
Respetando una arquitectura de diseño MVT que nos posibilitó lograr una performance aceptable para ser un primer proyecto.
Y lo más importante es lo suficientemente flexible y adpatable para ser escalable y mejorar/agregar funcionalidades.
La performance fue testeada en las diferentes etapas del desarrollo con diferentes pruebas "Debug".


    - iniciamos el proyecto con Django (startproject)
    - iniciamos la aplicación (startapp) y generamos una aplicación adicional para la sección TICKET
    - definimos las clases y modelos
    - configuramos el archivo settings (INSTALLED APP y el nombre de dB)
    - configuramos la dB (makemigrations + migrate)
    - configuramos el archivo admin (creamos superuser + password)
    - comenzamos a diseñar las vistas y a conectar las urls (aplicación - aplicativo y vistas)
    - utilizamos templates y statics (con la libreria BOOTSTRAP)
    - la herencia la hacemos desde base_padre.html y los childs la usaran
    - diseñamos los formularios para la creación y busqueda (CR)

Adicional desarrollamos nuestra API para poder compartir nuestra información con diferentes lenguajes de programación. (Django rest_framwork)
El TO DO que nos queda pendiente es poder integrarlo a una aplicación front end desarrollada en REACT.

``About Me``
Mi nombre es Ignacio Olazábal.
Soy profesional de Ciencia Económicas, más precisamente Contador Público. Hace ya muchos años que formo parte del mundo corporativo, orientado a Pymes en el sector de consumo masivo, donde he liderado varios negocios y he formado parte de proyectos de desarrollo de marcas (Aleluya, JuanValdez) tanto en el mercado local como en el internacional.
Estoy en busca de nuevas experiencias y creo firmemente que el futuro llegó en el mundo digital.
Mi deseo es seguir mi carrera en esta industria, para lo cual me estoy preparando y este curso he decidido realizarlo en esa línea.

``Agradecimientos``
A mi familia que me acompañó en este proceso, a los compañeros que han sido un gran aporte durante toda la cursada, a los tutores que nos dieron su apoyo, a toda la comunidad digital de la que siempre tomamos ideas y funcionalidades y a nuestro profesor GR, que con mucha paciencia y profesionalismo nos compartió su conocimiento y nos ayudo a poder interpretarlo e incorporarlo.

``Fecha = 22-07-2022``
