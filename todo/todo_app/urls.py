from rest_framework import routers
from .views import TodoViewset

router = routers.DefaultRouter()
router.register("tasks", TodoViewset)

# router = routers.DefaultRouter()
# router.register("task", BoardViewset)
