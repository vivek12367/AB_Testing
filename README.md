# 🧪 A/B Testing Tool

An interactive **A/B testing calculator and results analyzer** built with **Streamlit**. This app helps users determine the required **sample size** for an A/B test and analyze the statistical significance of test results.

!![Output](Screenshot(129).png)
---

## 🚀 Features
- **📊 Sample Size Calculator**  
  - Calculates the required sample size for an A/B test based on:
    - **Baseline conversion rate** (current success rate)
    - **Minimum Detectable Effect (MDE)** (expected improvement)
    - **Significance level (alpha)** (false positive risk)
    - **Statistical power** (ability to detect true differences)
  - Plots a **sample size curve** using **Altair** to visualize how sample size changes with MDE.

- **📈 Results Analyzer**  
  - Accepts conversion data for **A & B** groups.
  - Computes:
    - Conversion rates
    - Statistical significance (p-value)
    - Confidence intervals
    - Percentage impact
  - Displays results with **interactive Altair charts**.

- **🎨 Interactive UI**
  - Built with **Streamlit**
  - Uses sliders, number inputs, and dynamic charts.
  - Responsive layout with **tabs for easy navigation**.

---

## 🛠️ Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/ab-testing-tool.git
   cd ab-testing-tool
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app**:
   ```bash
   streamlit run streamlit_app.py
   ```

---

## 📂 File Structure
```
📁 ab-testing-tool/
🌍── 📄 streamlit_app.py        # Main Streamlit application
🌍── 📄 requirements.txt        # List of dependencies
🌍── 📁 assets/                 # Images and icons
🌍── 📄 README.md               # This file
```

---

## 📖 Usage Guide
### **1️⃣ Sample Size Calculator**
1. Go to the **"Sample Size Calculator"** tab.
2. Adjust the sliders for:
   - **Baseline conversion rate** (current success rate)
   - **Minimum Detectable Effect (MDE)** (expected improvement)
   - **Significance level (alpha)**
   - **Statistical power**
3. View the **required sample size** and **sample size curve**.

### **2️⃣ Results Analyzer**
1. Go to the **"Results Analyzer"** tab.
2. Enter the number of **conversions** and **total samples** for **Groups A & B**.
3. Adjust the **confidence level** slider.
4. View:
   - **Conversion rates**
   - **P-value** (statistical significance)
   - **Confidence intervals**
   - **Impact percentage**
   - **Bar chart comparison**

---

## 📊 Understanding Key Terms
| Term | Meaning |
|------|---------|
| **Baseline Conversion Rate** | The current success rate before making changes. |
| **Minimum Detectable Effect (MDE)** | The smallest improvement you want to detect. |
| **Significance Level (Alpha)** | The probability of a false positive (usually set to 0.05 or 5%). |
| **Statistical Power** | The probability of detecting a real effect (typically 80%). |
| **P-value** | The probability that the observed difference is due to chance (p < alpha means statistically significant). |
| **Confidence Interval** | The range in which the true conversion rate is likely to fall. |

---

## 📍 Example
### **Scenario**: You want to test a new **website design**.
- Your current **conversion rate**: **10%** (Baseline)
- You want to detect at least a **2% improvement** (MDE = 2%)
- You set **alpha = 5%** and **power = 80%**
- The tool calculates a required **sample size per group** (e.g., **5,000 users** per group).
- After running the test, you enter your **conversion data** and check if the result is **statistically significant**.

---

## 📝 Dependencies
- **Streamlit** – Web application framework
- **Pandas** – Data manipulation
- **NumPy** – Mathematical operations
- **SciPy** – Statistical analysis
- **Altair** – Data visualization

Install all dependencies using:
```bash
pip install -r requirements.txt
```

---

## 🌟 Contributing
Feel free to **fork this repository** and improve the app! Contributions are welcome.  
To contribute:
1. **Fork** the repo.
2. **Create a new branch**:
   ```bash
   git checkout -b feature-name
   ```
3. **Make your changes** and commit them.
4. **Push to your fork** and submit a **Pull Request**.

