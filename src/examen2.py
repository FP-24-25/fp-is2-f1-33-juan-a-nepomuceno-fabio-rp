
"""No he importado la clase Agragado_lineal del módulo entrega2 
porque he decidido colocar la modificada de la defensa antes 
que la de ColaConLimite"""

from __future__ import annotations
from typing import TypeVar, Generic, List, Callable, Optional
from abc import ABC, abstractmethod

E = TypeVar('E')

class Agregado_lineal(ABC, Generic[E]):
    
    #PROPIEDADES
    def __init__(self,elements: List[E]):  #He decidido que Agregado_lineal pueda implemetar directamente algunos elementos si lo introducimos en una lista en el constructor
        self._elements = elements
    
    @property
    def size(self)->int:
        return (len(self._elements) )
    
    @property
    def is_empty(self)->bool:
        return ( len(self._elements) == 0 )
    
    @property
    def elements(self)->list[E]:
        return self._elements
    
    
    #OTROS MÉTODOS
    @abstractmethod
    def add(self, e: E)->None:
        pass
    
    
    def add_all(self, ls: list[E])->None:
        for var in ls:
            self.add(var)

    def remove(self)->E:
        assert len(self._elements) > 0, 'El agregado está vacío'
        return self._elements.pop(0)

    def remove_all(self)->list[E]:
        eliminados:list[E] = []
        if not self.is_empty:
            for size in range(len(self._elements)):
                eliminados.append(self.remove())
        return eliminados


    def contains(self, e:E)-> bool:
        
        if e in self.elements:
            return True
        else: return False
        
    
    def find(self, func:Callable[[E], bool])-> E | None:
        for i in self.elements:
            if func(i):
                return i
        return None
        
    def filter(self, func:Callable[[E], bool])-> list[E]:
        return [i for i in self.elements if func(i)]
    
        



#CLASE ColaConLimite:

class ColaConLimite(Agregado_lineal):
    def __init__(self, capacidad:int, elements: List[E] = []):
        super().__init__(elements)
        
        self.capacidad = capacidad

    def of(self, capacidad:int) -> ColaConLimite:
        self.capacidad = capacidad
        #el método de factoría no eliminará sus elementos porque ya hay un metodo que se encarga de ello: remove_all()
        return self
    

    
    def add(self, e: E) -> None: 
        if len(self.elements) < self.capacidad:
            self._elements.append(e)
        else: raise OverflowError("La cola está llena.")
        
    def print_cola(self):
        txt='{0}({1})'
        print(txt.format("Cola", self.elements))
        
    def is_full(self) -> bool:
        if len(self.elements) >= self.capacidad:
            return True
        else: return False



"""
Como el metodo add(E) en Agregado_lineal contine unicamente pass en su 
cuerpo, no se puede crear un objeto de dicha clase unicamente, por lo
que voy a testear el funcionamiento de sus métodos usando un objeto
ColaConLimite.
"""
#TEST ColaConLimite

claseCola = ColaConLimite(2)
cola = claseCola.of(3)
cola.add("Tarea1")
cola.add_all(["Tarea 2", "Tarea 3"])
try:
    cola.add("Tarea 4")
except OverflowError as e:
    print(e)
print(cola.remove())

print("-------------------------")
#TEST Agregado_Lineal

AgregadoLineal = ColaConLimite(50,[0])

AgregadoLineal.add_all([1,2,3,4,5,6,7,8,9,10,11,12])

AgregadoLineal.print_cola()

print(AgregadoLineal.contains(3))
print(AgregadoLineal.contains(20))
print(AgregadoLineal.find(lambda x: x == 4))
print(AgregadoLineal.find(lambda x:(x+4==40)))
print(AgregadoLineal.filter(lambda x: (x%2)==0) ) #los pares


