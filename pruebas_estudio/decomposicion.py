class Automovil:
    
    def __init__(self, modelo,marca,color):
        self.modelo=modelo
        self.marca=marca
        self.color=color
        
        self._estado="en_reposo"
        self._motor=Motor(cilindros=4)
        
        
    def acelerar(self,tipo="despacio"):
        if tipo== 'rapida':
            self._motor.inyecta_gasolina(10)
        else:
            self._motor.inyecta_gasolina(3)
            
            
        self._estado="en_movimiento"   
        
        
    class Motor:
        pass
             