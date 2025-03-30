# eSaral-Hack-apk-1

## Overview
eSaral-Hack-apk-1 is a web application designed to automate the verification of user credentials (UID and Date of Birth combinations) on the "Pravesh" examination website. The app uses asynchronous HTTP requests to efficiently check multiple date combinations for a given UID.


## Installation
To get started with this project, follow these steps:

1. Clone the repository:
    ```sh
    git clone https://github.com/DevLord-Avijit/eSaral-Hack-apk-1.git
    ```

2. Navigate to the project directory:
    ```sh
    cd eSaral-Hack-apk-1
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage
To run the application:

1. Start the Flask application:
    ```sh
    python app.py
    ```

2. Open your web browser and go to `http://localhost:5000`.

3. Enter the UID in the form and submit. The app will check multiple date combinations to find the valid Date of Birth for the provided UID.

## Features
- **Automated UID and DOB Verification:** Checks multiple date combinations for a given UID to find the valid Date of Birth.
- **Asynchronous Requests:** Utilizes aiohttp and asyncio for efficient and concurrent HTTP requests.
- **Flask Web Interface:** Simple web interface to input UID and view results.

## Contributing
Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch:
    ```sh
    git checkout -b feature-branch
    ```
3. Make your changes and commit them:
    ```sh
    git commit -m "Add new feature"
    ```
4. Push to the branch:
    ```sh
    git push origin feature-branch
    ```
5. Open a Pull Request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For any inquiries or feedback, feel free to contact:
- **Avijit Singh** - [GitHub Profile](https://github.com/DevLord-Avijit)
