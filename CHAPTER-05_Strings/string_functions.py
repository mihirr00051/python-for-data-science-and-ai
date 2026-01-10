# STRING FUNCTIONS / METHODS IN PYTHON
# Used heavily in Data Science, AI, and NLP pipelines


# 1. lower() and upper()
# Example 1
text = "Python For AI"
print(text.lower())

# Example 2
language = "machine learning"
print(language.upper())

# Example 3
name = "MiHiR"
print(name.lower())


print("-" * 40)


# 2. strip(), lstrip(), rstrip()
# Example 1
data = "   clean data   "
print(data.strip())

# Example 2
left_space = "   python"
print(left_space.lstrip())

# Example 3
right_space = "ai   "
print(right_space.rstrip())


print("-" * 40)


# 3. replace()
# Example 1
sentence = "I love Python"
print(sentence.replace("love", "learn"))

# Example 2
text = "data,data,data"
print(text.replace(",", " | "))

# Example 3
label = "benign_case"
print(label.replace("_", " "))


print("-" * 40)


# 4. split()
# Example 1
skills = "Python,Data Science,AI"
print(skills.split(","))

# Example 2
sentence = "Deep learning is powerful"
print(sentence.split())

# Example 3
path = "2025/09/21"
print(path.split("/"))


print("-" * 40)


# 5. find() and count()
# Example 1
text = "machine learning"
print(text.find("learn"))

# Example 2
text = "ai ai ai"
print(text.count("ai"))

# Example 3
word = "classification"
print(word.count("i"))


print("-" * 40)


# 6. startswith() and endswith()
# Example 1
filename = "model_v1.py"
print(filename.endswith(".py"))

# Example 2
dataset = "train_data.csv"
print(dataset.endswith(".csv"))

# Example 3
api = "https://api.openai.com"
print(api.startswith("https"))
