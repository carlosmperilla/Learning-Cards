from drf_yasg.utils import swagger_auto_schema
from .oa_query_parameters import card_get_params

card_list_schema = swagger_auto_schema(
    operation_summary="Obtiene las tarjetas paginadas",
    operation_description='Se visualizan maximo *6 tarjetas* por pagina.\n'+
                          '### Ejemplo:\n'+
                          '`GET /cards/`',
    tags=['Cards - Visualización'],
    manual_parameters=card_get_params
)

card_all_schema = swagger_auto_schema(
    operation_summary="Muestra todas las tarjetas sin paginación",
    operation_description='### Ejemplo:\n'+
                          '`GET /cards/all/`',
    tags=['Cards - Visualización'],
    manual_parameters=card_get_params
)

card_retrieve_schema = swagger_auto_schema(
    operation_summary="Obtiene una tarjeta por su id",
    operation_description='### Ejemplo:\n'+
                          '`GET /cards/25/`',
    tags=['Cards - Visualización']
)

card_create_schema = swagger_auto_schema(
    operation_summary="Crea una tarjeta",
    operation_description='### Ejemplo:\n'+
                          '`POST /cards/`',
    tags=['Cards - Creación']
)

card_update_schema = swagger_auto_schema(
    operation_summary="Actualiza una tarjeta por su id",
    operation_description='### Ejemplo:\n'+
                          '`PUT /cards/25/`',
    tags=['Cards - Actualización']
)

card_partial_update_schema = swagger_auto_schema(
    operation_summary="Actualiza una tarjeta parcialmente por su id",
    operation_description='### Ejemplo:\n'+
                          '`PATCH /cards/25/`',
    tags=['Cards - Actualización']
)

card_destroy_schema = swagger_auto_schema(
    operation_summary="Elimina una tarjeta por su id",
    operation_description='### Ejemplo:\n'+
                          '`DELETE /cards/25/`',
    tags=['Cards - Eliminación']
)
