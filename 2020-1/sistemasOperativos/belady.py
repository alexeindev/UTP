from random import randint

def belady(secuenceList, frameNumber):
    #Mmostramos en la consola la secuencia ¿
    queue = []
    fails = 0

    for pageNumber in secuenceList:
        # pageNumber = int(page)

        if pageNumber in queue:
            pass
        else:
            fails +=1
            if len(queue)== frameNumber:
                queue.pop() #Saca el último elemento 
                queue.insert(0, pageNumber) #Inserta el nuevo elemento
            else: #Si la cola tiene menos elementos que marcos
                queue.insert(0, pageNumber)  #Inserta el nuevo elemento
    print('Frames:', frameNumber,'Fallas:', fails)

def secuenceGenerator(n):
    #Genera un número que será usado como secuencia 
    return [randint(0, 9) for _ in range(n)]
    
if __name__ == "__main__":

    for i in range (15):
        n = secuenceGenerator(12)  #Se genera la secuencia
        print('{} '.format(n)) #Se imprime la secuencia
        #Lo siguiente que se hará es demostrar que los fallos que se tienen con 3 marcos no serán menos si se les añaden mas, esto se demuestra realizando la misma secuencia con 4.
        belady(n, 3)
        belady(n, 4)

        
        

