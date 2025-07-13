# OIBSIP_Python_Task1 - BMI Calculator (Advanced GUI Version)

## 🚀 Objective
Develop a graphical BMI (Body Mass Index) Calculator with data storage and visualization capabilities using Python. This tool helps users calculate and track their BMI over time.

## 🛠️ Steps Performed
- Designed a dark-themed GUI using Tkinter
- Accepted user input: Name, Weight (kg), and Height (m)
- Validated inputs and handled errors gracefully
- Calculated BMI using the formula: `BMI = weight / (height^2)`
- Classified BMI into categories: Underweight, Normal, Overweight, or Obese
- Saved user data to a `.csv` file with timestamps
- Allowed users to visualize their BMI trend over time using `matplotlib`

## 🧰 Tools & Libraries Used
- Python
- Tkinter (GUI)
- CSV module (for storing data)
- Matplotlib (for graphs)
- datetime (for timestamps)

## 💾 Data Storage
All user inputs are saved to a `bmi_data.csv` file with the following fields:
- Date
- Name
- Weight
- Height
- BMI
- Category

## 📊 BMI Trend Analysis
Users can view their BMI history as a line graph filtered by their name. The graph helps monitor BMI fluctuations over time.

## 🎯 Outcome
A fully functional, user-friendly, dark-themed BMI Calculator with data tracking and visualization, fulfilling all the advanced-level objectives of the OIBSIP Task 1.

## 🔎 How to Run
1. Install the required libraries:  
   ```bash
   pip install matplotlib
   ```

2. Run the script:  
   ```bash
   python BMI_Calculator.py
   ```

3. Enter your details and click **Calculate BMI**  
4. Click **Show BMI Trend** to view your graph
