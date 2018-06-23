from django import forms

class CommentForm(forms.Form):
    name = forms.CharField(max_length=20,
            widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Name'}))
    comment = forms.CharField(widget=forms.Textarea(attrs={'class' : 'form-control', 'placeholder' : 'Comments'}))
    

    # def __str__(self):
    #     return 

    # def __unicode__(self):
    #     return 
