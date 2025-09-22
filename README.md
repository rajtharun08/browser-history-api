# Browser History API

This project is a Python-based API that simulates a web browser's history functionality (`visit`, `back`, `forward`). It's built as a hands-on exercise to demonstrate data structures, object-oriented programming, API development, and testing.

The core of the project is a **Doubly Linked List** data structure that manages the history. The history state is made **persistent** by saving to and loading from a JSON file, so it's not lost when the server restarts.

## Features
* **Browser Navigation:** Simulates `visit`, `back`, and `forward` browser functions.
* **Persistent History:** All history is saved to `browser_history.json` and reloaded on startup.
* **Doubly Linked List:** Uses a custom Doubly Linked List to efficiently manage history state.
* **Flask API:** The entire logic is wrapped in a Flask API for interaction.
* **Unit Tested:** Includes a full test suite with `pytest` to ensure the core logic is bug-free.

## Tech Stack
* **Python**
* **Flask:** For the web API.
* **pytest:** For unit testing.

## Installation & Setup

Follow these steps to run the project locally.

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/rajtharun08/browser-history-api.git](https://github.com/rajtharun08/browser-history-api.git)
    ```

2.  **Navigate to the project directory:**
    ```bash
    cd browser-history-api
    ```

3.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    ```

4.  **Activate the virtual environment:**
    * **Windows (CMD):**
        ```bash
        .\venv\Scripts\activate.bat
        ```
    * **Windows (PowerShell):**
        ```bash
        .\venv\Scripts\Activate.ps1
        ```
    * **macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

5.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

## How to Run

### Running the API Server
With your virtual environment active, run the Flask app:
```bash
python api.py
```
The server will start on `http://127.0.0.1:5000`.

### Running the Tests
To verify the core logic, you can run the `pytest` suite:
```bash
pytest
```

## API Endpoints

You can interact with the running API using tools like Postman or `curl`.

| Method | Endpoint | Body (JSON) | Query Params | Description |
| :--- | :--- | :--- | :--- | :--- |
| `GET` | `/current` | (none) | (none) | Gets the URL of the current page. |
| `POST` | `/visit` | `{"url": "..."}` | (none) | Visits a new page. This clears all forward history. |
| `GET` | `/back` | (none) | `?steps=1` | Moves backward in history by the number of steps. |
| `GET` | `/forward` | (none) | `?steps=1` | Moves forward in history by the number of steps. |