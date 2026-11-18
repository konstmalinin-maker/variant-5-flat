"""Совместимый адаптер для старых тестов; бизнес-правила уже в application."""

from database import SQLiteRepository
from src.application.services.university_service import UniversityService as Service


class UniversityService(Service):
    def __init__(self, path):
        super().__init__(SQLiteRepository(path))
