"""hopitale URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # ex: /hemato/
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^r/$', views.Recherche.as_view(), name='rech'),
    url(r'^ajoutp/$', views.Ajoutp.as_view(), name='ajoutp'),
    url(r'^1/(?P<slug>[0-9]+)/', views.AfacteurRC.as_view(), name='facris'), #facteur risque cardio..
    url(r'^2/(?P<slug>[0-9]+)/', views.EpisodeT.as_view(), name='epTr'), #episode thrombotique..
    url(r'^3/(?P<slug>[0-9]+)/', views.TromboseVeineuse.as_view(), name='trVe'), # trombose veineuse..
    url(r'^4/(?P<slug>[0-9]+)/', views.TromboseArteriel.as_view(), name='trAr'), # trombose arteriel..
    url(r'^5/(?P<slug>[0-9]+)/', views.AtcdCher.as_view(), name='atcd'), # antecedent cheregucaux..
    url(r'^6/(?P<slug>[0-9]+)/', views.Episodes.as_view(), name='trRec'), # episodes thrombose récidivante.. TromboseRecidivant
    url(r'^7/(?P<slug>[0-9]+)/', views.TromboseRecidivant.as_view(), name='traiACoa'), #traitement anticoagulant au moment de la trombose
    url(r'^8/(?P<slug>[0-9]+)/', views.PathologieMalain.as_view(), name='pathoMaligne'), #pathologie  Maligne (Cancer solide , ....etc)
    url(r'^9/(?P<slug>[0-9]+)/', views.CancerSolide.as_view(), name='CancerSolide'),
    url(r'^10/(?P<slug>[0-9]+)/', views.HemoTissu.as_view(), name='HemoTissu'),
    url(r'^11/(?P<slug>[0-9]+)/', views.SyndroMyelo.as_view(), name='SyndroMyelo'),
    url(r'^12/(?P<slug>[0-9]+)/', views.TraitementAnt.as_view(), name='TraitementAnt'), # trairement anticancereux
    url(r'^13/(?P<slug>[0-9]+)/', views.GrossessInfertilite.as_view(), name='compVasGI'), # complicaton vasculaire de grosses et infertilite
    url(r'^14/(?P<slug>[0-9]+)/', views.ConsultationSuivi.as_view(), name='consulsuivi'), #consultation de suivi
    url(r'^15/(?P<slug>[0-9]+)/', views.BilanBiologique.as_view(), name='bilanBio'), #bilan biologique
    #url(r'^login/', views.Login.as_view(), name='login') deja exist!!
    url(r'^16/(?P<slug>[0-9]+)/', views.ExamenArret.as_view(), name='ExamenArret'), #Examens à faire à l’arrêt du traitement : Hypercoagulabilité ?
    url(r'^17/(?P<slug>[0-9]+)/', views.Recommandation.as_view(), name='Recommandation'), #Recommandations thérapeutiques – Suivi sous traitement
    url(r'^18/(?P<slug>[0-9]+)/', views.MyelomeMultiple.as_view(), name='myelMulti'), #myelome multiple (patho malgine)
    url(r'^19/(?P<slug>[0-9]+)/', views.HemopathiesLigneeMyeloide.as_view(), name='HemoLigMye')  # Hemopathies Lignee Myeloide (patho malgine)


]
