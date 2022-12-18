# Learning-Cards
Language Learning Cards Web Application
Flashcard vocabulary learning web application:
- Minimalist and responsive interface.
- Bilingual, button to switch between English and Spanish.
- Score and progress system.
- Dynamic and reactive cards.
- Random and rechargeable images related to the word to learn.
- Pagination of cards.
- Rest API for handling greater control of the data.
---
Aplicación web de aprendizaje de vocabulario mediante flashcard:
- Interfaz minimalista y responsiva.
- Bilingüe, boton para cambiar entre inglés y español.
- Sistema de puntaje y progreso.
- Tarjetas dinamicas y reactivas.
- Imagenes aleatorias y recargables relacionadas con la palabra a aprender.
- Paginación de tarjetas.
- Rest API para manejo mayor control de los datos.

## Dependencies
- Python 3.x

## Local Use
Running the following script you can test the operation locally.

- The repository is downloaded locally.
- A virtual environment is created, for the python dependencies.
- The virtual environment is activated.
- The dependencies are installed in the virtual environment.
- The server starts in local 0.0.0.0 is to be able to use the page
   on multiple devices locally,
   as mobile, although the local IP of the router may vary.
---
Ejecutando el siguiente script se puede probar el funcionamiento en local.

- Se descarga el repositorio en local.
- Se crea un entorno virtual, para las dependencias python.
- Se activa el entorno virtual.
- Se instalan las dependencias en el entorno virtual.
- Se inicia el servidor en local 0.0.0.0 es para poder usar la pagina  
  en multiples dipositivos en local,  
  como moviles, aunque la ip local del router puede variar.
  
 ```sh
git clone https://github.com/carlosmperilla/Learning-Cards.git
cd Learning-Cards
python -m venv lc-env
lc-env\Scripts\activate
pip install -r requirements.txt
cd learningcards
python -m manage runserver 0.0.0.0:8000
```

## Is it necessary to sign up?
No, it has a button on the main page, which allows entry as a guest.

This way you can explore the basic operation, trying the Sports, Hobbies and Fruits flashcards.

If you want to edit, delete, use the API with its functionality without restrictions, it is necessary to sign up.

If you need more control of the application the root user is:
>Username: Charles
>
>Password: 12345

I recommend changing the password to a more secure one or removing the root user and creating a new one.

---
No, posee un botón en la pagina principal, que permite el ingreso como invitado/a.

Así se puede explorar el funcionamiento basíco, probando las flashcards de Deportes, Pasatiempos y Frutas.

Si se quiere editar, eliminar, usar la API con su funcionlidad sin restricciones, sí es necesario sign up.

Si necesita más control de la aplicación el superusuario es:
>Username: Carlos
>
>Password: 12345

Recomiendo cambiar el password por uno más seguro o eliminar el superusario y crear uno nuevo.



