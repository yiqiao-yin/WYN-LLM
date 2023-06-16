import numpy as np
from scipy.spatial.distance import cosine
from sentence_transformers import SentenceTransformer
import openai
import google.generativeai as palm

def calculate_cosine_similarity(sentence1: str, sentence2: str) -> float:
    """
    Calculate the cosine similarity between two sentences.

    Args:
        sentence1 (str): The first sentence.
        sentence2 (str): The second sentence.

    Returns:
        float: The cosine similarity between the two sentences, represented as a float value between 0 and 1.
    """
    # Tokenize the sentences into words
    words1 = sentence1.lower().split()
    words2 = sentence2.lower().split()

    # Create a set of unique words from both sentences
    unique_words = set(words1 + words2)

    # Create a frequency vector for each sentence
    freq_vector1 = np.array([words1.count(word) for word in unique_words])
    freq_vector2 = np.array([words2.count(word) for word in unique_words])

    # Calculate the cosine similarity between the frequency vectors
    similarity = 1 - cosine(freq_vector1, freq_vector2)

    return similarity


def levenshtein_distance(s1: str, s2: str) -> float:
    """
    Compute the Levenshtein distance between two strings.

    Args:
        s1 (str): The first string.
        s2 (str): The second string.

    Returns:
        float: The Levenshtein distance between the two strings.
    """
    m = len(s1)
    n = len(s2)

    # Create a matrix to store the distances between substrings of s1 and s2
    d = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize the first row and column of the matrix
    for i in range(m + 1):
        d[i][0] = i
    for j in range(n + 1):
        d[0][j] = j

    # Compute the distances between all substrings of s1 and s2
    for j in range(1, n + 1):
        for i in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                d[i][j] = d[i - 1][j - 1]
            else:
                d[i][j] = min(d[i - 1][j], d[i][j - 1], d[i - 1][j - 1]) + 1

    # Return the Levenshtein distance between the two strings
    return d[m][n] * (-1)


def calculate_sts_score(sentence1: str, sentence2: str) -> float:
    model = SentenceTransformer(
        "paraphrase-MiniLM-L6-v2"
    )  # Load a pre-trained STS model

    # Compute sentence embeddings
    embedding1 = model.encode([sentence1])[0]  # Flatten the embedding array
    embedding2 = model.encode([sentence2])[0]  # Flatten the embedding array

    # Calculate cosine similarity between the embeddings
    similarity_score = 1 - cosine(embedding1, embedding2)

    return similarity_score


def openai_text_embedding(prompt: str, key: str) -> str:
    # API Key
    openai.api_key = key

    return openai.Embedding.create(
        input=prompt, model="text-embedding-ada-002"
    )["data"][0]["embedding"]


def calculate_sts_openai_score(sentence1: str, sentence2: str, key: str) -> float:
    # Compute sentence embeddings
    embedding1 = openai_text_embedding(sentence1, key) # Flatten the embedding array
    embedding2 = openai_text_embedding(sentence2, key)  # Flatten the embedding array

    # Convert to array
    embedding1 = np.asarray(embedding1)
    embedding2 = np.asarray(embedding2)

    # Calculate cosine similarity between the embeddings
    similarity_score = 1 - cosine(embedding1, embedding2)

    return similarity_score


def palm_text_embedding(prompt: str, key: str) -> str:
    # API Key
    palm.configure(api_key=key)
    model = "models/embedding-gecko-001"

    return palm.generate_embeddings(model=model, text=prompt)['embedding']


def calculate_sts_palm_score(sentence1: str, sentence2: str, key: str) -> float:
    # Compute sentence embeddings
    embedding1 = palm_text_embedding(sentence1, key) # Flatten the embedding array
    embedding2 = palm_text_embedding(sentence2, key)  # Flatten the embedding array

    # Convert to array
    embedding1 = np.asarray(embedding1)
    embedding2 = np.asarray(embedding2)

    # Calculate cosine similarity between the embeddings
    similarity_score = 1 - cosine(embedding1, embedding2)

    return similarity_score