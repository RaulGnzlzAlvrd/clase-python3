# Complemento (clase 09)

## Temas

1. Análisis de los ejercicios

  1. Búsquedas y revisión: `has_no_e`

  2. Alternativa con `in`

  3. Revisión: `avoids`

  4. Revisión: `uses_only`

  5. Revisión: `uses_all`

  6. Reducción a problemas ya solucionados
    1. `uses_all`
    2. `is_palindrome`
  7. Uso de índices y revisión: `is_abecedarian`

---

2. Implementar: `zfill`

---

3. Testing

  1. Uso de `assert`

  2. Distintos casos y casos especiales

  3. Conjunto de test cases
> Program testing can be used to show the presence of bugs, but never to show
their absence!
>
> -Edsger W. Dijkstra

---

4. Uso de `range(n, m)`.

```python
for i in range(0, 1000):
  print(i)
```

---

## Tarea

Estos ejercicios están basadas en un enigma que fue retransmitido en el programa de radio [Car Talk](http://www.cartalk.com/content/puzzlers).


> Give me a word with three consecutive double letters. I’ll give you a couple of words
that almost qualify, but don’t. For example, the word committee, c-o-m-m-i-t-t-e-e. It
would be great except for the ‘i’ that sneaks in there. Or Mississippi: M-i-s-s-i-s-s-i-
p-p-i. If you could take out those i’s it would work. But there is a word that has three
consecutive pairs of letters and to the best of my knowledge this may be the only word.
Of course there are probably 500 more but I can only think of one. What is the word?

1. Escribe un programa para encontrar la palabra.

> “I was driving on the highway the other day and I happened to notice my odometer.
Like most odometers, it shows six digits, in whole miles only. So, if my car had 300,000
miles, for example, I’d see 3-0-0-0-0-0.
>
> “Now, what I saw that day was very interesting. I noticed that the last 4 digits were
palindromic; that is, they read the same forward as backward. For example, 5-4-4-5 is a
palindrome, so my odometer could have read 3-1-5-4-4-5.
>
> "One mile later, the last 5 numbers were palindromic. For example, it could have read
3-6-5-4-5-6. One mile after that, the middle 4 out of 6 numbers were palindromic. And
you ready for this? One mile later, all 6 were palindromic!
>
> “The question is, what was on the odometer when I first looked?”

2. Escribe un programa que compruebe todos los números con 6 dígitos e imprima cualquier número que satisfaga los requerimientos
