from django.urls import path
from main.views import show_main, create_item, show_xml, show_json, show_xml_by_id, show_json_by_id, register, \
    login_user, logout_user, edit_item, delete_item, add_item_ajax, create_exam_flutter

app_name = 'main'

urlpatterns = [
    path('create-item-ajax/', add_item_ajax, name='add_item_ajax'),
    path('delete/<int:id>', delete_item, name='delete_item'),
    path('edit-item/<int:id>', edit_item, name='edit_item'),
    path('logout/', logout_user, name='logout'),
    path('login/', login_user, name='login'),
    path('register/', register, name='register'),
    path('', show_main, name="show_main"),
    path('create-item', create_item, name='create_item'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('create-flutter/', create_exam_flutter, name='create_book_flutter'),
]
