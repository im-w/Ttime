#  ________  ________  ______  __       __  ________
# /        |/        |/      |/  \     /  |/        |
# $$$$$$$$/ $$$$$$$$/ $$$$$$/ $$  \   /$$ |$$$$$$$$/
#    $$ |      $$ |     $$ |  $$$  \ /$$$ |$$ |__
#    $$ |      $$ |     $$ |  $$$$  /$$$$ |$$    |
#    $$ |      $$ |     $$ |  $$ $$ $$/$$ |$$$$$/
#    $$ |      $$ |    _$$ |_ $$ |$$$/ $$ |$$ |_____
#    $$ |      $$ |   / $$   |$$ | $/  $$ |$$       |
#    $$/       $$/    $$$$$$/ $$/      $$/ $$$$$$$$/


# Librarys

from datetime import datetime, timedelta
import os


# Defines

yes_words = ["Y", "Yes", "Affirmative", "Amen", "Fine", "Good", "Okay", "True", "Assuredly", "Aye", "Gladly",
             "Roger", "Yep", "Absolutely", "Agreed", "All right", "Certainly", "Sure", "No problem",
             "I'd be happy to", "I guess so", "Yeah", "Yup", "Uh-huh", "Mhmm", "Definitely"]

no_words = ["N", "No", "Nah", "Nope", "Negative", "Nay", "Absolutely not", "Not at all", "By no means",
            "Never", "Under no circumstances", "Not really", "I don't think so", "I'm afraid not",
            "Not likely", "Unfortunately not", "I guess not", "I'd rather not", "Not exactly", "Not quite",
            "Certainly not", "Definitely not"]


# Structures

class Plan:
    def __init__(self, study_time_minutes, break_time_minutes, num_of_study_sections):
        self.study_time_minutes = study_time_minutes
        self.break_time_minutes = break_time_minutes
        self.num_of_study_sections = num_of_study_sections


# Functions

def get_time():
    confirm_time = False

    while (confirm_time == False):
        current_sys_time = datetime.now()
        current_sys_time_str = current_sys_time.strftime("%H:%M")
        print(f"The current time is {current_sys_time_str}.")

        is_time_correct_str = input("is time correct? (Y/n) ").capitalize()
        if is_time_correct_str in yes_words:
            current_time = current_sys_time
            confirm_time = True
        elif is_time_correct_str in no_words:
            current_time_str = input(
                "input your local time like this 12:34 : ")
            try:
                current_time = datetime.strptime(current_time_str, "%H:%M")
                confirm_time = True
            except:
                print("Invalid input, try again.")
        else:
            print("Invalid input, try again.")

    return current_time


def get_plan():
    confirm_plan = False

    while (confirm_plan == False):
        is_default_str = input(
            "Do you want use default 10 x 1h plan? (Y/n) ").capitalize()
        if is_default_str in yes_words:
            plan = Plan(60, 10, 10)
            confirm_plan = True
        elif is_default_str in no_words:
            try:
                study_time_minutes = int(
                    input("How many minutes is each study section? "))
                break_time_minutes = int(
                    input("How many minutes is each break section? "))
                num_of_study_sections = int(
                    input("How many study sections are there in total? "))
                plan = Plan(study_time_minutes, break_time_minutes,
                            num_of_study_sections)
                confirm_plan = True
            except:
                print("Invalid input, try again.")
        else:
            print("Invalid input, try again.")

    return plan


def create_timetable(time, plan):
    timetable = list()
    for index in range(1, plan.num_of_study_sections + 1):
        row = list()
        # row = [index, start_time, end_time, section_name, description]

        # index
        row.append(index)

        # start_time
        time_str = time.strftime("%H:%M")
        row.append(time_str)

        # end_time
        time = time + timedelta(minutes=plan.study_time_minutes)
        time_str = time.strftime("%H:%M")
        row.append(time_str)

        # section_name
        row.append("study section : ")

        # description
        print(f"write a description for study section number {index} : ")
        description = input()
        row.append(description)

        timetable.append(row)

        if index != (plan.num_of_study_sections + 1):
            row = list()
            # row = [index, start_time, end_time, section_name, description]

            # index
            row.append(index)

            # start_time
            time_str = time.strftime("%H:%M")
            row.append(time_str)

            # end_time
            time = time + timedelta(minutes=plan.break_time_minutes)
            time_str = time.strftime("%H:%M")
            row.append(time_str)

            # section_name
            row.append("break")

            # description
            description = ''
            row.append(description)

            timetable.append(row)

    return timetable


def print_timetable(timetable):
    rows = len(timetable)
    cols = len(timetable[0])

    # Print column headers
    print("    ", end="")
    for col_header in ["StartTime", "EndTime", "SectionName", "Description"]:
        print(f"{col_header}", end=" ")
    print("\n" + "-" * (4 * cols + 1))

    # Print rows
    for row in range(rows):
        print(f"{row + 1:2}" + "|", end=" ")
        for col in range(1, cols):
            print(f"{timetable[row][col]:2}", end=" ")
        print()


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_output(greatful_str, life_goal_str, today_goal_str, timetable):
    print('\x1b[6;30;42m' + 'Time Table' + '\x1b[0m')
    print('You are greatful for : ' + greatful_str)
    print('Your life goal is    : ' + life_goal_str)
    print('Your Today goal is   : ' + today_goal_str)
    print_timetable(timetable)


# Main

def main():
    greatful_str = input("Why you are Greatful for today? ")
    life_goal_str = input("What is your goal in your whole life? ")
    today_goal_str = input("What do you want from today? ")

    time = get_time()

    time_str = time.strftime("%H:%M")
    print(f"The time set at {time_str}.")
    plan = get_plan()

    timetable = create_timetable(time, plan)
    clear_terminal()

    print_output(greatful_str, life_goal_str, today_goal_str, timetable)



if __name__ == "__main__":
    main()
