from django.forms import ModelForm
from .models import *


class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'


class FacteurResiqueForm(ModelForm):
    class Meta:
        model = FacteurResique
        fields = '__all__'

class EpisodeTForm(ModelForm):
    class Meta:
        model = EpisodeT
        fields = '__all__'
        TromboseVeineuse

class TromboseVeineuseForm(ModelForm):
    class Meta:
        model = TromboseVeineuse
        fields = '__all__'

class TromboseArterielForm(ModelForm):
    class Meta:
        model = TromboseArteriel
        fields = '__all__'

class AtcdCherForm(ModelForm):
    class Meta:
        model = AtcdCher
        fields = '__all__'

class EpisodesForm(ModelForm):
    class Meta:
        model = Episodes
        fields = '__all__'

class TromboseRecidivantForm(ModelForm):
    class Meta:
        model = TromboseRecidivant
        fields = '__all__'


class PathologieMalainForm(ModelForm):
    class Meta:
        model = PathologieMalain
        fields = '__all__'

class TraitementAntForm(ModelForm):
    class Meta:
        model = TraitementAnt
        fields = '__all__'

class GrossessInfertiliteForm(ModelForm):
    class Meta:
        model = GrossessInfertilite
        fields = '__all__'

class ConsultationSuiviForm(ModelForm):
    class Meta:
        model = ConsultationSuivi
        fields = '__all__'

class BilanBiologiqueForm(ModelForm):
    class Meta:
        model = BilanBiologique
        fields = '__all__'

class ExamenArretForm(ModelForm):
    class Meta:
        model = ExamenArret
        fields = '__all__'

class RecommandationForm(ModelForm):
    class Meta:
        model = Recommandation
        fields = '__all__'

class MyelomeMultipleForm(ModelForm):
    class Meta:
        model = MyelomeMultiple
        fields = '__all__'

HemopathiesLigneeMyeloide

class HemopathiesLigneeMyeloideForm(ModelForm):
    class Meta:
        model = HemopathiesLigneeMyeloide
        fields = '__all__'

