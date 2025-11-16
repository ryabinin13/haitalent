# import pytest
# from fastapi.testclient import TestClient
# import sys
# import os

# # Добавляем корневую директорию в путь
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# from app.main import app  # импортируйте из вашего главного файла

# @pytest.fixture
# def client():
#     return TestClient(app)