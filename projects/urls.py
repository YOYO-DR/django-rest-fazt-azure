from rest_framework import routers
from .api import ProjectViewSet
router = routers.DefaultRouter()

#esta es la ruta, el tercer parametro es el name
router.register('api/projects',ProjectViewSet,'projects')

#igual tengo que pasar un urlpatterns, ya el router hace las 4 rutas principales, las del CRUD
urlpatterns = router.urls

########
#cuando vaya a actualizar solo un dato en la api, utilizo el metodo PATCH, si es todo los datos visibles, entonces el PUL, pq si utilizo el PUL me va a pedir los otros 2 campos aunque no los quiera actualizar