# FPL AMD HACC Workshop Poster Gallery
   
{% for item in site.data.gallery.docs %}
<P class="fpl-gal">
    <img src="{{ item.src }}" alt="{{ item.title }}" class="responsive">
</p>
{% endfor %}