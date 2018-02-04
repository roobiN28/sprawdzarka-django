from django import forms

from .models import Test, Solution


class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ('input_data', 'output_data')


class SolutionForm(forms.ModelForm):
    class Meta:
        model = Solution
        fields = ('program_code',)
