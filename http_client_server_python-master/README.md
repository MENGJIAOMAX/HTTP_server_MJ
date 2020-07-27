# http_client_server_python

This project contains simple http client-server setup written in python.

## Installation
1. Clone this repo.  

2. Create a virtualenv in the root dir of the cloned repo.  
**Note**: ```pip install virtualenv``` if command is not found in your terminal.
    ```sh
    # For Python 2
    virtualenv venv
    # For Python 3
    python3 -m venv venv
    ```
3. Activate the virtualenv created in the previous step.  
**Note**: You can configure Pycharm to set this virtualenv as the python interpreter.  
```source venv/bin/activate```

4. Install lib via requirements.  
    ```sh
    # For Python 2
    pip install -r requirements.txt
    # For Python 3
    pip3 install -r requirements.txt
    ```
## Run the client and server
1. To run the client.  
```sh client.sh```

2. To run the server.  
```sh server.sh```