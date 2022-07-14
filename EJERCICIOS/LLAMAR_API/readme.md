## ¿Qué es una API?
Las API son mecanismos que permiten a dos componentes de software comunicarse entre sí mediante un conjunto de definiciones y protocolos. Por ejemplo, el sistema de software del instituto de meteorología contiene datos meteorológicos diarios. La aplicación meteorológica de su teléfono “habla” con este sistema a través de las API y le muestra las actualizaciones meteorológicas diarias en su teléfono.

## ¿Qué significa API?
API significa “interfaz de programación de aplicaciones”. En el contexto de las API, la palabra aplicación se refiere a cualquier software con una función distinta. La interfaz puede considerarse como un contrato de servicio entre dos aplicaciones. Este contrato define cómo se comunican entre sí mediante solicitudes y respuestas. La documentación de su API contiene información sobre cómo los desarrolladores deben estructurar esas solicitudes y respuestas.

## ¿Cómo funcionan las API?
La arquitectura de las API suele explicarse en términos de cliente y servidor. La aplicación que envía la solicitud se llama cliente, y la que envía la respuesta se llama servidor. En el ejemplo del tiempo, la base de datos meteorológicos del instituto es el servidor y la aplicación móvil es el cliente. 

## API de REST
Estas son las API más populares y flexibles que se encuentran en la web actualmente. El cliente envía las solicitudes al servidor como datos. El servidor utiliza esta entrada del cliente para iniciar funciones internas y devuelve los datos de salida al cliente.

## ¿Qué son las API de REST?
REST significa transferencia de estado representacional. REST define un conjunto de funciones como GET, PUT, DELETE, etc. que los clientes pueden utilizar para acceder a los datos del servidor. Los clientes y los servidores intercambian datos mediante HTTP.


Puede llamar a funciones llamadas por otros programas alojados en servidores web. Los servicios cognitivos de Microsoft Azure contienen varias API a las que puede llamar desde su código para agregar inteligencia a sus aplicaciones y sitios web.

En el ejemplo de código, llamará a la función Analizar imagen de Computer Vision

Requisitos para llamar a una API:

* Clave API para darle permiso para llamar a la API
* Dirección o Endpoint del servicio
* nombre de la función del método para llamar como se indica en la documentación de la API
* parámetros de función como se enumeran en la documentación de la API
* Encabezados HTTP como se enumeran en la documentación de la API
