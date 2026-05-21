# Torre de Hanoi

Una Torre de Hanói es un rompecabezas consistente en una serie de discos perforados que deben trasladarse desde su posición inicial en el primer pilar, ordenados desde el más grande abajo hasta el más pequeño arriba, hasta la misma posición pero en el tercer pilar. Sin embargo, hay una regla importante: **debes trasladar los discos al tercer poste moviendo un disco a la vez y sin colocar un disco grande encima de uno pequeño**. Ahora implementarás tu propia versión de este rompecabezas.

![](../img/hanoi-1.png)

La clase `TorreDeHanoi` está conformada por 3 pilares, donde cada uno es un *stack*, ya que solo puedes añadir y quitar discos por un extremo de cada pilar. La clase viene con los métodos `__init__` y `__str__` implementados, por lo que puedes ver el estado inicial de la torre. Sin embargo, **solo con métodos de *stacks***, deberás implementar el método `mover_disco`, que recibe el número del pilar desde donde sale el disco y el número del pilar al que llega un disco. Cabe destacar que el tamaño de un disco está representado por el número contenido en el pilar (por ejemplo, el 6 representa al disco más grande y el 1 al más pequeño). Una vez que implementes este método, te retamos a hacer una función que ocupe las operaciones de *stacks* necesarias para mover el disco. **Recuerda no colocar un disco grande encima de uno pequeño**.

![](../img/hanoi-2.png)

**PS:** Además, te retamos a: (1) verificar que un movimiento es válido (no queda un disco grande sobre uno pequeño) y (2) crear una función que verifique si el rompecabezas fue completado correctamente . 