Productor()
{
   int posición = 0;
   for(;;)
   {
      producir un dato;
      wait(huecos);
      buffer[posicion] = dato;
      posición = (posición + 1)%TAMAÑO_BUFFER
      signal(elementos);
   }
}

Consumidor()
{
  int posición = 0;
  for(;;)
  {
    wait(elementos);
    dato = buffer[posicion];
    posición = (posición + 1)%TAMAÑO_BUFFER;
    signal(huecos);
    consumir el dato extraído;
  }
}