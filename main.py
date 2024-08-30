import os
from dotenv import load_dotenv
from prompt_execution_sdk import PromptExecutor, YAMLPromptRepository, LLMGateway, Logger

# Load environment variables
load_dotenv()


def main():
    # Initialize components
    base_path = os.getenv('PROMPT_REPO_PATH')
    repository = YAMLPromptRepository(base_path)
    llm_gateway = LLMGateway(api_key=os.getenv('OPENROUTER_API_KEY'))
    logger = Logger(log_dir=os.getenv('LOG_DIR', './logs'))

    # Create the executor
    executor = PromptExecutor(repository, llm_gateway, logger)

    # Example usage
    try:
        result = test_job_ratings(executor)
        print("Execution Result:", result)
        print("Message:", result["choices"][0]["message"]["content"])

        result = test_job_titles(executor)
        print("Execution Result:", result)
        print("Message:", result["choices"][0]["message"]["content"])

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def test_job_ratings(executor):
    # The job-ratings prompt is in the PROMPT_REPO_PATH directory, under the jobspy subdirectory
    #     it takes the parameters: job_titles, desired_words, undesirable_words, resume, job_title, and job_description.
    result = executor.execute_prompt("jobspy/job-ratings", {
        "job_titles": ["Software Engineer", "Full Stack Developer"],
        "desired_words": ["Python", "JavaScript", "AI"],
        "undesirable_words": ["Sales", "Customer Service"],
        "resume": "Experienced software engineer with 5 years of experience in Python and JavaScript development. Passionate about AI and machine learning.",
        "job_title": "Senior Full Stack Developer",
        "job_description": "We're seeking a Senior Full Stack Developer with 7+ years of experience in Python and JavaScript. Experience with AI and machine learning is a plus."
    })
    return result


def test_job_titles(executor):
    result = executor.execute_prompt("jobspy/job-titles", {
        "job_titles": ["Software Engineer", "Full Stack Developer"],
        "skill_words": ["Python", "JavaScript", "AI"],
        "stop_words": ["Sales", "Customer Service"],
        "resume": "Experienced software engineer with 5 years of experience in Python and JavaScript development. Passionate about AI and machine learning."
    })
    return result


if __name__ == "__main__":
    main()
