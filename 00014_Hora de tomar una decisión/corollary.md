En programación decimos que el `if` es _una estructura de control_ porque permite controlar el flujo de ejecución: ejecuta una cosa u otra dependiendo de una condición. En particular, el ejemplo anterior lo podemos leer como: 

* _si (`if`) el horario es **menor** a 19, entonces devolver buenos dias concatenado con el nombre_;
* _si no (`else`), devolver buenas noches concatenado con el nombre_;


Por eso es que:

* cuando saludamos a Juli a las 18 se ejecuta `return "Buenos días " + quien`;
* pero cuando saludamos a Pun Pun a las 19 horas (ojo :eye:, 19 **no es menor a** 19) se ejecuta `"Buenas noches " + quien`. 
 

