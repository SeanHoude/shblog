from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.views.generic import (TemplateView, RedirectView,)
from blog import views
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from blog.sitemap import (PostSitemap, StaticSiteMap, HomepageSiteMap)
from django.contrib.auth.views import (
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView,
)

sitemaps = {
    'posts': PostSitemap,
    'static': StaticSiteMap,
    'homepage': HomepageSiteMap,
}

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('contact/', views.contact, name='contact'),
    path('posts', views.PostListView.as_view()),
    path('posts/<slug>/', views.post_detail, name='post_detail'),
    path('posts/<slug>/edit/', views.edit_post, name='edit_post'),
    path('posts/<slug>/favorite/', views.toggle_favorite, name='toggle_favorite'),
    # Account Registration URL's
    path('accounts/register/', views.MyRegistrationView.as_view(), name='registration_register'),
    path('accounts/create_post/', views.create_post, name='registration_create_post'),
    # Password Reset URL's
    path('accounts/password/reset/', PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name="password_reset"),
    path('accounts/password/reset/done/', PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name="password_reset_done"),
    path('accounts/password/reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name="password_reset_confirm"),
    path('accounts/password/done/', PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name="password_reset_complete"),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('accounts/', include('registration.backends.simple.urls')),
    path('admin/', admin.site.urls),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
