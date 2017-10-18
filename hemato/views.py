from django.views.generic import TemplateView
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
#from .models import Person, Meuble
#from .forms import PersonForm
from django.urls import reverse
from django.views import View
from .forms import *
from .models import *
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin


def index(request):
    return render(request, 'hemato/accueil.html')

class Login(TemplateView):

    def get(self, request):
        response = {}
        response['a'] = 123
        return render(request, 'hemato/login.html', response)
    def post(self, request):

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return HttpResponse('kayn')
        else:
            # Return an 'invalid login' error message.
            return HttpResponse('mkanech')

        form = PatientForm(request.POST)
        print(form.errors)
        if form.is_valid():

            p = form.save()
            response = {}
            response['id'] = p.pk
            return HttpResponseRedirect(reverse('facris', kwargs={'slug': response['id']}))
            #return redirect("facris",response)
        else:
            return HttpResponse("Form Not Valid (ajoutp)")


class Index(LoginRequiredMixin, TemplateView):

    def get(self, request):
        patients = Patient.objects.all()
        response = {}
        response['patient']=patients
        print(patients.all())
        response['a'] = 123
        return render(request, 'hemato/accueil.html', response)
        #return render(request, 'hemato/fpatient.html', response)

    def post(self, request):
        form = PatientForm(request.POST)
        print(form.errors)
        if form.is_valid():

            p = form.save()
            response = {}
            response['id'] = p.pk
            return HttpResponseRedirect(reverse('facris', kwargs={'slug': response['id']}))
            #return redirect("facris",response)
        else:
            return HttpResponse("Form Not Valid (ajoutp)")


class Ajoutp(LoginRequiredMixin, TemplateView):

    def get(self, request):

        response = {}
        #response['form'] = PersonForm()
        response['a'] = 123
        return render(request, 'hemato/fpatient.html', response)

    def post(self, request):
        form = PatientForm(request.POST)
        print(form.errors)
        if form.is_valid():

            p = form.save()
            response = {}
            response['id'] = p.pk
            return HttpResponseRedirect(reverse('facris', kwargs={'slug': p.pk}))
            #return redirect("facris",response)
        else:
            return HttpResponse("Form Not Valid (ajoutp)")



class AfacteurRC(LoginRequiredMixin, TemplateView):

    def get(self, request, slug):
        #print(self.kwargs)
        response = {}
        #response['form'] = PersonForm()
        response['id'] = self.kwargs['slug']
        print(response['id'])
        return render(request, 'hemato/fFacteurResique.html', response)

    def post(self, request, slug):
        form = FacteurResiqueForm(request.POST)
        print(form.errors)
        if form.is_valid():
            p = form.save()
            response = {}
            response['id'] = p.patient_idpatient.pk
            return HttpResponseRedirect(reverse('epTr', kwargs={'slug': response['id']}))
        else:
            messages.error(request, "Error")
            return render(request, 'hemato/page.html', {'form': FacteurResiqueForm()})
            #return HttpResponse("Form Not Valid (fact)")

class EpisodeT(LoginRequiredMixin, TemplateView):
    def get(self, request, slug):
        response = {}
        response['id'] = self.kwargs['slug']
        return render(request, 'hemato/fEpisodeT.html', response)
    def post(self, request, slug):
        form = FacteurResiqueForm(request.POST)
        print(form.errors)
        if form.is_valid():
            p = form.save()
            response = {}
            response['id'] = p.patient_idpatient.pk
            return HttpResponse("Thank you")
        else:
            messages.error(request, "Error")
            return render(request, 'hemato/page.html', {'form': FacteurResiqueForm()})

class TromboseVeineuse(LoginRequiredMixin, TemplateView):
    def get(self, request, slug):
        response = {}
        response['id'] = self.kwargs['slug']
        return render(request, 'hemato/fTVeineuse.html', response)
    def post(self, request, slug):
        form = TromboseVeineuseForm(request.POST)
        print(form.errors)
        if form.is_valid():
            p = form.save()
            response = {}
            response['id'] = p.patient_idpatient.pk
            return HttpResponseRedirect(reverse('epTr', kwargs={'slug': response['id']}))
        else:
            messages.error(request, "Error")
            return HttpResponse(form.errors)


class TromboseArteriel(LoginRequiredMixin, TemplateView):
    def get(self, request, slug):
        response = {}
        response['id'] = self.kwargs['slug']
        return render(request, 'hemato/fTArteriel.html', response)
    def post(self, request, slug):
        form = TromboseArterielForm(request.POST)
        print(form.errors)
        if form.is_valid():
            p = form.save()
            response = {}
            response['id'] = p.patient_idpatient.pk
            return HttpResponseRedirect(reverse('epTr', kwargs={'slug': response['id']}))
        else:
            messages.error(request, "Error")
            return render(request, 'hemato/page.html', {'form': FacteurResiqueForm()})


