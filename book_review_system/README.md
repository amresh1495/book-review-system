# Book Review System API

This is a FastAPI-based RESTful API for a hypothetical book review system.

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/amresh1495/book-review-system.git
   cd book-review-system
   ```
2. **Create a virtual environment (optional but recommended):**
    ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4. **Run the migrations:**
    ```bash
    alembic upgrade head
    ```

5. **Run the App**
    ```bash
    uvicorn app.main:app --reload
    ```












