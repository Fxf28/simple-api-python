import requests

# Define parameters for the API request
parameters = {
    "amount": 10,        # Number of questions to fetch
    "type": "boolean"    # Type of question (True/False)
}

def fetch_question_data():
    """
    Fetch quiz question data from the Open Trivia Database API.

    This function makes an HTTP GET request to the OpenTDB API with predefined
    parameters (amount=10, type=boolean). It handles possible errors like
    timeouts, connection issues, and JSON parsing errors.

    Returns:
        list: A list of question data dictionaries. Each dictionary contains 
              'question' and 'correct_answer' fields among others.
              Returns an empty list if an error occurs.
    """
    try:
        response = requests.get(
            "https://opentdb.com/api.php", 
            params=parameters, 
            timeout=10
        )
        response.raise_for_status()  # Raises HTTPError if status != 200
        data = response.json()
        question_data = data.get("results", [])
        return question_data
    except requests.exceptions.Timeout:
        print("Request timed out.")
    except requests.exceptions.ConnectionError:
        print("Connection error occurred.")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    except (ValueError, KeyError) as e:
        print(f"Error parsing response: {e}")
    
    return []  # Fallback if an error happens

# Fetch the question data when the module is imported
# question_data = fetch_question_data()
# print(f"Fetched {len(question_data)} questions.")