class AtcdCher(LoginRequiredMixin, TemplateView):
    def get(self, request, slug):
        response = {}
        response['id'] = self.kwargs['slug']
        return render(request, 'hemato/fatcd_cher.html', response)
    def post(self, request, slug):
        form = AtcdCherForm(request.POST)
        print(form.errors)
        if form.is_valid():
            p = form.save()
            response = {}
            response['id'] = p.patient_idpatient.pk
            return HttpResponseRedirect(reverse('trRec', kwargs={'slug': response['id']}))
        else:
            messages.error(request, "Error")
            return render(request, 'hemato/page.html', {'form': FacteurResiqueForm()})


class Episodes(LoginRequiredMixin, TemplateView):
    def get(self, request, slug):
        response = {}
        response['id'] = self.kwargs['slug']
        return render(request, 'hemato/fTreci.html', response)
    def post(self, request, slug):
        form = EpisodesForm(request.POST)
        print(form.errors)
        if form.is_valid():
            p = form.save()
            response = {}
            response['id'] = p.patient_idpatient.pk
            return HttpResponseRedirect(reverse('trRec', kwargs={'slug': response['id']}))
        else:
            messages.error(request, "Error")
            return render(request, 'hemato/page.html', {'form': FacteurResiqueForm()})

class TromboseRecidivant(LoginRequiredMixin, TemplateView):
    def get(self, request, slug):
        response = {}
        response['id'] = self.kwargs['slug']
        return render(request, 'hemato/ftrACoa.html', response)
    def post(self, request, slug):
        form = TromboseRecidivantForm(request.POST)
        print(form.errors)
        if form.is_valid():
            p = form.save()
            response = {}
            response['id'] = p.patient_idpatient.pk
            return HttpResponseRedirect(reverse('pathoMaligne', kwargs={'slug': response['id']}))
        else:
            messages.error(request, "Error")
            return render(request, 'hemato/page.html', {'form': FacteurResiqueForm()})

class PathologieMalain(LoginRequiredMixin, TemplateView):
    def get(self, request, slug):
        response = {}
        response['id'] = self.kwargs['slug']
        return render(request, 'hemato/fpatho_maligne.html', response)


class CancerSolide(LoginRequiredMixin, TemplateView):
    def get(self, request, slug):
        response = {}
        response['id'] = self.kwargs['slug']
        return render(request, 'hemato/cancer_sol.html', response)
    def post(self, request, slug):
        form = PathologieMalainForm(request.POST)
        print(form.instance)
        print(form.errors)
        if form.is_valid():
            print(form.is_valid())
            p = form.save()
            print("and")
            print(p)
            response = {}
            response['id'] = p.patient_idpatient.pk
            return HttpResponseRedirect(reverse('pathoMaligne', kwargs={'slug': response['id']}))
            return HttpResponse('done!')
        else:
            messages.error(request, "Error")
            return render(request, 'hemato/page.html', {'form': PathologieMalainForm()})

class HemoTissu(LoginRequiredMixin, TemplateView):
    def get(self, request, slug):
        response = {}
        response['id'] = self.kwargs['slug']
        return render(request, 'hemato/hemo_tissu.html', response)
    def post(self, request, slug):
        form = PathologieMalainForm(request.POST)
        print(form.errors)
        if form.is_valid():
            p = form.save()
            response = {}
            response['id'] = p.patient_idpatient.pk
            return HttpResponseRedirect(reverse('pathoMaligne', kwargs={'slug': response['id']}))
            return HttpResponse('done!')
        else:
            messages.error(request, "Error")
            return render(request, 'hemato/page.html', {'form': PathologieMalainForm()})

class SyndroMyelo(LoginRequiredMixin, TemplateView):
    def get(self, request, slug):
        response = {}
        response['id'] = self.kwargs['slug']
        return render(request, 'hemato/syndro_myelo.html', response)
    def post(self, request, slug):
        form = PathologieMalainForm(request.POST)
        print(form.errors)
        if form.is_valid():
            p = form.save()
            response = {}
            response['id'] = p.patient_idpatient.pk
            return HttpResponseRedirect(reverse('pathoMaligne', kwargs={'slug': response['id']}))
            return HttpResponse('done!')
        else:
            messages.error(request, "Error")
            return render(request, 'hemato/page.html', {'form': PathologieMalainForm()})

class MyelomeMultiple(LoginRequiredMixin, TemplateView):
    def get(self, request, slug):
        response = {}
        response['id'] = self.kwargs['slug']
        return render(request, 'hemato/myelomMultiple.html', response)
    def post(self, request, slug):
        form = MyelomeMultipleForm(request.POST)
        print(form.errors)
        if form.is_valid():
            p = form.save()
            response = {}
            response['id'] = p.patient_idpatient.pk
            return HttpResponseRedirect(reverse('pathoMaligne', kwargs={'slug': response['id']}))
            return HttpResponse('done!')
        else:
            messages.error(request, "Error")
            return render(request, 'hemato/page.html', {'form': PathologieMalainForm()})



