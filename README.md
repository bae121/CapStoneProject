# Persona Note API

A Django REST Framework-based API for managing personal notes, weekly summaries, and goals.  
This project provides user authentication, token-based security, and CRUD operations for goals.


# 1. Project Setup
- Created a new Django project called `personal_note_api`.
- Added a local app named `notes` to handle user-related functionality.
- Installed and configured:
  - Django REST Framework (DRF)
  - Token Authentication

---

# 2. Custom User Model
- Defined a custom `User` model in `notes/models.py` extending Django's `AbstractUser`.
- Added extra fields:
  - `daily_notes` > text field for daily reflections
  - `weekly_summary` > text field for weekly summaries
- Configured Django to use this custom model via:
  ```python
  AUTH_USER_MODEL = 'notes.User'
