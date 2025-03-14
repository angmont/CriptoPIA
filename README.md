# Cifrado y Descifrado de Imágenes con S-DES

Este proyecto permite cifrar y descifrar imágenes utilizando el algoritmo **Simplified DES (S-DES)**. Convierte las imágenes a su representación en bits, las cifra con una clave de 10 bits y luego permite su restauración al formato original.

## Características
- **Conversión de imágenes a bits**: Utiliza codificación Base64 para transformar la imagen en texto binario.
- **Cifrado con S-DES**: Aplica dos rondas de S-DES con claves derivadas de una clave de 10 bits.
- **Descifrado**: Restaura la imagen original a partir del cifrado en bits.
- **Validación de claves y archivos**: Verifica que la clave ingresada tenga el formato correcto y que los archivos existan.

## Requisitos
Este proyecto usa Python 3 y requiere las siguientes librerías:
```bash
pip install bitarray numpy
```

## Uso
Ejecuta el script principal:
```bash
python main.py
```

El programa solicitará una opción:
- `1` para cifrar una imagen.
- `2` para descifrar una imagen.

### **Cifrado**
1. Ingresa el nombre del archivo de imagen.
2. Ingresa una clave binaria de 10 bits (ejemplo: `1010101010`).
3. Se genera un archivo cifrado con `_cif` en el nombre.

### **Descifrado**
1. Ingresa el nombre del archivo cifrado.
2. Ingresa la clave utilizada en el cifrado.
3. Se genera un archivo descifrado con `_des` en el nombre.

## Archivos Principales
- `main.py`: Script principal que gestiona la interfaz y el flujo de cifrado/descifrado.
- `encriptado.py`: Implementación de **Simplified DES (S-DES)** para cifrar y descifrar los bits de la imagen.

## Notas
- Este proyecto **no usa 3DES**, sino una versión simplificada de DES con bloques de 8 bits.
- La clave debe ser de exactamente **10 bits** y contener solo `0`s y `1`s.

## Mejoras Futuras
- Implementar 3DES para un cifrado más robusto.
- Mejorar el manejo de errores y validación de datos.
- Agregar una interfaz gráfica para facilidad de uso.

## Licencia
Este proyecto se distribuye bajo la licencia MIT.

