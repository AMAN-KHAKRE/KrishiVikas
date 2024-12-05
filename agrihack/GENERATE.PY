import pandas as pd
import random

# Sample crops list
crops = [
    "Rice", "Maize", "Barley", "Soybean", "Cotton", "Tomato", "Carrot", 
    "Sugarcane", "Potato", "Wheat", "Oats", "Groundnut", "Peas", "Onion", 
    "Cabbage", "Cauliflower", "Brinjal", "Chili", "Garlic", "Ginger", "Turmeric", 
    "Apple", "Mango", "Banana", "Pineapple", "Papaya", "Watermelon", 
    "Pomegranate", "Coconut", "Grapes", "Guava", "Lemon", "Avocado", "Dragonfruit", 
    "Spinach", "Lettuce", "Pumpkin", "Zucchini", "Cucumber", "Radish", "Beetroot", 
    "Basil", "Mint", "Parsley", "Coriander", "Chili Pepper", "Mustard", "Sesame", 
    "Sunflower", "Safflower", "Peanut", "Tea", "Coffee", "Tobacco", "Cassava", 
    "Yam", "Sweet Potato", "Jute", "Hemp", "Taro", "Mushroom", "Kale", "Chickpea", 
    "Lentil", "Lima Bean", "Soybean", "Mung Bean", "Fava Bean", "Black Bean", 
    "Kidney Bean", "Pinto Bean", "Navy Bean", "Cranberry Bean", "Broad Bean", 
    "Chia Seeds", "Flax Seeds", "Pumpkin Seeds", "Sunflower Seeds"
]


# Sample cities list
cities = [
    "Agartala", "Agra", "Ahmedabad", "Ajmer", "Aligarh", "Alipurduar", "Allahabad", "Ambala", "Amritsar", 
    "Aurangabad", "Bagalkot", "Bangalore", "Baran", "Baroda", "Bathinda", "Bhopal", "Bhubaneswar", "Bilaspur", 
    "Chandigarh", "Chandrapur", "Chennai", "Chittorgarh", "Coimbatore", "Cuttack", "Dehradun", "Delhi", 
    "Dhanbad", "Dibrugarh", "Faridabad", "Gandhinagar", "Gangtok", "Gaya", "Ghaziabad", "Gorakhpur", "Gulbarga", 
    "Gurgaon", "Guwahati", "Gwalior", "Haldwani", "Haridwar", "Hyderabad", "Indore", "Jabalpur", "Jaipur", 
    "Jammu", "Jamshedpur", "Jhansi", "Jodhpur", "Kanpur", "Kochi", "Kolkata", "Kota", "Kozhikode", "Lucknow", 
    "Madurai", "Mangalore", "Meerut", "Moradabad", "Mumbai", "Muzaffarpur", "Nagpur", "Nashik", "Noida", 
    "Patna", "Pune", "Raipur", "Rajkot", "Ranchi", "Rishikesh", "Saharanpur", "Sambalpur", "Shimla", "Siliguri", 
    "Surat", "Thane", "Tiruchirappalli", "Tirunelveli", "Vadodara", "Varanasi", "Vijayawada", "Vishakhapatnam", 
    "Visakhapatnam", "Warangal", "Yamunanagar", "Agra", "Kolkata", "Bhubaneswar", "Bhopal", "Surat", "Coimbatore", 
    "Mysore", "Jabalpur", "Patiala", "Indore", "Nagpur", "Vijayawada", "Bhilai", "Mangalore", "Srinagar", "Ranchi", 
    "Amritsar", "Jodhpur", "Gurgaon", "Udaipur", "Durgapur", "Bikaner", "Kota", "Raigarh", "Udupi", "Vellore", 
    "Chandigarh", "Dehradun", "Kolkata", "Kochi", "Puducherry", "Madurai", "Goa", "Patna", "Chennai", "Tirupati", 
    "Kochi", "Bhubaneswar", "Mysore", "Trichy", "Ludhiana", "Bihar Sharif", "Haridwar", "Rajahmundry", "Tirunelveli", 
    "Jamshedpur", "Amritsar", "Ranchi", "Mysuru", "Bhubaneshwar", "Coimbatore", "Meerut", "Nagaland", "Agartala"
]

# Generate data
data = []
for _ in range(1000):
    city = random.choice(cities)
    nitrogen = random.randint(50, 100)
    phosphorus = random.randint(20, 50)
    potassium = random.randint(50, 80)
    pH_value = round(random.uniform(5.5, 7.5), 1)
    rainfall = random.randint(100, 250)
    farm_area = round(random.uniform(1.0, 5.0), 1)
    irrigation_type = random.choice(["Drip", "Flood","Sprinkler"])
    fertilizer_used = random.randint(10,70)
    pesticide_used = random.randint(10,70)
    soil_type = random.choice(["Loam", "Clay", "Sandy"])
    season = random.choice(["Winter", "Summer", "Monsoon", "Rainy"])
    crop = random.choice(crops)
    
    # Generate weather data (temperature, humidity, UV index)
    # temperature = random.randint(20, 40)
    # humidity = random.randint(40, 90)
    # uv_index = random.randint(0, 10)

    # Append all data
    data.append([farm_area, irrigation_type, fertilizer_used, pesticide_used, soil_type, season, rainfall,
                  nitrogen, phosphorus, potassium, pH_value, crop])

# Define correct column names
columns = ['Farm_Area(acres)', 'Irrigation_Type', 'Fertilizer_Used(tons)', 'Pesticide_Used(kg)', 
           'Soil_Type', 'Season', 'Rainfall(mm)',  
           'Nitrogen', 'Phosphorus', 'Potassium', 'pH_Value', 'Crop']

# Create DataFrame
df = pd.DataFrame(data, columns=columns)

# Save to CSV
df.to_csv('real_time_agriculture_data_with_crops.csv', index=False)

print("CSV file has been created!")
