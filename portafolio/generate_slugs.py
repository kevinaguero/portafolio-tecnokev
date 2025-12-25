import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portafolio.settings')
django.setup()

from apps.blog.models import Blog
from django.utils.text import slugify

blogs = Blog.objects.all()
print(f"Generando slugs para {blogs.count()} blogs...")

for blog in blogs:
    if not blog.slug:
        base_slug = slugify(blog.titulo)
        slug = base_slug
        counter = 1
        while Blog.objects.filter(slug=slug).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1
        blog.slug = slug
        blog.save()
        print(f"✓ Slug generado: {blog.titulo} -> {slug}")
    else:
        print(f"- Ya tiene slug: {blog.titulo} -> {blog.slug}")

print("\n¡Listo! Todos los slugs han sido generados.")
