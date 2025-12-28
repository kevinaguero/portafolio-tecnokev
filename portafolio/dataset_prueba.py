"""
Script para poblar la base de datos con datos de prueba
Ejecutar con: python manage.py shell < poblar_datos.py
O desde shell: exec(open('poblar_datos.py').read())
"""

import os
import django
from io import BytesIO
from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portafolio.settings')
django.setup()

from apps.blog.models import Blog
from apps.proyecto.models import Proyecto
from apps.configuraciones.models import Categoria
from django.contrib.auth.models import User

def crear_imagen_placeholder(nombre, ancho=1200, alto=630):
    """Crea una imagen placeholder para pruebas"""
    img = Image.new('RGB', (ancho, alto), color=(73, 109, 137))
    img_io = BytesIO()
    img.save(img_io, format='JPEG', quality=90)
    img_io.seek(0)
    return SimpleUploadedFile(nombre, img_io.read(), content_type='image/jpeg')

# Obtener o crear usuario
user, created = User.objects.get_or_create(
    username='admin',
    defaults={
        'email': 'admin@tecnokev.com',
        'is_staff': True,
        'is_superuser': True
    }
)
if created:
    user.set_password('admin')
    user.save()
    print(f"✓ Usuario creado: {user.username}")
else:
    print(f"✓ Usuario existente: {user.username}")

# Crear categorías si no existen
categorias_data = [
    'Python', 'Django', 'Web Development', 'Machine Learning', 
    'Data Science', 'Automatización', 'API', 'Tutorial',
    'LangChain', 'ChatBots', 'n8n', 'PostgreSQL'
]

categorias = {}
for nombre in categorias_data:
    cat, created = Categoria.objects.get_or_create(nombre=nombre)
    categorias[nombre] = cat
    if created:
        print(f"✓ Categoría creada: {nombre}")

# Datos de proyectos
proyectos_data = [
    {
        'titulo': 'Sistema de Gestión de Inventario',
        'descripcion': 'Aplicación web full-stack para gestión de inventario con Django y PostgreSQL. Incluye reportes en tiempo real, alertas de stock bajo y sistema de usuarios con roles.',
        'categorias': ['Python', 'Django', 'PostgreSQL', 'Web Development'],
        'titulo_boton': 'Ver demo',
        'link_boton': 'https://ejemplo.com/demo',
        'link_github': 'https://github.com/kevinaguero/inventario',
    },
    {
        'titulo': 'Chatbot con RAG y LangChain',
        'descripcion': 'Asistente conversacional que consulta documentos PDF usando RAG (Retrieval Augmented Generation). Implementado con LangChain, OpenAI GPT-4 y Pinecone para búsqueda vectorial.',
        'categorias': ['Python', 'LangChain', 'ChatBots', 'Machine Learning'],
        'titulo_boton': 'Probar bot',
        'link_boton': 'https://ejemplo.com/chatbot',
        'link_github': 'https://github.com/kevinaguero/rag-chatbot',
    },
    {
        'titulo': 'Automatización de Procesos con n8n',
        'descripcion': 'Workflows automatizados que integran múltiples APIs (Slack, Gmail, Google Sheets) para notificaciones, reportes y sincronización de datos. Reduce tiempo operativo en un 60%.',
        'categorias': ['Automatización', 'n8n', 'API'],
        'titulo_boton': 'Ver flujos',
        'link_boton': 'https://ejemplo.com/workflows',
    },
    {
        'titulo': 'Dashboard Analítico en Streamlit',
        'descripcion': 'Panel interactivo para visualización de datos con filtros dinámicos, gráficos en tiempo real y exportación a Excel. Conectado a PostgreSQL y actualización automática.',
        'categorias': ['Python', 'Data Science', 'PostgreSQL'],
        'titulo_boton': 'Ver dashboard',
        'link_boton': 'https://ejemplo.com/dashboard',
        'link_github': 'https://github.com/kevinaguero/dashboard',
    },
    {
        'titulo': 'API RESTful para E-commerce',
        'descripcion': 'API completa con Django REST Framework, autenticación JWT, paginación, filtros avanzados y documentación con Swagger. Maneja productos, carritos, órdenes y pagos.',
        'categorias': ['Python', 'Django', 'API', 'Web Development'],
        'titulo_boton': 'Ver docs',
        'link_boton': 'https://ejemplo.com/api-docs',
        'link_github': 'https://github.com/kevinaguero/ecommerce-api',
    },
    {
        'titulo': 'Pipeline ETL con Airflow',
        'descripcion': 'Orquestación de procesos de extracción, transformación y carga de datos desde múltiples fuentes. Incluye validación, limpieza y almacenamiento en data warehouse.',
        'categorias': ['Python', 'Data Science', 'Automatización', 'PostgreSQL'],
        'link_github': 'https://github.com/kevinaguero/etl-pipeline',
    },
]

