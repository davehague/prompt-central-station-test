# Prompt Central Station (PCS) Test Project
This is a test project for the [PCS SDK](https://github.com/davehague/prompt-central-station/).
It is intended to be a simple example of how to use the SDK.

This first version only supoorts the YAML repository and OpenRouter LLM Gateway.  Your
YAML files should be in the `PROMPT_REPO_PATH` directory, and will follow the 
[Prompty schema](https://github.com/microsoft/prompty/blob/main/Prompty.yaml).

1. Set up your development environment:
   - Create a virtual environment for your test project:
   ```
     python -m venv test_env
     source test_env/bin/activate  # On Windows, use `test_env\Scripts\activate`
     ```

2. Install the PCS SDK in editable mode:
    ```
    pip install -e path/to/your/sdk
    ```

3. Test your prompts
   - Run your `main.py` script


4. Logs will become available in the `logs` directory, specified by the `LOG_DIR` environment variable. 

