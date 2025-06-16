import os
import datetime


if __name__ == "__main__":
    #get the current time string for the time output
    # this is used for a single step in the greeting action
    current_time = datetime.datetime.now()
    mytime = f"{current_time:%I:%M%p on %B %d, %Y}"

    GIT_OUTPUT = os.getenv("GITHUB_OUTPUT")
    with open(GIT_OUTPUT, "a", encoding="utf-8") as fp:
        fp.write(f"greeting_time='{mytime}'")