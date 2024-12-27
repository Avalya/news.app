from django.views import View # new
class CommentGet(DetailView): # new
 model = Article
template_name = "article_detail.html"
def get_context_data(self, **kwargs):
 context = super().get_context_data(**kwargs)
 context["form"] = CommentForm()
 return context
class CommentPost(): # new
 pass
class ArticleDetailView(LoginRequiredMixin, View): # new
 def get(self, request, *args, **kwargs):
  view = CommentGet.as_view()
  return view(request, *args, **kwargs)
def post(self, request, *args, **kwargs):
 view = CommentPost.as_view()
 return view(request, *args, **kwargs)