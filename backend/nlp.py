import csv
import re
import json
from collections import Counter

def nlp_clean_csv(csv_input_path, csv_output_path):
    stopwords = {"the", "and", "or", "a", "an", "in", "on", "at", "to", "for", 
                "with", "by", "of", "from", "as", "is", "was", "were", "be", "been"}

    all_words = []
    usernames = []
    passwords = []
    words_frequency = Counter()

    with open(csv_input_path, "r", encoding="utf-8") as infile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        cleaned_rows = []

        for row in reader:
            if "content" not in row or not row["content"]:
                cleaned_rows.append(row)
                continue

            text = row["content"]
            text_lowercase = text.lower()

            username_keywords = ["username:", "user:", "login:", "@", "email:"]
            for keyword in username_keywords:
                if keyword in text_lowercase:
                    start_pos = text_lowercase.find(keyword) + len(keyword)        
                    remaining_text = text[start_pos:].strip()            
                    potential_username = remaining_text.split()[0] if remaining_text else ""             
                    potential_username = potential_username.rstrip(",.:;!?")
              
                    if potential_username and len(potential_username) >= 3:
                        usernames.append(potential_username)
                        
                    if keyword == "email:" and "@" in remaining_text:
                        email_parts = remaining_text.split()
                        for part in email_parts:
                            if "@" in part and "." in part:
                           
                                email = part.rstrip(",.:;!?")
                                usernames.append(email)
            
            words = text.split()
            for word in words:
                if word.startswith("@") and len(word) > 1:
                    username = word[1:].rstrip(",.:;!?")
                    if username:
                        usernames.append(username)
            
            password_keywords = ["password:", "pwd:", "pass:"]
            for keyword in password_keywords:
                if keyword in text_lowercase:             
                    start_pos = text_lowercase.find(keyword) + len(keyword)               
                    remaining_text = text[start_pos:].strip()                
                    potential_password = remaining_text.split()[0] if remaining_text else ""         
                    potential_password = potential_password.rstrip(",.:;!?")

                    if potential_password and len(potential_password) >= 5:
                        passwords.append(potential_password)
            
            words = []
            for word in text.split():
                clean_word = word.strip(".,!?;:()[]{}\"'")
                if clean_word:
                    words.append(clean_word.lower())
            
            filtered_words = [word for word in words if word not in stopwords and len(word) >= 3]
            
            word_frequency.update(filtered_words)
            
            all_words.extend(filtered_words)
            
            cleaned_text = " ".join(filtered_words)
            row["content"] = cleaned_text
            cleaned_rows.append(row)
    
    repeated_words = [word for word, count in word_frequency.items() if count >= 2]
    
    sorted_words = [word for word, _ in word_frequency.most_common()]
    
    result = {
        "usernames": list(set(usernames)),
        "passwords": list(set(passwords)),
        "frequent_words": [word for word, count in word_frequency.most_common(100)],
        "repeated_words": repeated_words,
        "all_words": sorted_words
    }
    
    with open(txt_output_path, "w", encoding="utf-8") as txt_file:
        txt_file.write("Usernames:\n")
        for username in result["usernames"]:
            txt_file.write(f"{username}\n")
        
        txt_file.write("\nPasswords:\n")
        for password in result["passwords"]:
            txt_file.write(f"{password}\n")
        
        txt_file.write("\nFrequent Words:\n")
        for word in result["frequent_words"]:
            txt_file.write(f"{word}\n")
    
    with open(json_output_path, "w", encoding="utf-8") as json_file:
        json.dump(result, json_file, indent=2)

    with open(csv_output_path, "w", newline="", encoding="utf-8") as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(cleaned_rows)

    print(f"Cleaned CSV created at {csv_output_path}")
    print(f"Wordlist TXT created at {txt_output_path}")
    print(f"Wordlist JSON created at {json_output_path}")

    return result

if __name__ == "__main__":
    csv_input_path = "crawled_data.csv"
    csv_output_path = "cleaned_data.csv"
    txt_output_path = "ai_wordlist.txt"
    json_output_path = "ai_wordlist.json"

    result = nlp_clean_csv(csv_input_path, csv_output_path, txt_output_path, json_output_path)