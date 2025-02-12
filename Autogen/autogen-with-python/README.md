# Agentic-AI-Autogen-autogen-with-python

# Autogen AI Assistant

This project demonstrates how to use **Autogen** to create an AI assistant that can generate and modify Python code automatically. The system consists of:
- An **Assistant Agent** (`autogen.AssistantAgent`) responsible for executing tasks.
- A **User Proxy Agent** (`autogen.UserProxyAgent`) that interacts with the assistant and executes code.
- A chat system that allows tasks to be executed sequentially, modifying files dynamically.

---

## **1. Installation & Setup**
To set up the environment and run this project, follow these steps:

### **1.1 Clone the Repository**
First, clone this repository to your local machine and navigate into the project directory:
```sh
git clone https://github.com/yourusername/your-repo.git
cd your-repo
```

### **1.2 Create a Conda Environment**
Create a new Conda environment and activate it:
```sh
conda create --name autogen_env python=3.11 -y
conda activate autogen_env
```

### **1.3 Install Dependencies**
Install the required Python packages:
```sh
pip install pyautogen openai
```

### **1.4 Set Up OpenAI API Key**
You need an OpenAI API key to use this project. Generate your key from:  
🔗 [OpenAI API Keys](https://platform.openai.com/account/api-keys)

Then, add your key to the `config_list` in `main.py`:
```python
config_list = [
    {
        'model': "gpt-4",
        'api_key': "your-api-key-here"
    }
]
```

---

## **2. How It Works**
### **2.1 Running the Code**
Execute the script:
```sh
python main.py
```
The assistant will:
1. **Create a Python file** that prints numbers from 1 to 100.
2. Modify the file to **print numbers from 1 to 200**.

### **2.2 Generated Files**
- The script **automatically generates Python files** in the `web` directory.
- Example output file:
  ```
  web/output.py
  ```

### **2.3 Caching Responses**
- The assistant **caches responses** using the `seed` parameter.
- If the same task is run again, it **reuses cached results** instead of generating new ones.
- This saves **API costs and execution time**.

---

## **3. Customization**
### **3.1 Change Tasks**
Modify `task` and `task2` in `main.py` to execute different commands.

### **3.2 Enable Manual Approval**
If you want **manual approval** before the assistant modifies files, change:
```python
human_input_mode='NEVER'
```
To:
```python
human_input_mode='TERMINATE'
```
This will **prompt for user confirmation** before execution.

---

## **4. Troubleshooting**
### **4.1 API Key Issues**
If you get an API authentication error:
- Ensure your key is **valid** and added to `config_list`.
- Check that **billing is enabled** for your OpenAI account.

### **4.2 Dependencies Not Found**
Run:
```sh
pip install --upgrade pyautogen openai
```
To update the required packages.

### **4.3 Code Execution Issues**
- Ensure that the `web` directory exists before running the script.
- If the assistant doesn’t modify files, check **console logs** for error messages.

---

## **5. Future Improvements**
- Add error handling for **task failures**.
- Implement a **web UI** to monitor file changes in real time.
- Use **LLM fine-tuning** for better task execution.



