# 🚀 DecisionFlow

**DecisionFlow** is a smart product recommendation platform that helps users make informed purchasing decisions based on what matters most to them. Instead of relying on generic ratings or endless manual comparisons, users can compare products using their own priorities such as price, performance, battery, storage, or portability. The platform analyzes these preferences and recommends the product that best fits the user's needs.

---

# 🧩 Problem

Choosing the right product has become increasingly difficult due to the overwhelming number of options available online. Buyers often spend hours switching between multiple websites, comparing specifications manually, and trying to balance factors like price, performance, ratings, battery life, and storage.

Most comparison platforms simply display specifications side by side without understanding what is actually important to the individual user. A student looking for affordability, a gamer seeking high performance, and a professional prioritizing portability all have different requirements, yet they receive the same comparison experience.

This results in information overload, decision fatigue, and uncertainty before making a purchase.

---

# 💡 Solution

DecisionFlow transforms traditional product comparison into a personalized decision-making experience.

The platform allows users to:

* Create a secure account.
* Browse and compare multiple products.
* Select the features that matter most by assigning their own priorities.
* Analyze products using a weighted decision engine.
* Receive a recommendation based on their personal preferences rather than generic rankings.

Instead of forcing users to adapt to fixed comparison criteria, DecisionFlow adapts the comparison to the user's own decision-making process.

---

# 🎯 What DecisionFlow Solves

DecisionFlow helps users make confident and personalized purchasing decisions by:

* Reducing the time spent comparing products manually.
* Eliminating confusion caused by information overload.
* Providing recommendations tailored to individual priorities.
* Making the recommendation process transparent through weighted evaluation.
* Offering a simple, secure, and intuitive comparison experience.

Whether someone values affordability, performance, battery life, or portability, DecisionFlow identifies the product that best matches those priorities.

---

# ⚙️ Tech Stack

## Frontend

* React
* Tailwind CSS

## Backend

* FastAPI
* SQLAlchemy
* Pydantic
* JWT Authentication
* SQLite

## Development Tools

* Python
* Git
* GitHub
* VS Code

---

# 🔄 Workflow

```text
User Login
      │
      ▼
Browse Products
      │
      ▼
Create Comparison
      │
      ▼
Select Priority Weights
      │
      ▼
Decision Engine
      │
      ▼
Weighted Analysis
      │
      ▼
Best Product Recommendation
```

---

# 🏗️ Project Setup

## Clone the Repository

```bash
git clone <repository-url>
```

## Backend Setup

```bash
cd backend

python -m venv venv

# Windows
venv\Scripts\activate

# Linux / macOS
source venv/bin/activate

pip install -r requirements

uvicorn app.main:app --reload
```

## Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

---

# 📌 Future Scope

* AI-powered recommendation engine
* Support for additional product categories
* Product review and feedback system
* Cloud database integration
* Advanced filtering and sorting
* Recommendation history
* Interactive comparison charts

---

# 👥 Team

* **Ayush Modanwal** - Backend Development
* **Teammate** - Frontend Development

---

### Built to simplify decision-making through personalized product recommendations.
