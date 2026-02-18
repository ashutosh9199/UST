import re
from collections import Counter

def intelligent_log_anomalizer(log_file_path, threshold=0.01):
   
    with open(log_file_path, 'r') as f:
        lines = f.readlines()

    # 1. Count occurrences of every unique word
    all_words = []
    for line in lines:
        # Use regex to find alphanumeric words, convert to lowercase
        words = re.findall(r'\b\w+\b', line.lower())
        all_words.extend(words)

    word_counts = Counter(all_words)
    total_words = sum(word_counts.values())
    
    # Calculate frequency threshold (e.g., 1% = 0.01)
    threshold_count = total_words * threshold

    print(f"Total words: {total_words}")
    print(f"Rare word threshold: {threshold_count:.2f} occurrences\n")

    # 2. Flag lines containing rare words
    anomalous_lines = []
    for i, line in enumerate(lines):
        words = re.findall(r'\b\w+\b', line.lower())
        for word in words:
            if word_counts[word] < threshold_count:
                anomalous_lines.append((i + 1, line.strip()))
                break # Flag line once, no need to check other words

    # Display findings
    for line_num, line in anomalous_lines:
        print(f"Anomaly [Line {line_num}]: {line}")

