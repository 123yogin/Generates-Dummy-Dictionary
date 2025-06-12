# 🧪 Dummy Dictionary Data Generator

This Python script generates realistic dummy data in dictionary format for use in testing, prototyping, or educational projects. The generator automatically detects the most appropriate data type based on the field name and fills in values such as names, emails, phone numbers, addresses, salaries, dates, and more.

---

## 🚀 Features

- 🧠 Auto-detects data type using intelligent key pattern matching
- 📧 Realistic data: names, emails, phones, companies, salaries, etc.
- 🔁 Supports generating multiple dictionaries in one session
- 📄 Outputs both pretty-printed and JSON format
- 🧪 Great for testing APIs, UIs, or data ingestion pipelines

---

## 📦 Requirements

- Python 3.6+

> No external dependencies required — uses only Python standard libraries.

---

## 🛠️ How It Works

1. Run the script.
2. Enter the number of key-value pairs you want in your dummy dictionary.
3. The generator intelligently determines the type of data for each key.
4. Outputs a nicely formatted dictionary and JSON version.
5. You can optionally generate more dictionaries in a loop.

---

## 📌 Example

```bash
$ python dummy_data_generator.py
=== Dummy Dictionary Data Generator ===

Enter the number of keys you want in the dictionary: 5

=== Generated Dictionary with 5 keys ===

name: John Smith
email: john.smith@yahoo.com
age: 32
phone: +1-763-493-2718
address: New York

=== JSON Format ===

{
  "name": "John Smith",
  "email": "john.smith@yahoo.com",
  "age": 32,
  "phone": "+1-763-493-2718",
  "address": "New York"
}

🧰 Key Pattern Logic
The script identifies data types using common naming patterns. For example:

email, email_address → generates an email

phone, contact_number → generates a phone number

salary, income → generates a realistic salary

date, joined_date → generates a random date

score, rating, grade → generates a decimal score

etc.

🔁 Loop Mode
After generating one dictionary, the script asks whether you want to create another. You can continue generating as many as you need.

📁 File Structure
Copy
Edit
dummy_data_generator.py
README.md
🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you’d like to change or improve.

📜 License
This project is open-source and available under the MIT License.
