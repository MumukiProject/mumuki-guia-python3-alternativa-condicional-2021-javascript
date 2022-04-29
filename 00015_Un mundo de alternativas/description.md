Ahora que ya vimos varios `if`s, volvamos a la función con la que iniciamos la lección: 

```javascript
ム saludarA("Ivi", 17)
"Buenos días Ivi"
```

¿No es un poco tarde para decir _buen día_? :dizzy_face: ¿No sería mejor que `saludar_a` hiciera lo siguiente?

 1. Si son menos de las 12, que diga _Buenos días_;
 2. **en caso contrario** y si son menos de las 19, que diga _Buenas tardes_;
 3. **en caso contrario**, finalmente, que diga _Buenas noches_.
 
Sí, ¡eso es exactamente lo que queremos! Demos la bienvenida a un amigo inseparable del `if` y el `else`: el `else if`.

```javascript
function saludarA(quien, horario) {
  if (horario < 12){
    return "Buenos días " + quien;
  } else if (horario < 19) {
    return "Buenas tardes " + quien;
  } else {
    return "Buenas noches " + quien;
  }
}
```

Como vemos, el `else if` nos permite tomar una decisión cuando la condición anterior no se cumplió, y tal como su nombre lo sugiere, funciona como la combinación de un `if` justo después de un `else`. 

> :warning: ¿Esto significa que las condiciones se evalúan **en orden**? Esta definición alternativa...
> 
> ```javascript
function saludarARecargado(quien, horario) {
  if (horario < 19){
    return "Buenas tardes " + quien;
  } else if (horario < 12) {
    return "Buenos días " + quien;
  } else {
    return "Buenas noches " + quien;
  }
}
> ```
>
> ...¿hará lo mismo que la anterior? Te dejamos en la consola a `saludarA` y `saludarARecargado` para que las pruebes y compares.
> 
> Cuando termines, escribí `listo()`
