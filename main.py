#this is a test main file
import os
import sys

def main():
    print("This is the main function of the script.")
    print("Current working directory:", os.getcwd())
    print("Python version:", sys.version)

    # Example functionality: simple arithmetic operation
    result = 2 + 2
    print("Result of 2 + 2 is:", result)
    result = 5 * 3
    print("Result of 5 * 3 is:", result)
    #add sample jwt token for testing purposes
    jwt_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWUsImlhdCI6MTUxNjIzOTAyMn0.KMUFsIDTnFmyG3nMiGM6H9FNFUROf3wh7SmqJp-QV30"
    print("Sample JWT token:", jwt_token)
    #add sample github token for testing purposes
    github_token = "ghp_16c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r9s0t"
    print("Sample GitHub token:", github_token)
    #add sample API key for testing purposes
    api_key = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"
    print("Sample API key:", api_key)
    #add sample secret key for testing purposes
    secret = "-----BEGIN RSA PRIVATE KEY-----\nMIIEpAIBAAKCAQEA7v1z3nMiGM6H9FNFUROf3wh7SmqJp-QV30\n-----END RSA PRIVATE KEY-----"
    print("Sample secret key:", secret)
    #add sample password for testing purposes
    password = "P@ssw0rd123"
    print("Sample password:", password)
    #add sample mysql connection string for testing purposes
    mysql_connection_string = "mysql+pymysql://user:password@localhost/dbname"
    print("Sample MySQL connection string:", mysql_connection_string)
    #add sample 

    password1223341
    #code for adding a button to website


    greet("User")

def greet(name):
    """Function to greet a user."""
    print(f"Hello, {name}!")

if __name__ == "__main__":
    main()