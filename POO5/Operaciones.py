class Operaciones:

    def __init__(self):
        self.numero1=0
        self.numero2=0

    def setNumeros(self):
        formato = False
        while formato == False:
            try: 
                self.numero1 = float( input ("Ingresar primer número: "))
                self.numero2 = float( input("Ingresar segundo número: "))
                
                formato = True
            except ValueError:
                print("Error solomente números")
    

    def suma(self,  numero1 ,  numero2):
        try :
            resultado = numero1 +numero2
            return resultado

        except TypeError:
            return "ERROR POR TIPO DE DATO"
        
      
    
    def resta( self, numero1, numero2):
        resultado = numero1 -numero2
        return resultado
    
    def multiplicacion(self, numero1, numero2):
        return (numero1 *numero2 )
    
    def division(self, numero1, numero2):

        try :
            resultado = numero1/numero2
            return resultado
        
        except ZeroDivisionError:
            return "ERROR"
        
        except TypeError:
            return "ERROR TIPO DE DATO"

      