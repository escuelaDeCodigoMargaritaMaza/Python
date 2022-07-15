Si tenemos una función que hemos creado y quisieramos compartirla con el resto del mundo, podriamos almacenarla en un servidor web, y todo aquel que tuviera la dirección web donde esta almacenada podria acceder a la función y usarla en sus propios programas, algo así es una API.

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


Para esta práctica utilizaremos una API de Microsoft llamada Computer Vision, la cual esta de forma gratuita en el portal de AZURE, realizando algo de IE, ciencia de datos y analiza la imagen y nos dice su contenido.

Para acceder a ella necesitamos saber su dirección web, para ir a usar la o las funciones que hacen esto, si entramos al servicio veremos que es un servicio bien documentado, podremos ver las direcciones donde podemos acceder a el y las distinta funciones que me ofrece.

![image](https://user-images.githubusercontent.com/91554777/179100764-112fd6df-04b7-4695-a83f-271366ea5a9f.png)

https://westus.dev.cognitive.microsoft.com/docs/services/computer-vision-v3-2/operations/56f91f2e778daf14a499f21b

Regularmente vamos a querer tener control sobre el ingreso a los servicios que se ofeezcan, en este caso a API restringe el acceso para que se igrese a él via una KEY o clave, para identificar el acceso al servicio, regularmente esas claves son personales para identificar quien accede al servicio, basicamente esa clave es el permiso para usar la función.

Para que las dos aplicaciones puedan "hablar" utilizan un miso idioma o protocolo, en este caso el HTTP, en el qe podriamos decir usan 4 verbos básicos para comunicarse, el POST, el GET, el UPDATE y el DELETE, si vemos en la documentación de la API nos dice el tipo de verbo a usar en cada función, en este caso vemos que solo maneja solicitudes POST y GET, la diferencia entre uno y otro es basicamente la forma en que pasan los datos.

![image](https://user-images.githubusercontent.com/91554777/179108586-c6387f70-f187-47eb-bc31-a5b8ea63be17.png)

Conocimos que son las bibliotecas en Python, y una de las bibliotecas básicas cuando hacemos solicitudes HTTP es la de request, lo que hará es facilitarnos la comunicación POST o GET.

![image](https://user-images.githubusercontent.com/91554777/179117600-9cc49b5e-6016-4671-ac1c-69cfcfcaa41b.png)

![image](https://user-images.githubusercontent.com/91554777/179117503-cd1cb031-cab5-42c2-bf34-f5ad28ecc966.png)

![image](https://user-images.githubusercontent.com/91554777/179117712-ec1ffc70-00c0-4b9f-bd6f-a51fa01c2656.png)

![image](https://user-images.githubusercontent.com/91554777/179117775-6d7fa5bc-ab38-4365-9161-fc4d5e4712f1.png)


Puede llamar a funciones llamadas por otros programas alojados en servidores web. Los servicios cognitivos de Microsoft Azure contienen varias API a las que puede llamar desde su código para agregar inteligencia a sus aplicaciones y sitios web.

En el ejemplo de código, llamará a la función Analizar imagen de Computer Vision

Requisitos para llamar a una API:

* Clave API para darle permiso para llamar a la API
* Dirección o Endpoint del servicio
* nombre de la función del método para llamar como se indica en la documentación de la API
* parámetros de función como se enumeran en la documentación de la API
* Encabezados HTTP como se enumeran en la documentación de la API


Iniciamos ingresando a https://portal.azure.com/ si ya tenemos cuenta de microsoft la podemos usar, de lo contrario podriamos registrarnos con nuesta cuenta de github

![image](https://user-images.githubusercontent.com/91554777/179118284-49273e4f-6590-4688-ba7d-7233a97f6a2a.png)

una vez logueados estamos en el portal de azure.

Nos pedirá completar el registro y nos dará alguna promo de servicio inicial

![image](https://user-images.githubusercontent.com/91554777/179118603-29ef80ec-86fe-44e3-af22-fad25696f449.png)


escribimos en el buscador computer vision y escogemos la opción del mrkeplace para iniciar con la creación del recurso

![image](https://user-images.githubusercontent.com/91554777/179118797-aeaa70f6-b8bc-408f-89fb-240d93a4a8f4.png)



![image](https://user-images.githubusercontent.com/91554777/179118952-2be94ac7-b62b-4a1a-80a1-6e8e72f5233c.png)

Despues de llenar los datos del nombre del recurso y crear un grupo de recursos, que es como una carpeta donde se guardarán los proyectos, adem{as del tipo de servicio, gratuito o de pago.

Dspués de aceptar se habrá creado el recurso

![image](https://user-images.githubusercontent.com/91554777/179119227-84909b70-2c70-42ad-8092-37d737c3245c.png)

Al ir al recurso

![image](https://user-images.githubusercontent.com/91554777/179119272-98db58c7-257d-422f-a66e-8a7e511542a2.png)




vemos la dirección a la que se conectará buscando la función y la KEY necesaria para validar el ingreso

![image](https://user-images.githubusercontent.com/91554777/179120098-b3e2b1ac-c629-47e0-9cef-11972c623254.png)

De esta manera tenemos listo un servicio web para llamar y usar, ahora habría que ir a Python para escribir el código que permita usar la aplicación.
