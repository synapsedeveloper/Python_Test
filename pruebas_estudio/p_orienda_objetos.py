class Lamp:
    
    LAMPS=['''
          .
     .    |    ,
      \   '   /
       ` ,-. '
    --- (   ) ---
         \ /
        _|=|_
       |_____|
    ''',
    '''
         ,-.
        (   )
         \ /
        _|=|_
       |_____|
    ''']
    
    
    def __init__(self,is_turned_on):
        self._is_turned_on=is_turned_on
        
    def turn_on(self):
        self._is_turned_on=True
        self._display_image()
    
    def turn_off(self):
        self._is_turned_on=False
        self._display_image()   
        
    def _display_image(self):
        
        if self._is_turned_on:
            print (self.LAMPS[0])   
        else:
            print(self.LAMPS[1]) 
            
def run():
    lamp=Lamp(is_turned_on=False) 
    
    while True:
        command = str(input('''
            ¿Que deseas Hacer?
                            
            [p]render
            [a]pagar
            [s]alir                            
                            
            '''))   
        
        if command == 'p':
            lamp.turn_on()
        
        elif command=='a':
            lamp.turn_off()
        
        else:
            break                
               
if __name__ == '__main__':
    run()
            