SwasthAI
SwasthAI is an AI-powered healthcare platform designed for rural and low-resource environments. It provides features like risk detection, multilingual support, offline functionality, and personalized health recommendations.
Features

AI-Powered Risk Detection: Identifies high-risk pregnancies and anemia.
Multilingual Voice & Text Support: Supports regional languages for non-literate users.
Offline Functionality: Works without internet, syncing data when available.
Automated Scheme Eligibility Mapping: Matches patients to government healthcare schemes.
Personalized Dietary & Health Recommendations: Culturally relevant nutritional guidance.
Medical Guidelines & Treatment Support: AI-powered diagnostic support for rural doctors.
Seamless Data Collection & Reporting: Structured reports for frontline workers.
Edge AI: Optimized for low-resource devices.

Installation

Clone the repository:git clone https://github.com/sushantvairat/SwasthAI.git
cd SwasthAI


Create a virtual environment and install dependencies:python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt


Run the application:python src/swasthai/core/main.py


Use the CLI for custom inputs:python src/swasthai/cli/cli.py --name Anita --bp 145 --glucose 150 --hemoglobin 10 --income 400000 --age 36 --language en



Project Structure
SwasthAI/
├── src/
│   ├── swasthai/
│   │   ├── core/           # Core functionality
│   │   ├── utils/          # Utilities (logging, config)
│   │   ├── cli/            # Command-line interface
│   ├── tests/              # Unit tests
├── config/                 # Configuration files
├── data/                   # Database storage
├── README.md
├── requirements.txt
├── setup.py
├── .gitignore

Testing
Run unit tests using:
python -m unittest discover src/tests

Uploading to Git

Initialize a Git repository:git init
git add .
git commit -m "Initial commit"


Create a repository on GitHub and link it:git remote add origin https://github.com/sushantvairat/SwasthAI.git
git branch -M main
git push -u origin main



Creating a ZIP File
To create a ZIP file of the project:

Ensure all files are in the SwasthAI directory.
Run:zip -r SwasthAI.zip SwasthAI


The SwasthAI.zip file will contain the entire project.

Requirements
See requirements.txt for dependencies.
