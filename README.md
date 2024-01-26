# Rupload - Django File Sharing App

Welcome to Rupload, a simple file-sharing app built with Django. This app allows users to upload files, and if more than one file is uploaded, it automatically zips them for convenient download.

## Screenshot 
![Screenshot](./Screenshot_3.png)
![Screenshot](./Screenshot_4.png)
## Features

- **File Upload:** Easily upload files using the user-friendly interface.
- **Zip Multiple Files:** If you upload more than one file, Rupload zips them for efficient downloading.
- **Download:** Access your uploaded files and download them whenever you need.

## Getting Started

Follow these steps to get Rupload up and running on your local machine.

### Prerequisites

- Python installed on your system.
- [Pipenv](https://pypi.org/project/pipenv/) for managing virtual environments.

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/Rupload.git
    cd Rupload
    ```

2. **Install dependencies using pipenv:**

    ```bash
    pipenv install
    ```

3. **Activate the virtual environment:**

    ```bash
    pipenv shell
    ```

4. **Apply database migrations:**

    ```bash
    python manage.py migrate
    ```

### Running the App

1. **Start the development server:**

    ```bash
    python manage.py runserver
    ```

2. **Open your browser and go to [http://localhost:8000](http://localhost:8000) to access the app.**

## Usage

1. **Upload Files:**
   - Visit the home page and use the simple upload form to add your files.

2. **Download Files:**
   - Files are available for download on the dedicated download page.

## Code Reference

- **File Upload Handling:**
  - The `FileUploadHandler` class in `views.py` takes care of handling file uploads.

- **File Serialization:**
  - File serialization is handled by the `FileSerializer` and `FileListSerializer` classes in `serializers.py`.

- **Zip Files:**
  - The `zip_files` method in `FileListSerializer` zips the uploaded files if more than one file is present.

## Contributions

Contributions to enhance or extend the functionality of Rupload are welcome. Feel free to open an issue or submit a pull request.

