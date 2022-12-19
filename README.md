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
- Bilingüe, botón para cambiar entre inglés y español.
- Sistema de puntaje y progreso.
- Tarjetas dinámicas y reactivas.
- Imagenes aleatorias y recargables relacionadas con la palabra a aprender.
- Paginación de tarjetas.
- Rest API para manejo mayor control de los datos.

## URL To test the web application
https://learningcards.pythonanywhere.com/

## URL To test the web application (API)
Get all the cards with 2 hits and 1 mistake (For Guests).
```sh
   curl "https://learningcards.pythonanywhere.com/api/cards/all/?hits=2&mistakes=1" -u "Invitados:contraseña_invitados"
```
Get kits with with success between 12 and 80 percent (For Guests).
```sh
   curl "https://learningcards.pythonanywhere.com/api/kits/?min_successful=12&max_successful=80" -u "Invitados:contraseña_invitados"
```
To test the API in the browser, you need to log in as a Guest (read only) or as a registered user (with all CRUD functions).
Remember that to enter as a user you only have to press the Guests button on the main page.

https://learningcards.pythonanywhere.com/api/

---
Obtiene todas las cartas con 2 aciertos y 1 error (Para Invitados).
```sh
    curl "https://learningcards.pythonanywhere.com/api/cards/all/?hits=2&mistakes=1" -u "Invitados:contraseña_invitados"
```
Obtiene kits con un éxito entre el 12 y el 80 por ciento (Para Invitados).
```sh
    curl "https://learningcards.pythonanywhere.com/api/kits/?min_successful=12&max_successful=80" -u "Invitados:contraseña_invitados"
```
Para probar la API en el navegador, debe iniciar sesión como invitado (solo lectura) o como usuario registrado (con todas las funciones CRUD).
Recuerda que para ingresar como usuario solo debes presionar el botón de Invitados en la página principal.

https://learningcards.pythonanywhere.com/api/

## URL To test the web application (API-Swagger and ReDoc Documentation)
https://learningcards.pythonanywhere.com/api/swagger/

https://learningcards.pythonanywhere.com/api/redoc/


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

## Example images

### Index
<img src="https://raw.githubusercontent.com/carlosmperilla/Learning-Cards/main/example%20images/examples%20desktop/0%20-%20Inicio.png" alt="Inicio Learning Cards" width="600"/>

### Index - English
<img src="https://raw.githubusercontent.com/carlosmperilla/Learning-Cards/main/example%20images/examples%20desktop/1%20-%20Inicio%20Ingles.png" alt="Index Learning Cards" width="600"/>

### Kits
<img src="https://raw.githubusercontent.com/carlosmperilla/Learning-Cards/main/example%20images/examples%20desktop/2%20-%20kits.png" alt="Kits" width="600"/>

### Kits - Edit
<img src="https://raw.githubusercontent.com/carlosmperilla/Learning-Cards/main/example%20images/examples%20desktop/3%20-%20kits%20edit.png" alt="Kits - Edit" width="600"/>

### Kits - Delete
<img src="https://raw.githubusercontent.com/carlosmperilla/Learning-Cards/main/example%20images/examples%20desktop/4%20-%20kits%20delete.png" alt="Kits - Delete" width="600"/>

### Cards - First Impression
<img src="https://raw.githubusercontent.com/carlosmperilla/Learning-Cards/main/example%20images/examples%20desktop/5%20-%20cards%20first%20impression.png" alt="Cards - First Impression" width="600"/>

### Cards - Second Impression
<img src="https://raw.githubusercontent.com/carlosmperilla/Learning-Cards/main/example%20images/examples%20desktop/5%20-%20cards%20second%20impression.png" alt="Cards - Second Impression" width="600"/>

### Responsive Design - Movil

<p float="left" align="middle">
  <img src="https://raw.githubusercontent.com/carlosmperilla/Learning-Cards/main/example%20images/examples%20movil/0%20-%20movil%20inicio.png" alt="Movil - Index" width="200"/>
    <img src="https://raw.githubusercontent.com/carlosmperilla/Learning-Cards/main/example%20images/examples%20movil/1%20-%20movil%20kit.png" alt="Movil - Kit" width="200"/>
  <img src="https://raw.githubusercontent.com/carlosmperilla/Learning-Cards/main/example%20images/examples%20movil/2%20-%20movil%20kit%20options.png" alt="Movil - Kit Options" width="200"/>
  <img src="https://raw.githubusercontent.com/carlosmperilla/Learning-Cards/main/example%20images/examples%20movil/3%20-%20movil%20cards.png" alt="Movil - Cards" width="200"/>
</p>

