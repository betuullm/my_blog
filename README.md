# Medium Blog Project

This is a Django-based blog application inspired by Medium. The project is structured to provide a clean and maintainable codebase, following best practices for Django development.

## Features

- User-friendly interface for reading and writing blog posts.
- Responsive design similar to Medium.
- Easy management of blog posts through the Django admin interface.
- Support for future enhancements, such as user authentication and comments.

## Project Structure

```
medium_blog/
├── blog/                  # Blog application
│   ├── admin.py          # Admin configuration for blog models
│   ├── apps.py           # Blog application configuration
│   ├── migrations/        # Database migrations
│   ├── models.py         # Data models for the blog
│   ├── templates/        # HTML templates
│   ├── static/           # Static files (CSS, JS)
│   ├── tests.py          # Test cases for the blog application
│   ├── urls.py           # URL patterns for the blog
│   └── views.py          # View functions for handling requests
├── medium_blog/          # Project configuration
│   ├── __init__.py       # Package initialization
│   ├── asgi.py           # ASGI entry point
│   ├── settings.py       # Project settings
│   ├── urls.py           # Project URL patterns
│   └── wsgi.py           # WSGI entry point
├── manage.py              # Command-line utility for the project
└── README.md              # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd medium_blog
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```
   python manage.py migrate
   ```

5. Run the development server:
   ```
   python manage.py runserver
   ```

## Usage

- Access the blog at `http://127.0.0.1:8000/`.
- Use the Django admin interface at `http://127.0.0.1:8000/admin/` to manage blog posts.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.