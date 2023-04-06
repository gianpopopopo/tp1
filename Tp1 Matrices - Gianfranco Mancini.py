class MYARRAY:
    
    def __init__(self,r,c,elems):
        self.r = r
        self.c = c
        self.elems = elems
        
    def myprint(self):
        print('\n')
        for k in range(1,self.r+1):
            print(self.get_row(k))
        print('\n')
        return None
        
    def get_pos(self,j,k):
        """
        La funcion le pide que ingrese las coordenadas del elemento en la lista
        de la cual usted quiere saber el indice. 
        Por ejemplo: si usted ingresara k = 1 , j = 1 : esta funcion le devolveria el indice 0
        de la lista en el cual esta la matriz, ya que las coordenadas (1,1) pertenecen al 
        primer elemento de cualquier matriz sin importar el tamaño. 
        """
        
        if j > self.r or k > self.c:
            None
        else:
            m = (j-1) * (self.c) + (k-1)
            return m
        
    
    def get_coords(self,m):
        """
        El objetivo de esta funcion es sacar las coordenadas de un elementos en una matriz, expresada en
        una lista plana, mediante el indice seleccionado. En el caso que m sea un indice mayor a aquellos
        que la lista tiene, el codigo no funcionara.
        "j" representa la fila mientras que "k" la columna. A su vez // da el cociente de la division y % da el resto.
        Por alguna flasheada de la vida resulta que justo conciden los indices y las coordenadas de una matriz en
        formato lista.
        """
        
        if m > len(self.elems)-1:
            None
        else:
            j = m // self.c
            k = m % self.c
            return [j+1,k+1]
    
    def switch(self, by_row):
        """
        Esta funcion cambia la forma de analizar la matriz. En el caso de que la matriz elems= [1,2,3,4]
        sea analizada por "rows" esta devolvera [1,2,3,4], en cambio si by_row = False la matriz sera vista 
        de la siguiente manera: [1,3,2,4].
        La logica detras del codigo recae en que por cada fila (j) quiero que por cada columna (k) en el range 
        del grande de la matriz me appendee a la lista vacia los elementos de self.elems de manera que quede
        analizada "by_row=False".
        Por ejemplo;
        j y k estan en range 0:3 en el caso de tener una matriz 3x3, la primera instancia va a resultar de la
        siguiente manera:
            self.elems[0*3 + 0] --> 1
            self.elems[1*3 + 0] --> 4
            self.elems[2*3 + 0] --> 7
            y asi sucesivamente hasta appendear self.elems[2*3+2] --> 9
            
        (A CHEQUEAR HICE CAGADA ME APRECE D:)
        """

        if by_row == True:
            return self.elems
        else:
            switched_elems = []
            for j in range(self.c):
                for k in range(self.r):
                    index = k * self.c + j
                    if index >= len(self.elems):
                        index -= len(self.elems)
                    elif index > len(self.elems):
                        return self.elems
                    else:
                        switched_elems.append(self.elems[index])
                        
            self.elems = switched_elems
            return self.elems 
            
    def get_row (self,j):
        """
        Esta funcion tiene el objeivo de devolver una row, j, que el usuario idnique.
        Logra esto mediante un slicing de la instancia de la matriz, a j se le resta 1
        para ponerlo en formato "indice", luego es multiplicado por la cantidad de rows en la matriz
        entonces:
            En el caso de tener una matriz 3x3 y que j sea 1:
                self.elems[(1-1)*3:3] o self.elems[0:3]
                devolviendonos --> [1,2,3]        
        """
        if j > self.r:
            None
        else:
            return self.elems[(j-1)*self.r:self.r*j]
         
    def get_col(self,k):
        """
        Esta funcion tiene el objeivo de devolver una columna, k, que el usuario idnique.
        Logra esto mediante un slicing de la instancia de la matriz habiendole aplicado
        la funcion "switch". En realidad lo que esta pasando es que la matriz, al ser switcheada,
        las columnas se vuelven filas, por ende se le puede aplicar la funcion "get_row".
        """
        if k > self.c:
            None
        else:
            self.elems = self.switch(by_row=False)
            return matriz.get_row(k) 
        
    def get_elem(self,m):
        """
        Esta funcion tiene el objeivo de devolver el elemento de la matriz self.elems al ingresar
        el incide de este en la lista. 
        Esto es posible al aplicar la funcion "get_coords" en m, lo cual te da las coordenadas, luego
        aplicar el resultado a la funcion previa "get_pos" lo que devolvera el indice del numero.
        La verdad que no entendi muy bien que me pide el enunciado hice esto pero ahora me doy cuenta que
        es al pedo :D
        """
        j,k = matriz.get_coords(m)
        m = matriz.get_pos(j,k)
        return self.elems[m] 
    
    def del_row(self,j,matrix):
        """
        Esta funcion tiene el objeivo de devolver la matriz self.elems habiendo eliminado una fila
        seleccionada por el usuario.
        Existe la posibilidad de implementar la funcion "get_row" pero no es posible usar el operador "del"
        con funciones.
        """
        if j < 1 or j > self.r:
            None
        else:
            del matrix[(j-1)*self.c:j*self.c]
            self.r -=1
            return matrix #matriz.myprint()
            
        
    def del_col(self,k,matrix):
        """
        Esta funcion tiene el objeivo de devolver la matriz self.elems habiendo eliminado una columna
        seleccionada por el usuario.
        Usa la funcion switch para hacer que las columnas sean filas, luego se usa switch una segunda vez
        al haber eliminado la "fila" para regresar al formato orginial.
        """
        if k < 1 or k > self.r:
            None
        else:
            #print(matrix)
            matrix = self.switch(by_row = False)
            self.del_row(k,matrix)
            self.c = self.r
            return matrix

    def swap_rows(self,j1,j2):
        """
        Esta funcion tiene el objeivo de devolver la matriz con las filas intercambiadas segun el usuario elija.
        La funcion define mediante un slicing las filas utilizando la funcion "get_row" para luego reemplazarlas 
        directamente en la matriz original. 
        """
        if j1 > self.r or j2 > self.r:
            None
        else:
            row1 = matriz.get_row(j2)[0:self.c]
            row2 = matriz.get_row(j1)[0:self.c]
            self.elems[(j1-1)*self.c:self.c*j1] = row1[0:self.c]
            self.elems[(j2-1)*self.c:self.c*j2] = row2[0:self.c]
           
            return self.elems #matriz.myprint() 
            
  
    def swap_cols(self,k1,k2):
        """
        Esta funcion tiene el objeivo de devolver la matriz con las columnas intercambiadas segun el usuario elija.
        Utiliza la matriz self.elems aplicada la funcion "switch" luego se le aplica la funcion "swap_rows", con 
        el fin de usar las columnas como filas, luego se ejecuta "switch" nuevamente para devolver la matriz
        a su fomrato original.
        """
        if k1 > self.c or k2 > self.c:
            None
        else:
            self.elems = self.switch(by_row=False)
            self.elems = self.swap_rows(k1,k2)
            self.elems = self.switch(by_row=False)
            return self.elems #matriz.myprint()

            
    def scale_row(self,j,x, n = 0):
        """
        Esta funcion tiene como objevio multiplicar la fila de una matriz elegida por el susuario. esto se consigue
        definiendo la fila como "row" utilizando la funcion "get_row" y aplicarle "j" (el numero que eligio el usuario).
        luego se usa un metodo recursivo para intercambiar el numero multiplicado por su correspondiente de la matriz.
        Una vez que n se le sume suficientes veces 1 hasta lelgar al largo de "row"(la fila que se eligio multiplicar),
        la funcion termina.
        """
        row = matriz.get_row(j)
        if n == len(row):
            None
        else:
            row[n] = row[n] * x
            self.elems[(j-1)*self.c+n] = row[n]
            return self.scale_row(j, x, n+1) #matriz.myprint()
        
    def scale_col(self,k,y):
        """
        Esta funcion tiene como objevio multiplicar la columna de una matriz elegida por el susuario. Nuevamente
        se utiliza la funcion "switch" luego la funcion "scale_row" para nuevamente usar "switch" con el fin
        de devolverle su formato original.
        """

        if k > self.c:
            None
        else:
            self.elems = matriz.switch(by_row=False)
            matriz.scale_row(k,y)
            self.elems = matriz.switch(by_row=False) 
            return self.elems #matriz.myprint()
        
    def transpose(self,matrix):
        """
        Cumple una funcion similar a la funcion "switch" pero el valor asignado
        a las filas y columnas se intercambia.
        (PROBLEMA CON LOS INDICES EN MATRICES NO CUADRADAS (self.r+1??))
        """
        transposed = []
        for j in range(self.c):
            for k in range(self.r):
                index = ((k * self.r) + j)
                transposed.append(matrix[index])
        self.r, self.c = self.c, self.r
        return transposed #matriz.myprint()
              
    def flip_cols(self):
        """
        Intercamia las columnas de manera especular. Hay que tener el cuenta que para matrices mayores
        a 3x3 se intercambian todas las columnas. Entonces, similar al switch, pido que me pase por cada
        columna quiero que me de por cada columna un appendeo de un elemento en la lista.
        """
        flipped = []
        for i in range (1,self.c+1):
            for k in range (1,self.r+1):
                flipped.append(self.elems[(self.c*i)-k])
        self.elems = flipped
        return self.elems

        
    def flip_rows(self):
        """
        Intercamia las filas de manera especular. Se utiliza la funcion "flip_rows" en formato by_row = False 
        para intercambiar las filas como si fuesen columnas, luego se utiliza la funcion "switch" nuevamente.
        """
        self.switch(by_row = False)
        self.flip_cols()
        self.switch(by_row = False)
        return self.elems
    
    def __add__ (self,k):
        """
        Suma un elemento K por igual a toda la matriz.
        """
        self.elems = [i + k for i in self.elems]
        return self.elems
    
    def __radd__ (self,r):
        """
        Suma de manera inversa, x + y lo suma en cambio: y + x.
        """
        self.elems = [i + r for i in self.elems]
        return self.elems
        
    def __sub__ (self,s):
        """
        REsta un numero S por igual a toda la matriz.
        """
        self.elems = [i - s for i in self.elems]
        return self.elems
        
    def __rsub__ (self,ñ):
        """
        Realiza la resta inversa. x - y lo resta en cambio: y - x.
        """
        self.elems = [i - ñ for i in self.elems]
        return self.elems
        
    def __mul__ (self,m):
        """
        Multiplica un numero por cada elemento de la matriz por igual.
        """
        self.elems = [i * m for i in self.elems]
        
    #def __matmul__ (self):
        
    #def __rmul__ (self):
        
    #def cof(self):
    
    def sub_matriz(self,i,matrix):
        """
        (SIN TERMINAR + FUCIONA MAL POR EL del_col)
        """
        sub = MYARRAY(self.r,self.c,self.del_row(1,matrix))
        print(sub.elems)
        sub = MYARRAY(self.r,self.c,self.del_row(i,sub.del_col(sub.elems)))
        print(sub.elems)
        return sub.elems
            

    def det(self,matrix):
        """
        (SIN TERMINAR, PROBLEMAS CON QUE SE MODIFICA LA MATRIZ ORIGINAL)
        Esta funcion tiene como objetivo sacar el determinante atraves de achicar
        matrises cuadradas de mayor tamaño a 2x2. Una vez calculada la sub matriz se saca 
        el determinante de la misma y se appendea a una lista, sumandolas todas dando como 
        resultado el determinante.
        """
        if self.c == 1:
            matrix[0]
            
        elif self.c and self.r == 2:
            determinant =  matrix[0]*matrix[-1] - matrix[1]*matrix[-2]

        else:
            sub_matrix_list = []
            sign = 1
            for i in range(1,self.c+1):
                if i % 2 == 0:
                    sign = sign*(-1)
                else:
                    sign = sign
                sub_mat = MYARRAY(self.r,self.c,self.sub_matriz(i,matrix))
                #print(sub_mat.elems,sub_mat.r,sub_mat.c)
                sub_det = self.det(sub_mat.elems)
                sub_matrix_list.append(sign * sub_det)
            determinant = sum(sub_matrix_list)
        return determinant
        
    #def seb(self,B):
        
    #def rprod(self,B):
    
    #def lprod(self,B):
        
    #def pow(self,B):
        
