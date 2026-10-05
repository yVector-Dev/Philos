from django import forms

from .models import Comment, ReadingList


class EntryForm(forms.Form):
    rating = forms.IntegerField(min_value=0, max_value=10, required=False)
    review = forms.CharField(widget=forms.Textarea(attrs={"rows": 8}), required=False, max_length=12000)
    read_on = forms.DateField(required=False, widget=forms.DateInput(attrs={"type": "date"}))
    reread = forms.BooleanField(required=False, label="I've read this before")
    liked = forms.BooleanField(required=False, label="Like")

    def clean_rating(self):
        return self.cleaned_data.get("rating") or None


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("body",)
        widgets = {"body": forms.Textarea(attrs={"rows": 3, "placeholder": "Add a thoughtful reply…"})}
        labels = {"body": "Reply"}


class ReadingListForm(forms.ModelForm):
    class Meta:
        model = ReadingList
        fields = ("title", "description", "is_ranked")
        widgets = {"description": forms.Textarea(attrs={"rows": 4})}
        labels = {"is_ranked": "Ranked list (show numbers)"}
