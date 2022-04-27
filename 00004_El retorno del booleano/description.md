Para cerrar, ahora que ya vimos cómo escribir la alternativa condicional, es momento de un pequeño recordatorio:
si usás adecuadamente las expresiones booleanas, ¡no es necesario utilizar esta estructura de control!

Supongamos que queremos desarrollar una función `es_mayor_de_edad`, que nos diga si alguien tiene
18 años o más. Una tentación es escribir lo siguiente:

```python
def es_mayor_de_edad(edad):
  if edad >= 18:
    return True
  else:
    return False
```

Sin embargo, **este `if` es totalmente innecesario**, dado que la expresión `edad >= 18` ya es booleana:

```python
def es_mayor_de_edad(edad):
  return edad >= 18
```

Mucho más simple, ¿no? :wink:

> Para Ema un número es de la suerte si:
>
> * es positivo, y
> * es menor a 100, y
> * no es el 15.
>
> Definí la función `es_numero_de_la_suerte` que dado un número diga si cumple la lógica anterior. ¡No vale usar `if`! 
