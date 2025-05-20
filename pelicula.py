class Pelicula:
    def __init__ (self, codigo=0, titulo="", duracion=0, director="", prestada=False):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__duracion = duracion
        self.__director = director
        self.__prestada = prestada

    # GETTER
    def get_codigo(self):
        return self.__codigo
    
    def get_titulo(self):
        return self.__titulo
    
    def get_duracion(self):
        return self.__duracion
    
    def get_director(self):
        return self.__director
    
    def get_prestada(self):
        return self.__prestada
    
    # SETTER
    def set_codigo(self, codigo):
        self.__codigo = codigo

    def set_titulo(self, titulo):
        self.__titulo = titulo

    def set_duracion(self, duracion):
        self.__duracion = duracion

    def set_director(self, director):
        self.__director = director

    def set_prestada(self, prestada):
        self.__prestada = prestada
    
    # METODOS
    # PRESTAR
    def prestar(self):
        if not self.__prestada:
            self.__prestada = True
            return "La pelicula no ha sido prestada"
        else:
            return "La pelicula ya esta prestada"
        
    # DEVOLVER
    def devolver(self):
        if not self.__prestada:
            self.__prestada = False
            return "La pelicula no ha sido devuelta"
        else:
            return "La pelicula ha sido devuelta"
        
    # COSTO REPRODUCCION
    def costo_reproduccion(self, tarifa_por_minuto):
        coste_total = self.__duracion * tarifa_por_minuto
        return f"El costo de reproducción es de: ${coste_total:.2f}"
    
    # Se mira si la pelicula fue prestada o no
    def __str__(self):
        estado = "esta prestada" if self.__prestada else "no esta prestada"
        return f"La pelicula #{self.__codigo} titulada {self.__titulo} dirigida por {self.__director} dura {self.__duracion} minutos y {estado}"
    
    # Se compara si dos peliculas tienen el mismo codigo
    def __eq__(self, otro_pelicula):
        if isinstance(otro_pelicula, Pelicula):
            return self.__codigo == otro_pelicula.get_codigo()
        return False