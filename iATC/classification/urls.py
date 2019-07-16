from django.urls import path, include

import classification.views

urlpatterns = [
    path('index', classification.views.get_index_page),
    path('batch', classification.views.batch_predict),
    path('send_email', classification.views.send_email),
    path('smiles', classification.views.get_smiles_page),
    path('description', classification.views.get_description_page),
    path('references', classification.views.get_references_page),
    path('reference', classification.views.get_reference),
    path('predict_result', classification.views.predict_result)
]
