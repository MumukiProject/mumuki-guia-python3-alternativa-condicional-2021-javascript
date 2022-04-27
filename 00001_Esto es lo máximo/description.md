_Bueno, quizás no sea para taaaanto, pero sí, el `if` es muy útil_  :stuck_out_tongue_closed_eyes:

Veamos otro ejemplo...

```python
# Equivalente a abs
def valor_absoluto(numero):
  if numero >= 0:
    return numero
  else:
    return -numero
```

...y pongamos nombre a cada parte de la alternativa condicional:  

 1. en primer lugar, tenemos la _condición_, que es lo que decide qué acción vamos a ejecutar. Podría ser cualquier _expresión booleana_, o en criollo cualquier cosa que represente una "pregunta" que se pueda responder con sí (`True`) o no (`False`);
 2. luego está _la acción_ del `if`, que retornará lo que queremos en caso de que la condición anterior sea **verdadera**;
 3. por último contamos con  _la acción_ del `else`, que retornará lo que queremos en caso de que la condición anterior sea **falsa**. 

Además, a cada una de estas acciones también se las conoce como _ramas_ :deciduous_tree:, porque ramifican el flujo de ejecución, introduciendo en nuestro programa caminios alternativos. Ah, y algo no menor: las tabulaciones `↹` en cada rama son necesarias para que todo ande. :sweat_smile:

> ¡Escribamos nuestro primer `if`! Definí una función `maximo`, que funcione como `max` (¡no vale usarla!) y devuelva el máximo entre dos números:
> 
> ```python
> ム maximo(4, 5)
> 5
> ム maximo(10, 4) 
> 10
> ```