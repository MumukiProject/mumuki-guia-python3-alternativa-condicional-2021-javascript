Ahora que ya podemos escribir nuestros cartelitos identificatorios grandes y chicos, queremos una función que nos dé el cartelito de tamaño óptimo:

* si nombre y apellido tienen, en total, más de 15 letras, queremos un cartelito corto;
* de lo contrario, queremos un cartelito largo.

> Definí la función `escribir_cartelito_optimo` que tome un título, un nombre y un apellido, e invocando `escribir_cartelito` genere un cartelito corto o largo, según las reglas anteriores. Ejemplo:
>
> ```python
> ム escribir_cartelito_optimo("Ing.", "Carla", "Toledo")
> "Ing. Carla Toledo"
> ム escribir_cartelito_optimo("Dr.", "Estanislao", "Schwarzschild")
> "Dr. Schwarzschild"
> ```
