from drf_yasg.utils import swagger_auto_schema
from .oa_query_parameters import kit_get_params

kit_list_schema = swagger_auto_schema(
    operation_summary="Obtiene los kits paginados",
    operation_description='Se visualizan maximo *6 kits* por pagina.\n'+
                          '### Ejemplo:\n'+
                          '`GET /kits/`',
    tags=['Kits - Visualización'],
    manual_parameters=kit_get_params
)

kit_all_schema = swagger_auto_schema(
    operation_summary="Muestra todos los kits sin paginación",
    operation_description='### Ejemplo:\n'+
                          '`GET /kits/all/`',
    tags=['Kits - Visualización'],
    manual_parameters=kit_get_params
)

kit_retrieve_schema = swagger_auto_schema(
    operation_summary="Obtiene un kit por su id",
    operation_description='### Ejemplo:\n'+
                          '`GET /kits/25/`',
    tags=['Kits - Visualización'],

)

kit_create_schema = swagger_auto_schema(
    operation_summary="Crea un kit, con o sin tarjetas",
    operation_description='Si desea crearse un Kit vacío se puede omitir el campo **cards**\n'+
                          '### Ejemplo:\n'+
                          '`POST /kits/`',
    tags=['Kits - Creación']
)

kit_update_schema = swagger_auto_schema(
    operation_summary="Actualiza un kit por su id",
    operation_description='Se pueden editar las *tarjetas actuales*.\n\n'+
                          'Si desea editar las *tarjetas individualmente*, mejor use:\n\n'+
                          '`PUT /cards/{card_id}/`\n'+
                          '### Ejemplo:\n'+
                          '`PUT /kits/25/`',
    tags=['Kits - Actualización']
)

kit_partial_update_schema = swagger_auto_schema(
    operation_summary="Actualiza un kit parcialmente por su id",
    operation_description='Se pueden editar las *tarjetas actuales*.\n\n'+
                          'Si desea editar las *tarjetas individualmente*, mejor use:\n\n'+
                          '`PATCH /cards/{card_id}/`\n'+
                          '### Ejemplo:\n'+
                          '`PATCH /kits/25/`',
    tags=['Kits - Actualización']
)

kit_destroy_schema = swagger_auto_schema(
    operation_summary="Elimina un kit por su id",
    operation_description='### Ejemplo:\n'+
                          '`DELETE /kits/25/`',
    tags=['Kits - Eliminación']
)
