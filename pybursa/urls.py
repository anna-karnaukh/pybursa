from django.views.generic import TemplateView


from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^products/$',TemplateView.as_view(template_name='products.html'),name='products'),
    url(r'^contacts/$',TemplateView.as_view(template_name='contacts.html'),name='contacts'),
    url(r'^product/$',TemplateView.as_view(template_name='product.html'),name='product'),
    url(r'^product2/$',TemplateView.as_view(template_name='product2.html'),name='product2'),
    url(r'^admin/', include(admin.site.urls)),
)
