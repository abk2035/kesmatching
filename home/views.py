from django.shortcuts import render, redirect
from admin_datta.forms import RegistrationForm, LoginForm, UserPasswordChangeForm, UserPasswordResetForm, UserSetPasswordForm
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetConfirmView, PasswordResetView
from django.views.generic import CreateView
from django.contrib.auth import logout
from django.utils import timezone
from django.contrib.auth.decorators import login_required
import pandas as pd
from rest_framework.response import Response
from .models import *
from rest_framework.decorators import api_view, renderer_classes


def index(request):

  context = {
    'segment'  : 'index',
    #'products' : Product.objects.all()
  }
  return render(request, "pages/index.html", context)

### work to manage files 
@login_required
@api_view(['POST'])
def uploadFiles(request):
       try:
            excel_file = request.FILES['file']
            
            # Lire le fichier Excel avec Pandas
            df = pd.read_excel(excel_file)

            # Nettoyer les noms de colonnes pour éviter les erreurs
            df.columns = df.columns.str.strip()
            
            # Itérer sur les lignes du DataFrame
            for index, row in df.iterrows():
                  id_unique= row['ID Unique']
                  id_lampadaire = row['ID Lampadaire']
                  commune = row['Commune']
                  zone = row['Zone']
                  photo_jour = row['Photo jour']
                  photo_nuit =row['Photo Nuit']
                  photo_jour_url = row['Photo jour_URL']
                  photo_nuit_url = row['Photo Nuit_URL']
                  submitted_by = row['submitted_by']
                  validation = row['validation']
                  observation = row['observation']
            
                  # Créer un nouvel objet Product
                  Lampadaire.objects.create(id_unique=id_unique,
                                            id_lampadaire=id_lampadaire,
                                            commune=commune,
                                            zone=zone,
                                            photo_jour=photo_jour,
                                            photo_nuit=photo_nuit,
                                            photo_jour_url=photo_jour_url,
                                            photo_nuit_url=photo_nuit_url,
                                            submitted_by=submitted_by,
                                            validation=validation,
                                            observation=observation,
                                            date_created=timezone.now())
                    
            # Retourner une réponse JSON
            return Response({'message': 'File uploaded successfully!'}, status=200)
       
       except Exception as e:
            return Response({'error': f" some error occurred :{str(e)}"}, status=400)
           

## get file pages 
@login_required
def manage_files(request):
  context = {
    'segment': 'files'
  }

  return render(request, "pages/manage-files.html", context)
