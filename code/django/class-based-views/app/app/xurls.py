from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^about/', TemplateView.as_view(template_name="about.html")),
)
# Uncomment the next two lines to enable the admin:

# urlpatterns = patterns('',
#     # Examples:
#     # url(r'^$', 'app.views.home', name='home'),
#     # url(r'^app/', include('app.foo.urls')),

#     # Uncomment the admin/doc line below to enable admin documentation:
#     # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

#     # Uncomment the next line to enable the admin:
#     # url(r'^admin/', include(admin.site.urls)),
# )

# class BlogPostDetailView(View):
#     """Displays the details of a BlogPost"""

#     def get(self, request, *args, **kwargs):
#         return TemplateResponse(request, self.get_template_name(),
#                                 self.get_context_data())

#     def get_template_name(self):
#         """Returns the name of the template we should render"""
#         return "blog/blogpost_detail.html"

#     def get_context_data(self):
#         """Returns the data passed to the template"""
#         return {
#             "blogpost": self.get_object(),
#         }

#     def get_object(self):
#         """Returns the BlogPost instance that the view displays"""
#         return get_object_or_404(BlogPost, pk=self.kwargs.get("pk"))
