En realidad no siempre saludamos con _buenos días_: por ejemplo, pasadas ciertas horas decimos _buenas noches_. :night_with_stars: 

Por eso, ahora nos gustaría modificar nuestra función `saludar_a` para que tome un parámetro adicional, `horario`, y retorne un saludo diferente según éste: 

```python
ム saludar_a("Dani", 10)
"Buenos días Dani"
ム saludar_a("Feli", 22)
"Buenas noches Feli"
```

¿Pero cómo podríamos lograr esto? Ninguna introducción al lenguaje Python estaría completa sin mostrar _la estructura de control_ más famosa de la programación: ¡la alternativa condicional!

```python
def saludar_a(quien, horario):
  if horario < 19:
    return "Buenos días " + quien
  else:
    return "Buenas noches " + quien
```

> :hourglass_flowing_sand: Tomate uno minutos para leer este `if` e intentar entender qué está pasando acá. Y después probá en la consola lo siguiente: 
>
>  1. saludá a `"Juli"` a las `18`
>  2. saludá a `"Pun Pun"` a las `19`
>
> ¿Sucede lo que esperabas? :thinking:
