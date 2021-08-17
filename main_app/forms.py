from django.db.models.base import Model
from django.forms import ModelForm, fields
from .models import Feeding

# create a new class called FeedingForm 
# that extends the ModelForm class
class FeedingForm(ModelForm):
    class Meta:
        model = Feeding
        fields = ['date', 'meal']