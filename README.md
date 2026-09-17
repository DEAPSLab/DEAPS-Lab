# DEAPS Lab Django Website

A Django-based website for DEAPS Lab.

## Setup & Running the Website

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- Git (optional, for cloning)

### Step-by-Step Instructions

1. **Clone or Download the Project**
   ```bash
   git clone <repository-url>
   cd django_website
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv venv
   ```

3. **Activate Virtual Environment**
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`

4. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Navigate to Project Directory**
   ```bash
   cd deapslab
   ```

6. **Run Database Migrations**
   ```bash
   python manage.py migrate
   ```

7. **Start Development Server**
   ```bash
   python manage.py runserver
   ```

8. **Access the Website**
   - Open your browser and go to: `http://127.0.0.1:8000/`
   - The website should now be running locally

### Stopping the Server
- Press `Ctrl+C` in the terminal to stop the development server
- Deactivate virtual environment: `deactivate`


## Deployment

For production deployment:
1. Set `DEBUG = False` in settings.py
2. Configure `ALLOWED_HOSTS`
3. Set up proper database (PostgreSQL recommended)
4. Configure static files serving
5. Use WSGI server like Gunicorn

## URL Structure

- `/` - Home page
- `/about/` - About page
- `/nitin-auluck/` - Prof. Nitin Auluck profile
- `/members/` - Team members
- `/research/` - Research areas
- `/publications/` - Publications
- `/opportunities/` - Job opportunities
- `/news-events/` - News and events
- `/resources/` - Resources
- `/contact/` - Contact information
- `/gallery/` - Photo gallery
- `/alumni/` - Alumni network
