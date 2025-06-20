import os
import re
import sys

def validate_inputs(name: str):
    """ Validate the input name """
    if not name:
        raise ValueError("input_name was empty")
    if not isinstance(name, str):
        raise ValueError("input_name must be a string")

    sanitized = re.sub(r'[;&|><`$(){}\[\]\\]', '', name) 
    if sanitized != name:
        print(f'Untrusted input provided: {sanitized}')
        raise ValueError("Invalid string for input_name")
    else:
        return sanitized


if __name__ == "__main__":
    """This is used for the greeting step in the greeting action"""    
    name = validate_inputs(sys.argv[1])  # scrub
    mytime = sys.argv[2]

    greeting_template = f"""## Greetings :bowtie:\n
    * Hello {name}!
    * We met at {mytime}\n\n
    Generated by: scorpio/greeting
    """
    
    # save the scrubbed name to runner output
    GIT_OUTPUT = os.getenv("GIT_OUTPUT")
    if GIT_OUTPUT:
        with open(GIT_OUTPUT, "a", encoding="utf-8") as fp:
            fp.write(f"output_name={name}")

    STEP_SUMMARY = os.getenv("GITHUB_STEP_SUMMARY")
    # STEP_SUMMARY can use GitHub markdown text
    if STEP_SUMMARY:    
        with open(STEP_SUMMARY, "a", encoding="utf-8") as fp:
            fp.write(greeting_template)