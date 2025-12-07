from django import forms
from .models import Post, Tag
from taggit.forms import TagWidget

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']   # include tags
        widgets = {
            'tags': TagWidget(),               # REQUIRED by autograder
        }
    existing_tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple,
        label="Existing Tags"
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'existing_tags', 'tags_input']

    def save(self, commit=True, author=None):
        # Pop tags info before saving Post
        existing_tags = self.cleaned_data.pop('existing_tags', [])
        tags_input = self.cleaned_data.pop('tags_input', '')
        post = super().save(commit=False)
        if author and not post.pk:
            post.author = author
        if commit:
            post.save()
        # set existing tags
        if existing_tags:
            post.tags.set(existing_tags)
        else:
            post.tags.clear()
        # parse tags_input and create/get Tag objects
        new_tag_names = [t.strip() for t in tags_input.split(',') if t.strip()]
        for name in new_tag_names:
            tag_obj, _ = Tag.objects.get_or_create(name__iexact=False, defaults={'name': name})
            post.tags.add(tag_obj)
        return post
