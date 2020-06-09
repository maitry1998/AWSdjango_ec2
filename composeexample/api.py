from rest_framework import routers
from AWSD import api_views as myapp_views

router = routers.DefaultRouter()
router.register(r'members', myapp_views.MembersViewsets,"members")
router.register(r'activity', myapp_views.ActivityViewsets)
