sistema de pasteleria trabajo de Harek Fredes y Daniel Soza

1. Descripción del sistema
es un sistema de administracion de una pasteleria que permite registrar una gran varedad de productos (pasteles, cuscakes y galletas) y poder ver el catalogo, tambien puedrecrear boletas y calcular los precios de forma automatica cuandopidan algo con sus respectivos pedidos, esta dirigido a las pastelerias con sus dueños y trabajadores y contienen funcionalidades como registrar nuevo producto,crerar orden, pagar orden, etc.

2. Conceptos de POO aplicados

Abstracción: creamos la clase abstracta producto para que sirva de molde, no se pueden crear productos "genéricos", obligatoriamente deben ser un tipo específico. Define los métodos obligatorios descripcion y calcular_precio

Herencia: las clases pastel, cupcake y galleta heredan de producto. esto nos ayuda a reutilizar código como el nombre, precio base e ingredientes sin tener que volver a escribirlos

Encapsulamiento: ocultamos los atributos usando un guion bajo al principio (por ejemplo, self._nombre), de modo que no se puedan modificar por error desde fuera de la clase. Usamos @property para leerlos de forma segura

Polimorfismo: El método calcular_precio se llama igual en las tres subclases, pero funciona diferente en cada una: el pastel cobra más según el tamaño, el cupcake hace un descuento por cantidad y la galleta cobra un extra si es sin gluten.



3. Criterios de aceptación
1. El sistema debe permitir registrar pasteles, cupcakes y galletas en el inventario.
2. Si un producto está marcado como no disponible, el sistema no debe dejar agregarlo a la orden del cliente.
3. No se puede proceder al pago de una orden si el cliente no ha agregado ningún producto (lista vacía).
4. El total de la orden debe cambiar automáticamente cada vez que se sume un nuevo producto.
5. El sistema debe validar que los precios ingresados sean números y no texto.
6. Al elegir la opción de salir (opcion 4) el programa debe terminar de forma limpia y controlada sin errores.


4. Pruebas de Usuario
accion realizada | resultado esperado | resultado obtenido | cumple? |
intentar pagar una orden que no tiene productos | debe mostrar el mensaje de error: "no puedes pagar una orden vacia" | mostro el error en pantalla y no dejo pagar | SI |
agregar un pastel "Venti" con precio base de 1000 | el precio final debe ser 1600 | el precio calculado fue 1600 | SI |
buscar un producto que no existe en el catálogo | Debe salir el mensaje: "El producto no existe en el catalogo" | Se mostro el mensaje de error correctamente | SI |
presionar la opcion 4 en el menu | el programa debe despedirse y cerrarse | SI |





