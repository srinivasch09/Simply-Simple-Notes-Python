# Simply Simple Notes

This is a simple application that stores notes in a SQLite file. This project is
meant to be used as a demo to display some of the [Gitlab's Secure](https://about.gitlab.com/stages-devops-lifecycle/secure/) Features.

This application is meant to be kept clean for demos. In order to showcase Secure features, please copy this application and perform functions in your own path.

## Requirements

- Python
- Pip

## Installation

1. Always use a virtual environment to keep the environment isolated and consistent:
    ```bash
    virtualenv venv
    source venv/bin/activate
    ```
2. Install the Dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

**Starting it up:**

```bash
$ python run.py
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
```

**Adding a note:**

```bash
$ curl -X POST "127.0.0.1:5000/add" -d '{"message":"my n0te"}'
Note added successfully!
```

**Deleting a note:**

```bash
curl -X DELETE "127.0.0.1:5000/delete?id=1"
Note deleted successfully!
```

**Viewing a note:**

```bash
$ curl -X POST "127.0.0.1:5000/add" -d '{"message":"my n0te"}'
Note added successfully!
```
