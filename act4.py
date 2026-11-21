class Libro:
    def _init_(self, titulo, autor, genero, editorial, traduccion, precio):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.editorial = editorial
        self.traduccion = traduccion
        self.precio = precio

    def description(self):
        return f"El libro {self.titulo} es un libro de {self.genero} escrito por {self.autor} y publicao por {self.editorial}"

    def escription_final(self):
        return self.precio * 1.21

libro = Libro("El principito", "Novela", "Antoine de Aint-Exupéry", "Gallimard", "Frances", 10.00)

print(libro.description())
print(libro.precio_final())