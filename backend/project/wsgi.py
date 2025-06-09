import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')  # ← Replace 'project' with your actual project name

application = get_wsgi_application()
