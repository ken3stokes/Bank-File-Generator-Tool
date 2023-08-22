# 🏦 Bank File Generator Tool

## 📜 Introduction

The `Bank File Generator Tool` is a GUI application crafted to help businesses generate transaction files for different banking operations, including Wire (in MT940 format), ACH, and POSPAY. In an era where testing and validation are paramount for financial systems, this tool serves as a valuable asset by generating mock transaction files, aiding in the thorough testing of financial software and systems.

## 🌐 Business Case

Modern banking and financial systems often interact with numerous transaction files daily. Before deploying changes or introducing new systems, rigorous testing is needed to ensure accuracy and reliability. This tool helps developers, testers, and system integrators by providing fictional, yet structurally accurate, transaction files for testing and validation purposes, thereby reducing potential risks and errors in a real-world scenario.

## 💡 Prompt

The idea behind this tool was initiated from a requirement to have an easy-to-use interface that can generate different types of transaction files. The user should be able to:
- Select a staging directory for file generation.
- Generate files with unique names to avoid overwrites.
- Have an option to select the currency for wire transactions.
- Receive immediate feedback on the success or failure of file generation.

## 🌟 Features

- **Directory Selection**: Allows users to specify the destination directory for generated files.
- **Dynamic File Naming**: Integrates a timestamp within filenames to ensure uniqueness.
- **Currency Selection**: Empowers users to select between USD and EUR for wire transactions.
- **Immediate Feedback**: Users are notified immediately about the success or failure of file generation.
  
## 🛠 Setup and Usage

### Requirements

- Python 3.7+
- `tkinter` library (usually bundled with Python)

### Installation

1. Clone the GitHub repository:
   ```bash
   git clone https://github.com/your-username/Bank-File-Generator-Tool.git
   ```
2. Navigate to the cloned directory:
   ```bash
   cd Bank-File-Generator-Tool
   ```
3. Launch the application:
   ```bash
   python main.py
   ```
## 🤝 Contributing

We welcome contributions! If you find a bug or have suggestions, please open an issue. Pull requests are also appreciated. Kindly ensure any major changes are discussed first by opening an issue.

## 📝 License
This project is licensed under the MIT License. See the LICENSE file in the project root for more information.

## 🙏 Acknowledgments

I'd like to express my gratitude to [OpenAI's ChatGPT](https://www.openai.com/chatgpt) for assisting in developing and refining this tool.
