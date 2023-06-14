# Create an app to practise mulitplication tables
    # User specifies number of random practice questions
    # User is presented with a prompt eg. '5 x 5 = ' and inputs the answer for each of the questions
    # When all questions are answered, print out following info:
        # some form of 'thanks for playing' greeting
        # number of correct answers / total answers
        # % correct
        
    # Bonus
        # measure and show time taken to answer - in total and per question
        # let user specify how high the numbers used should be
        # show all questions and answers at the end

import random
from timeit import default_timer as timer

def math_tutor():
    # input number of questions
    num_of_rounds = int(input("How many rounds would you like to play this time?"))
    # specify how high the numbers used should be
    max_num = int(input("What is the highest number you want to multiply?"))
    # initialise score
    total_score = 0
    # initialise lists to store all questions, answers and guesses
    all_questions = []
    all_answers = []
    all_guesses = []
    # initialise timer
    all_times_pq = []
    for i in range(num_of_rounds):
        # generate 2 random integers in range
        num1, num2 = random.randint(1, max_num), random.randint(1, max_num)
        # formulate the question
        question = f"{str(num1)} x {str(num2)} = "
        # save question in list
        all_questions.append(question)
        # start timer
        start = timer()
        # ask the question
        user_guess = int(input(question + "?"))
        # end timer
        end = timer()
        # calculate time taken and save in list
        time_pq = round(end - start, 2)
        all_times_pq.append(time_pq)
        # save guess in list
        all_guesses.append(str(user_guess))
        # calculate correect answer and save in list
        correct_answer = num1 * num2
        all_answers.append(str(correct_answer))
        # check answer
        if user_guess == correct_answer:
            total_score += 1
    # calculate percentage score
    percent = round(total_score / num_of_rounds * 100)
    # calculate total time taken
    total_time = round(sum(all_times_pq), 2)
    # score message
    msg = ""
    if percent >= 90:
        msg = "Congratulations!"
    elif percent == 0:
        msg = "Ouch!"
    else: msg = "Room for improvement!"
    # show all questions, answers and guesses
    summary = [f"{question}{answer}, but you guessed {guess} :(" if guess != answer else f"{question}{answer}. You got it right in {time} milliseconds!" for question, answer, guess, time in zip(all_questions, all_answers, all_guesses, all_times_pq)]
    # print summary line by line
    for line in summary:
        print(line)
    print(f"Total time: {str(total_time)}ms")
    print("Thank you for playing!")
    print(f"You got {str(total_score)} correct out of {str(num_of_rounds)}")
    print(f"That's a score of {percent}%. {msg}")

math_tutor()  