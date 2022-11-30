# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 08:18:31 2022

@author: Helen Moreta
"""
class Problema(object):
    def __init__(self, estado_inicial, estado_final = None):
        self.estado_inicial = estado_inicial
        self.estado_final = estado_final
        
    def acciones(self, estado):
        pass 
        
    def aplica(self, estado, accion):
        pass 
        
    def es_estado_final(self, estado):
        return estado == self.estado_final
    
    def costo_aplicar_accion(self, accion, estado):
        return 1 
    
class Jarras(Problema):
    def __init__(self):
        super().__init__((0,0))
    
    def acciones(self,estado):
        #llenar ,vacir , traspada ---- SIN INFORMACION
        Jarra5 = estado[0]
        Jarra3 = estado[1]
        
        accs = list()
        
            
        if (Jarra5 > 0):
            accs.append("Vaciar jarra de 5L")
            if (Jarra3 < 3):
                accs.append("Traspasar la jarra de 5L a la de 3L")
            
        if (Jarra5 < 5):
            accs.append("llenar jarra de 5L")
            if (Jarra3 > 0):
                accs.append("Traspasar de la jarra de 3L a la de 5L")
        
        if(Jarra3 > 0):
            accs.append("Vaciar jarra de 3L")
            if(Jarra5 < 5):
                accs.append("Traspasar la jarra de 3L a la de 5L")
            
        if(Jarra3 < 3):
            accs.append("llenar jarra de 3L")
            if(Jarra5 > 0):
                accs.append("Traspasar de la jarra de 5L a la de 3L")
        
        return accs
    
    
    def aplica(self,estado,accion):
        J5 = estado[0]
        J3 = estado[1]
        
        if(accion == "llenar jarra de 5L"):
            return(5,J3)
        
        elif(accion== "llenar jarra de 3L"):
            return(J5,3)
                
        elif(accion== "Vaciar jarra de 5L"):
            return(0,J3)
         
        elif(accion== "Vaciar jarra de 3L"):
            return(J5,0)
        
        elif(accion== "Traspasar la jarra de 5L a la de 3L"):
            return(0,J5+J3) if(J5 + J3<=3) else(J5-3+J3,3) 
        
        elif(accion== "Traspasar la jarra de 3L a la de 4L"):
            return(J5+J3,0) if(J5+J3<=5) else(5,J3-5+J5)
        
        
    def es_estado_final(self,estado):
        return estado[0]==2
    
pj =Jarras()
pj.estado_inicial
pj.acciones(pj.estado_inicial)
print(pj.aplica(pj.estado_inicial,"llenar jarra de 5L"))
pj.es_estado_final(pj.estado_inicial)