# Crear proyectos
print("\n=== CREANDO PROYECTOS ===")
for i, data in enumerate(proyectos_data):
    cats = data.pop('categorias')
    imagen = crear_imagen_placeholder(f'proyecto_{i+1}.jpg', 1200, 675)
    
    proyecto, created = Proyecto.objects.get_or_create(
        titulo=data['titulo'],
        defaults={**data, 'imagen': imagen}
    )
    
    if created:
        proyecto.categorias.set([categorias[c] for c in cats if c in categorias])
        print(f"✓ Proyecto creado: {proyecto.titulo}")
    else:
        print(f"  Proyecto ya existe: {proyecto.titulo}")

# Datos de blogs
blogs_data = [
    {
        'titulo': 'Introducción a LangChain y RAG',
        'descripcion': 'Aprende los fundamentos de LangChain y cómo implementar un sistema RAG para consultar documentos de manera inteligente.',
        'contenido': '''
            <h2>¿Qué es LangChain?</h2>
            <p>LangChain es un framework para desarrollar aplicaciones con modelos de lenguaje grandes (LLMs). Facilita la creación de chatbots, sistemas de preguntas y respuestas, y agentes inteligentes.</p>
            
            <h3>Componentes principales</h3>
            <ul>
                <li><strong>LLMs y Prompts:</strong> Interfaz unificada para diferentes modelos</li>
                <li><strong>Chains:</strong> Secuencias de llamadas a LLMs y otras utilidades</li>
                <li><strong>Agents:</strong> Entidades que toman decisiones sobre qué acciones ejecutar</li>
                <li><strong>Memory:</strong> Persistencia de estado entre llamadas</li>
            </ul>
            
            <h3>Implementación básica de RAG</h3>
            <pre><code>from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
from langchain.chains import RetrievalQA

# Crear embeddings
embeddings = OpenAIEmbeddings()

# Cargar documentos en vector store
vectorstore = Pinecone.from_documents(docs, embeddings)

# Crear chain de QA
qa_chain = RetrievalQA.from_chain_type(
    llm=OpenAI(),
    retriever=vectorstore.as_retriever()
)</code></pre>
            
            <p>Con este código base puedes empezar a construir tu propio sistema de RAG.</p>
        ''',
        'imagen_epigrafe': 'Arquitectura de un sistema RAG con LangChain',
        'categorias': ['Python', 'LangChain', 'Tutorial', 'ChatBots'],
    },
    {
        'titulo': 'Django: Mejores prácticas para APIs',
        'descripcion': 'Guía completa de mejores prácticas para desarrollar APIs RESTful robustas y escalables con Django REST Framework.',
        'contenido': '''
            <h2>Estructura del proyecto</h2>
            <p>Una buena estructura es fundamental para mantener el código organizado y escalable.</p>
            
            <h3>1. Serializers eficientes</h3>
            <pre><code>class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'category_name']
        read_only_fields = ['id', 'created_at']</code></pre>
            
            <h3>2. Vistas basadas en clases</h3>
            <p>Usa ViewSets para reducir código repetitivo:</p>
            <pre><code>class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.select_related('category')
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ['category', 'price']</code></pre>
            
            <h3>3. Paginación</h3>
            <p>Siempre implementa paginación en endpoints que retornan listas:</p>
            <pre><code>REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20
}</code></pre>
        ''',
        'imagen_epigrafe': 'Django REST Framework en acción',
        'categorias': ['Python', 'Django', 'API', 'Web Development', 'Tutorial'],
    },
    {
        'titulo': 'Automatización con n8n: Casos de uso reales',
        'descripcion': 'Descubre cómo n8n puede transformar tus procesos manuales en flujos automatizados eficientes.',
        'contenido': '''
            <h2>¿Qué es n8n?</h2>
            <p>n8n es una herramienta de automatización de workflows de código abierto que te permite conectar diferentes servicios y APIs sin escribir código.</p>
            
            <h3>Caso 1: Notificaciones de GitHub a Slack</h3>
            <ol>
                <li>Webhook de GitHub recibe eventos de push</li>
                <li>n8n procesa el payload</li>
                <li>Formatea el mensaje</li>
                <li>Envía notificación a Slack</li>
            </ol>
            
            <h3>Caso 2: Sincronización de leads</h3>
            <p>Conecta formularios web con tu CRM automáticamente:</p>
            <ul>
                <li>Captura leads desde Google Forms</li>
                <li>Valida y limpia los datos</li>
                <li>Crea contacto en HubSpot</li>
                <li>Envía email de bienvenida</li>
                <li>Notifica al equipo de ventas</li>
            </ul>
            
            <h3>Ventajas de n8n</h3>
            <ul>
                <li>Self-hosted: control total de tus datos</li>
                <li>Integración con 200+ servicios</li>
                <li>Custom nodes con JavaScript</li>
                <li>Debugging visual</li>
            </ul>
        ''',
        'imagen_epigrafe': 'Workflow de n8n para automatización',
        'categorias': ['Automatización', 'n8n', 'Tutorial'],
    },
    {
        'titulo': 'PostgreSQL: Optimización de consultas',
        'descripcion': 'Técnicas avanzadas para mejorar el rendimiento de tus consultas SQL y hacer que tu base de datos vuele.',
        'contenido': '''
            <h2>Análisis de performance</h2>
            <p>Antes de optimizar, necesitas entender qué está pasando.</p>
            
            <h3>EXPLAIN ANALYZE</h3>
            <pre><code>EXPLAIN ANALYZE
SELECT p.*, c.name as category_name
FROM products p
JOIN categories c ON p.category_id = c.id
WHERE p.price > 100;</code></pre>
            
            <h3>Índices estratégicos</h3>
            <p>Los índices son clave para consultas rápidas:</p>
            <pre><code>-- Índice en columnas usadas en WHERE
CREATE INDEX idx_products_price ON products(price);

-- Índice compuesto para búsquedas complejas
CREATE INDEX idx_products_category_price ON products(category_id, price);

-- Índice parcial
CREATE INDEX idx_active_products ON products(id) WHERE active = true;</code></pre>
            
            <h3>Consultas optimizadas</h3>
            <pre><code>-- Evita SELECT *
SELECT id, name, price FROM products;

-- Usa LIMIT en queries grandes
SELECT * FROM logs ORDER BY created_at DESC LIMIT 100;

-- Joins eficientes
SELECT p.name, COUNT(o.id) as order_count
FROM products p
LEFT JOIN orders o ON p.id = o.product_id
GROUP BY p.id, p.name
HAVING COUNT(o.id) > 10;</code></pre>
        ''',
        'imagen_epigrafe': 'Optimización de queries en PostgreSQL',
        'categorias': ['PostgreSQL', 'Tutorial', 'Data Science'],
    },
    {
        'titulo': 'Machine Learning en producción con Python',
        'descripcion': 'De notebooks a APIs: Aprende a llevar tus modelos de ML a producción de manera profesional.',
        'contenido': '''
            <h2>Del notebook al servidor</h2>
            <p>Desarrollar un modelo es solo el primer paso. Aquí te muestro cómo ponerlo en producción.</p>
            
            <h3>1. Serialización del modelo</h3>
            <pre><code>import joblib

# Guardar modelo
joblib.dump(model, 'model.pkl')

# Cargar modelo
model = joblib.load('model.pkl')</code></pre>
            
            <h3>2. API con FastAPI</h3>
            <pre><code>from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class PredictionInput(BaseModel):
    feature1: float
    feature2: float
    feature3: float

@app.post("/predict")
def predict(input_data: PredictionInput):
    features = [[input_data.feature1, input_data.feature2, input_data.feature3]]
    prediction = model.predict(features)
    return {"prediction": float(prediction[0])}</code></pre>
            
            <h3>3. Dockerización</h3>
            <pre><code>FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]</code></pre>
            
            <h3>4. Monitoring</h3>
            <p>No olvides monitorear tus predicciones:</p>
            <ul>
                <li>Latencia de respuesta</li>
                <li>Distribución de inputs</li>
                <li>Drift del modelo</li>
                <li>Errores y excepciones</li>
            </ul>
        ''',
        'imagen_epigrafe': 'Pipeline de ML en producción',
        'categorias': ['Python', 'Machine Learning', 'API', 'Tutorial'],
    },
]

# Crear blogs
print("\n=== CREANDO BLOGS ===")
for i, data in enumerate(blogs_data):
    cats = data.pop('categorias')
    imagen = crear_imagen_placeholder(f'blog_{i+1}.jpg', 1200, 630)
    
    blog, created = Blog.objects.get_or_create(
        titulo=data['titulo'],
        defaults={**data, 'imagen': imagen, 'autor': user}
    )
    
    if created:
        blog.categorias.set([categorias[c] for c in cats if c in categorias])
        print(f"✓ Blog creado: {blog.titulo}")
    else:
        print(f"  Blog ya existe: {blog.titulo}")

print("\n" + "="*50)
print("✓ ¡Datos de prueba creados exitosamente!")
print("="*50)
print(f"\nResumen:")
print(f"- {Proyecto.objects.count()} proyectos")
print(f"- {Blog.objects.count()} blogs")
print(f"- {Categoria.objects.count()} categorías")
