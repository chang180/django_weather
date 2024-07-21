# Django Weather API

This project is a simple Django application that fetches weather data from the Central Weather Bureau API and returns it as JSON.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/django-weather.git
    cd django-weather
    ```

2. Create a virtual environment:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the project root and add your API key:
    ```plaintext
    API_KEY=your_cwb_api_key
    ```

5. Apply migrations:
    ```sh
    python manage.py migrate
    ```

6. Run the development server:
    ```sh
    python manage.py runserver
    ```

## Usage

Visit `http://127.0.0.1:8000/weather/` to fetch weather data.

## Testing

To run tests, use the following command:
    ```sh
    python manage.py test
    ```

## Contributing

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Submit a pull request.

## License

This project is licensed under the MIT License.
