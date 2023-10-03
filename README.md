# Collector-API: Reddit Data Extractor and Transformer API

This REST API provides two functions to extract and transform text data from Reddit using the Reddit API. It utilizes Redis for storing raw data and NLTK for text transformation. You can easily run the API in a containerized environment using Docker and manage the build steps using the provided Makefile.

## Features

- **Data Extraction:** Retrieve text data from Reddit using Praw lib client for python.

- **Data Transformation:** Transform the extracted text data using NLTK for tasks such as text cleaning, tokenization, and more.

- **Data Storage:** Utilize Redis as a data store to efficiently manage raw data.

## Getting Started

### Prerequisites

Before running the API, ensure you have the following prerequisites installed:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Python 3.10](https://www.python.org/downloads/)
- [NLTK](https://www.nltk.org/install.html)
- Make (to automate the project execution)
- Reddit API credentials (to access Reddit data)

To use the application, you need to create an .env file with the following env variables:
```
REDIS_PORT ----> Redis port to access DB.
REDIS_HOST ----> Redis host public ip.
CLIENT_ID -----> Client id provided by Reddit.
SECRET_TOKEN --> Secret token provided by Reddit.
USER_AGENT ----> User agent provided by Reddit.
SUBREDDIT -----> The subreddit used for data extraction.
N_POSTS -------> The number of most recent messages, used to extract data.
```
### Running the API

1. Clone this repository to your local machine:

   ```bash
   $ git clone https://github.com/yourusername/reddit-data-api.git
   $ cd reddit-data-api
   ```

2. To run the aplication as container, you should run the following command:
    ```bash
    $ make run
    ```

Te swagger doc will be available at [localhost:5000/apidoc/swagger](http://localhost:5000/apidoc/swagger).
You can access the API endpoints for data extraction and transformation.

Run the command below to clear all the files in the docker container from the application modules environment.

1. Run make command to stop containers and clean all files from the app:
    ```bash
    $ make clean
    ```
### API Endpoints
- /extract: Extract text data from Reddit.

- /transform: Transform the extracted data using NLTK for various text processing tasks.

### Usage
- Use the API endpoints ```/extract``` and ```/transform``` to retrieve and transform Reddit data as needed for your application.

- Customize the extraction and transformation logic in the Python files located in the ```app/services``` directory.