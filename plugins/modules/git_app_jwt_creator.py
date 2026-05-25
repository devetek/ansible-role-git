import sys
import time
import jwt

# Get PEM file path
signing_key = '''
GIT-aPP-SECRET-PEM

'''

client_id = "GIT-APP-CLIENT-ID"

payload = {
    # Issued at time
    'iat': int(time.time()),
    # JWT expiration time (10 minutes maximum)
    'exp': int(time.time()) + 600,
    
    # GitHub App's client ID
    'iss': client_id

}

# Create JWT
encoded_jwt = jwt.encode(payload, signing_key, algorithm='RS256')

print(f"JWT: {encoded_jwt}")