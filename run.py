import os
from notes import note


# TODO: access aws instance with these
aws_key_id = "AKIAIOSFODNN7EXAMPLE"
aws_key_secret = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    note.run(host='0.0.0.0', port=port)
