from pelicula import Pelicula

if __name__ == "__main__":

    pelicula1 = Pelicula(7562, "Saw", 103, "James Wan", True)
    pelicula2 = Pelicula(6723, "Annabelle", 99, "John R. Leonetti", False)
    pelicula3 = Pelicula(7562, "Child's Play", 87, "Tom Holland", False)
    
    print(pelicula1)
    print(pelicula2)
    print(pelicula3)

    print(pelicula1.prestar())
    print(pelicula2.prestar())
    print(pelicula3.devolver())

    print(pelicula1.costo_reproduccion(125))
    print(pelicula2.costo_reproduccion(125))
    print(pelicula3.costo_reproduccion(125))
    
    print("¿pelicula1 y pelicula2 tienen el mismo código?", pelicula1 == pelicula2)
    print("¿pelicula1 y pelicula3 tienen el mismo código?", pelicula1 == pelicula3)