"""
Abajo se encuentran las especificaciones de la clase.
Caso base:
    c = 3
    r = 3
Matriz:
    
    [1,2,3]
    [4,5,6]
    [7,8,9]
    
by_row = None
    
"""

matriz = MYARRAY(3,3,[1,2,3,4,5,6,7,8,9])


"""
Abajo estan los ejecutables de cada funcion por separado,
es importante tener en cuenta las variables necesarias para ejecutar
el codigo correctamente.
Para utilizar las funciones se borra el "#" luego se especifican las variables
"""
j,k,m = 1,2,0
print(matriz.get_pos(j,k))
print(matriz.get_coords(m))
print(matriz.switch(by_row= False))
print(matriz.get_row(j))
print(matriz.get_col(k))
print(matriz.get_elem(m))
print(matriz.del_row(j))
print(matriz.del_col(k))
print(matriz.swap_rows(j1,j2)) #Definir j1,j2
print(matriz.swap_cols(k1,k2)) #Definir k1,k2
print(matriz.scale_row(j,x)) #Definir x
print(matriz.scale_col(k,y)) #Definir y
print(matriz.transpose(matriz.r,matriz.c))
print(matriz.flip_cols())
print(matriz.flip_rows())
print(matriz.__add__(3))
print(matriz.__radd__(2))
print(matriz.__sub__(2))
print(matriz.__rsub__(1))
print(matriz.__mul(3))
print(matriz.sub_matriz(1,matriz.elems))
print(matriz.det())

#Loren cuando corrijas me decis que estoy haciendo mal en la
#funcion del determinante porfavor