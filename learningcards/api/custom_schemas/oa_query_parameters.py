from drf_yasg import openapi

search_param = openapi.Parameter('search', openapi.IN_QUERY, description="Un término de búsqueda", type=openapi.TYPE_STRING)
page_param = openapi.Parameter('page', openapi.IN_QUERY, description="Un número de página dentro del conjunto de resultados paginado.", type=openapi.TYPE_INTEGER)

kit_ordering_param = openapi.Parameter('ordering', openapi.IN_QUERY, 
                                        description="Qué campo utilizar al ordenar los resultados",
                                        type=openapi.TYPE_STRING, 
                                        enum=[
                                                'name',
                                                '-name',
                                                'foreign_language',
                                                '-foreign_language',
                                                'native_language',
                                                '-native_language',
                                                'successful',
                                                '-successful',
                                                ])

kit_name_param = openapi.Parameter('name', openapi.IN_QUERY, description="Nombre", type=openapi.TYPE_STRING)
kit_foreign_language_param = openapi.Parameter('foreign_language', openapi.IN_QUERY, description="Idioma extranjero", type=openapi.TYPE_STRING)
kit_native_language_param = openapi.Parameter('native_language', openapi.IN_QUERY, description="Idioma nativo", type=openapi.TYPE_STRING)
kit_successful_param = openapi.Parameter('successful', openapi.IN_QUERY, description="Éxito (0-100)", type=openapi.TYPE_INTEGER)
kit_minsuccessful_param = openapi.Parameter('min_successful', openapi.IN_QUERY, description="Mínimo éxito (0-100)", type=openapi.TYPE_INTEGER)
kit_maxsuccessful_param = openapi.Parameter('max_successful', openapi.IN_QUERY, description="Máximo éxito (0-100)", type=openapi.TYPE_INTEGER)

card_ordering_param = openapi.Parameter('ordering', openapi.IN_QUERY, 
                                        description="Qué campo utilizar al ordenar los resultados",
                                        type=openapi.TYPE_STRING, 
                                        enum=[
                                                'foreign_word',
                                                '-foreign_word',
                                                'native_word',
                                                '-native_word',
                                                'hits',
                                                '-hits',
                                                'mistakes',
                                                '-mistakes',
                                                'success',
                                                '-success',
                                                ])

card_foreign_word_param = openapi.Parameter('foreign_word', openapi.IN_QUERY, description="Palabra extranjera", type=openapi.TYPE_STRING)
card_native_word_param = openapi.Parameter('native_word', openapi.IN_QUERY, description="Palabra nativa", type=openapi.TYPE_STRING)
card_hits_param = openapi.Parameter('hits', openapi.IN_QUERY, description="Aciertos", type=openapi.TYPE_INTEGER)
card_minhits_param = openapi.Parameter('min_hits', openapi.IN_QUERY, description="Mínimo aciertos", type=openapi.TYPE_INTEGER)
card_maxhits_param = openapi.Parameter('max_hits', openapi.IN_QUERY, description="Máximo aciertos", type=openapi.TYPE_INTEGER)
card_mistakes_param = openapi.Parameter('mistakes', openapi.IN_QUERY, description="Errores", type=openapi.TYPE_INTEGER)
card_minmistakes_param = openapi.Parameter('min_mistakes', openapi.IN_QUERY, description="Mínimo errores", type=openapi.TYPE_INTEGER)
card_maxmistakes_param = openapi.Parameter('max_mistakes', openapi.IN_QUERY, description="Máximo errores", type=openapi.TYPE_INTEGER)
card_success_param = openapi.Parameter('success', openapi.IN_QUERY, description="Éxito (0-100)", type=openapi.TYPE_INTEGER)
card_minsuccess_param = openapi.Parameter('min_success', openapi.IN_QUERY, description="Mínimo éxito ", type=openapi.TYPE_INTEGER)
card_maxsuccess_param = openapi.Parameter('max_success', openapi.IN_QUERY, description="Máximo éxito (0-100)", type=openapi.TYPE_INTEGER)


kit_get_params = [
                    kit_name_param,
                    kit_foreign_language_param,
                    kit_native_language_param,
                    kit_successful_param,
                    kit_minsuccessful_param,
                    kit_maxsuccessful_param,
                    kit_ordering_param,
                    search_param,
                    page_param,
                        ]

card_get_params = [

                    card_ordering_param,
                    card_foreign_word_param,
                    card_native_word_param,
                    card_hits_param,
                    card_minhits_param, 
                    card_maxhits_param,
                    card_mistakes_param,
                    card_minmistakes_param,
                    card_maxmistakes_param,
                    card_success_param,
                    card_minsuccess_param,
                    card_maxsuccess_param,
                    search_param,
                    page_param,
                        ]

