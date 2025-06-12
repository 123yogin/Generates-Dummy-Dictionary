import random
import string
from datetime import datetime, timedelta
import json

class DummyDataGenerator:
    def __init__(self):
        # Sample data pools
        self.first_names = ["John", "Jane", "Michael", "Sarah", "David", "Emily", "Robert", "Lisa", "James", "Maria"]
        self.last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"]
        self.cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"]
        self.companies = ["TechCorp", "DataSys", "InnovateLab", "FutureTech", "CloudWorks", "DevSolutions", "SmartSystems", "NextGen", "AlphaCode", "BetaLogic"]
        self.departments = ["Engineering", "Marketing", "Sales", "HR", "Finance", "Operations", "IT", "Customer Service", "Research", "Development"]
        self.products = ["Laptop", "Smartphone", "Tablet", "Monitor", "Keyboard", "Mouse", "Headphones", "Speaker", "Camera", "Printer"]
        
        # Key patterns for different data types
        self.key_patterns = {
            'name': ['name', 'full_name', 'username', 'user_name', 'title'],
            'email': ['email', 'email_address', 'contact_email'],
            'age': ['age', 'years_old', 'user_age'],
            'phone': ['phone', 'phone_number', 'contact_number', 'mobile'],
            'address': ['address', 'location', 'city', 'residence'],
            'company': ['company', 'employer', 'organization', 'workplace'],
            'salary': ['salary', 'income', 'wage', 'pay', 'compensation'],
            'date': ['date', 'created_date', 'birth_date', 'joined_date', 'last_login'],
            'boolean': ['active', 'verified', 'premium', 'enabled', 'published'],
            'id': ['id', 'user_id', 'employee_id', 'customer_id', 'order_id'],
            'score': ['score', 'rating', 'points', 'grade', 'level'],
            'description': ['description', 'bio', 'summary', 'notes', 'comments']
        }
    
    def generate_random_string(self, length=8):
        """Generate a random string of specified length"""
        return ''.join(random.choices(string.ascii_letters, k=length))
    
    def generate_email(self, name=None):
        """Generate a realistic email address"""
        if name:
            base = name.lower().replace(' ', '.')
        else:
            base = self.generate_random_string(6).lower()
        
        domains = ["gmail.com", "yahoo.com", "hotmail.com", "company.com", "outlook.com"]
        return f"{base}@{random.choice(domains)}"
    
    def generate_phone(self):
        """Generate a phone number"""
        return f"+1-{random.randint(100, 999)}-{random.randint(100, 999)}-{random.randint(1000, 9999)}"
    
    def generate_date(self):
        """Generate a random date within the last 5 years"""
        start_date = datetime.now() - timedelta(days=365*5)
        random_days = random.randint(0, 365*5)
        return (start_date + timedelta(days=random_days)).strftime("%Y-%m-%d")
    
    def generate_description(self):
        """Generate a random description"""
        adjectives = ["excellent", "outstanding", "professional", "experienced", "dedicated", "innovative", "creative", "reliable"]
        nouns = ["developer", "manager", "specialist", "expert", "consultant", "analyst", "coordinator", "executive"]
        return f"An {random.choice(adjectives)} {random.choice(nouns)} with extensive experience in the field."
    
    def determine_data_type(self, key):
        """Determine what type of data to generate based on key name"""
        key_lower = key.lower()
        
        for data_type, patterns in self.key_patterns.items():
            if any(pattern in key_lower for pattern in patterns):
                return data_type
        
        # Default to mixed random data
        return random.choice(['string', 'number', 'boolean'])
    
    def generate_value_by_type(self, data_type, key):
        """Generate a value based on the determined data type"""
        if data_type == 'name':
            return f"{random.choice(self.first_names)} {random.choice(self.last_names)}"
        
        elif data_type == 'email':
            return self.generate_email()
        
        elif data_type == 'age':
            return random.randint(18, 65)
        
        elif data_type == 'phone':
            return self.generate_phone()
        
        elif data_type == 'address':
            return random.choice(self.cities)
        
        elif data_type == 'company':
            return random.choice(self.companies)
        
        elif data_type == 'salary':
            return random.randint(30000, 150000)
        
        elif data_type == 'date':
            return self.generate_date()
        
        elif data_type == 'boolean':
            return random.choice([True, False])
        
        elif data_type == 'id':
            return random.randint(1000, 99999)
        
        elif data_type == 'score':
            return round(random.uniform(0, 100), 2)
        
        elif data_type == 'description':
            return self.generate_description()
        
        elif data_type == 'string':
            return self.generate_random_string(random.randint(5, 15))
        
        elif data_type == 'number':
            return random.randint(1, 1000)
        
        else:  # boolean
            return random.choice([True, False])
    
    def generate_dummy_dict(self, num_keys):
        """Generate a dictionary with specified number of keys"""
        dummy_dict = {}
        used_keys = set()
        
        # Generate base keys
        base_keys = [
            "name", "email", "age", "phone", "address", "company", 
            "salary", "date", "active", "id", "score", "description"
        ]
        
        for i in range(num_keys):
            if i < len(base_keys):
                key = base_keys[i]
            else:
                # Generate additional keys
                key = f"field_{i+1}"
            
            # Ensure unique keys
            original_key = key
            counter = 1
            while key in used_keys:
                key = f"{original_key}_{counter}"
                counter += 1
            
            used_keys.add(key)
            
            # Generate value based on key type
            data_type = self.determine_data_type(key)
            value = self.generate_value_by_type(data_type, key)
            
            dummy_dict[key] = value
        
        return dummy_dict

def main():
    generator = DummyDataGenerator()
    
    print("=== Dummy Dictionary Data Generator ===\n")
    
    try:
        # Get number of keys from user
        num_keys = int(input("Enter the number of keys you want in the dictionary: "))
        
        if num_keys <= 0:
            print("Please enter a positive number.")
            return
        
        # Generate dummy dictionary
        dummy_data = generator.generate_dummy_dict(num_keys)
        
        print(f"\n=== Generated Dictionary with {num_keys} keys ===\n")
        
        # Pretty print the dictionary
        for key, value in dummy_data.items():
            print(f"{key}: {value}")
        
        print(f"\n=== JSON Format ===\n")
        print(json.dumps(dummy_data, indent=2, default=str))
        
        # Option to generate multiple dictionaries
        while True:
            choice = input("\nGenerate another dictionary? (y/n): ").lower().strip()
            if choice == 'y':
                try:
                    num_keys = int(input("Enter the number of keys: "))
                    if num_keys <= 0:
                        print("Please enter a positive number.")
                        continue
                    
                    dummy_data = generator.generate_dummy_dict(num_keys)
                    print(f"\n=== Generated Dictionary with {num_keys} keys ===\n")
                    
                    for key, value in dummy_data.items():
                        print(f"{key}: {value}")
                    
                    print(f"\n=== JSON Format ===\n")
                    print(json.dumps(dummy_data, indent=2, default=str))
                    
                except ValueError:
                    print("Please enter a valid number.")
            elif choice == 'n':
                print("Thank you for using the Dummy Data Generator!")
                break
            else:
                print("Please enter 'y' for yes or 'n' for no.")
    
    except ValueError:
        print("Please enter a valid number.")
    except KeyboardInterrupt:
        print("\nProgram interrupted. Goodbye!")

if __name__ == "__main__":
    main()