class TraitementAnt(LoginRequiredMixin, TemplateView):
    def get(self, request, slug):
        response = {}
        response['id'] = self.kwargs['slug']
        return render(request, 'hemato/traiAntiCance.html', response)
    def post(self, request, slug):
        form = TraitementAntForm(request.POST)
        print(form.errors)
        if form.is_valid():
            p = form.save()
            response = {}
            response['id'] = p.patient_idpatient.pk
            return HttpResponseRedirect(reverse('compVasGI', kwargs={'slug': response['id']}))
        else:
            messages.error(request, "Error")
            return render(request, 'hemato/page.html', {'form': PathologieMalainForm()})


class GrossessInfertilite(LoginRequiredMixin, TemplateView):
    def get(self, request, slug):
        response = {}
        response['id'] = self.kwargs['slug']
        return render(request, 'hemato/compVasGrossInf.html', response)
    def post(self, request, slug):
        form = GrossessInfertiliteForm(request.POST)
        print(form.errors)
        if form.is_valid():
            p = form.save()
            response = {}
            response['id'] = p.patient_idpatient.pk
            return HttpResponseRedirect(reverse('bilanBio', kwargs={'slug': response['id']}))
        else:
            messages.error(request, "Error")
            return render(request, 'hemato/page.html', {'form': PathologieMalainForm()})


class BilanBiologique(LoginRequiredMixin, TemplateView):
    def get(self, request, slug):
        response = {}
        response['id'] = self.kwargs['slug']
        return render(request, 'hemato/bilanBio.html', response)
    def post(self, request, slug):
        form = BilanBiologiqueForm(request.POST)
        print(form.errors)
        if form.is_valid():
            p = form.save()
            response = {}
            response['id'] = p.patient_idpatient.pk
            return HttpResponseRedirect(reverse('Recommandation', kwargs={'slug': response['id']}))
        else:
            messages.error(request, "Error")
            return render(request, 'hemato/page.html', {'form': PathologieMalainForm()})


class Recommandation(LoginRequiredMixin, TemplateView):
    def get(self, request, slug):
        response = {}
        response['id'] = self.kwargs['slug']
        return render(request, 'hemato/recomThéra.html', response)
    def post(self, request, slug):
        form = RecommandationForm(request.POST)
        print(form.errors)
        if form.is_valid():
            p = form.save()
            response = {}
            response['id'] = p.patient_idpatient.pk
            return HttpResponseRedirect(reverse('consulsuivi', kwargs={'slug': response['id']}))
            #return HttpResponse('done!')
        else:
            messages.error(request, "Error")
            return render(request, 'hemato/page.html', {'form': PathologieMalainForm()})

class ExamenArret(LoginRequiredMixin, TemplateView):
    def get(self, request, slug):
        response = {}
        response['id'] = self.kwargs['slug']
        return render(request, 'hemato/examArret.html', response)
    def post(self, request, slug):
        form = ExamenArretForm(request.POST)
        print(form.errors)
        if form.is_valid():
            p = form.save()
            response = {}
            response['id'] = p.patient_idpatient.pk
            return HttpResponseRedirect(reverse('Recommandation', kwargs={'slug': response['id']}))
        else:
            messages.error(request, "Error")
            return render(request, 'hemato/page.html', {'form': PathologieMalainForm()})

class ConsultationSuivi(LoginRequiredMixin, TemplateView):
    def get(self, request, slug):
        response = {}
        response['id'] = self.kwargs['slug']
        return render(request, 'hemato/consultation.html', response)
    def post(self, request, slug):
        form = ConsultationSuiviForm(request.POST)
        print(form.errors)
        if form.is_valid():
            p = form.save()
            response = {}
            response['id'] = p.patient_idpatient.pk
            return HttpResponseRedirect(reverse('ExamenArret', kwargs={'slug': response['id']}))
        else:
            messages.error(request, "Error")
            return render(request, 'hemato/page.html', {'form': PathologieMalainForm()})

class Recherche(LoginRequiredMixin, TemplateView):
    def get(self, request):
        response = {}
        #response['id'] = self.kwargs['slug']
        return render(request, 'hemato/recherche.html', response)
    def post(self, request):
        response = {}
        name = request.POST.get("name", "")
        print(name)
        result = Patient.objects.filter(nompatient__contains=name)
        response['patient'] = result
        print(response['patient'])
        return render(request, 'hemato/rechResultats.html', response)

class Dossier(LoginRequiredMixin, TemplateView):
    def get(self, request):
        response = {}
        #response['id'] = self.kwargs['slug']
        return render(request, 'hemato/recherche.html', response)
