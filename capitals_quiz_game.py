import random
from typing import List
import time


class QuestionsAndAnswers:
    def __init__(self, questions: str, correct_answer: str, other_answers: List[str]):
        self.question = questions
        self.correct_answer = correct_answer
        self.other_answers = other_answers


question_and_answer_list = [QuestionsAndAnswers('What is the capital city of Bulgaria 🇧🇬?',
                                                'Sofia',
                                                ['Bucharest', 'Belgrade', 'Athens']),
                            QuestionsAndAnswers('What is the capital city of France 🇫🇷?',
                                                'Paris',
                                                ['Toulouse', 'Strasbourg', 'Nantes']),
                            QuestionsAndAnswers('What is the capital city of Germany 🇩🇪?',
                                                'Berlin',
                                                ['Hamburg', 'Munich', 'Frankfurt']),
                            QuestionsAndAnswers('What is the capital city of Spain 🇪🇸?',
                                                'Madrid',
                                                ['Barcelona', 'Sevilla', 'Sofia']),
                            QuestionsAndAnswers('What is the capital city of Italy 🇮🇹?',
                                                'Rome',
                                                ['Florence', 'Milan', 'Venice']),
                            QuestionsAndAnswers('What is the capital city of Netherlands 🇳🇱?',
                                                'Amsterdam',
                                                ['Oslo', 'Rotterdam', 'Utrecht']),
                            QuestionsAndAnswers('What is the capital city of Portugal 🇵🇹?',
                                                'Lisbon',
                                                ['Bern', 'Porto', 'Vila Nova de Lisboa']),
                            QuestionsAndAnswers('What is the capital city of Sweden 🇸🇪?',
                                                'Stockholm',
                                                ['Rotterdam', 'Uppsala', 'Västerås']),
                            QuestionsAndAnswers('What is the capital city of Switzerland 🇨🇭?',
                                                'Bern',
                                                ['Ultrecht', 'Basel-Landschaft', 'Basel-Stadt']),
                            QuestionsAndAnswers('What is the capital city of United Kingdom 🇬🇧?',
                                                'London',
                                                ['Liverpool', 'Birmingham', 'Bristol']),
                            QuestionsAndAnswers('What is the capital city of United States 🇺🇸?',
                                                'Washington',
                                                ['Seattle', 'Arlington', 'Tacoma']),
                            QuestionsAndAnswers('What is the capital city of United Arab Emirates 🇦🇪?',
                                                'Abu Dhabi',
                                                ['Dubai', 'Sharjah', 'Umm al Qayway']),
                            QuestionsAndAnswers('What is the capital city of Argentina 🇦🇷?',
                                                'Buenos Aires',
                                                ['Dubai', 'Catamarca', 'La Rioja']),
                            QuestionsAndAnswers('What is the capital city of Australia 🇦🇺?',
                                                'Canberra',
                                                ['Melbourne', 'Sydney', 'Perth']),
                            QuestionsAndAnswers('What is the capital city of Austria 🇦🇹?',
                                                'Vienna',
                                                ['Moscow', 'Sydney', 'Brussels']),
                            QuestionsAndAnswers('What is the capital city of Belgium 🇧🇪?',
                                                'Brussels',
                                                ['Dublin', 'Antwerp', 'Hamburg']),
                            QuestionsAndAnswers('What is the capital city of Canada 🇨🇦?',
                                                'Ottawa',
                                                ['Toronto', 'Calgary', 'Winnipeg']),
                            QuestionsAndAnswers('What is the capital city of Chile 🇨🇱?',
                                                'Santiago',
                                                ['Perth', 'Cali', 'Asuncion']),
                            QuestionsAndAnswers('What is the capital city of Czech Republic 🇨🇿?',
                                                'Prague',
                                                ['Calgary', 'Brno', 'Bratislava']),
                            QuestionsAndAnswers('What is the capital city of Denmark 🇩🇰?',
                                                'Copenhagen',
                                                ['Oslo', 'Fredericia', 'Cali']),]


correct_answers_count = 0
random.shuffle(question_and_answer_list)

for qa in question_and_answer_list:
    print(f'{qa.question}\n')
    print(f'Possible answers are:\n')
    possible = qa.other_answers + [qa.correct_answer]
    random.shuffle(possible)
    count = 0

    while count < len(possible):
        print(str(count + 1) + ': ' + possible[count])
        count += 1
    print('')

    print('Please enter the correct answer:')
    user_input = input()

    while not user_input.isdigit():
        print('Please enter the number of your answer:')
        user_input = input()

    user_answer = int(user_input)

    while not (0 < user_answer <= len(possible)):
        print("The number doesn't correspond to any number. Please choose a valid number:")
        user_answer = input()

    if possible[user_answer - 1] == qa.correct_answer:
        print('Your answer was correct')
        correct_answers_count += 1
    else:
        print('Your answer was incorrect')
        print('The correct answer was: ' + qa.correct_answer)

    print('-' * 50)
    time.sleep(2)

print(f'💭You answered {correct_answers_count} of {len(question_and_answer_list)} questions')

