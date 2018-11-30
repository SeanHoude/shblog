class ProposedPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'description', )

    def save(self, commit=True):
        post = super().save(commit=False)
