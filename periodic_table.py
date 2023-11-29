#import tkinter for GUI
import tkinter as tk
from tkinter import messagebox
import random

#create a dictionary of almost all elements in the periodic table and their corresponding symbols
#exclude lanthanoids and actinoids

elements = {
    'Hydrogen': 'H',
    'Helium': 'He',
    'Lithium': 'Li',
    'Beryllium': 'Be',
    'Boron': 'B',
    'Carbon': 'C',
    'Nitrogen': 'N',
    'Oxygen': 'O',
    'Fluorine': 'F',
    'Neon': 'Ne',
    'Sodium': 'Na',
    'Magnesium': 'Mg',
    'Aluminum': 'Al',
    'Silicon': 'Si',
    'Phosphorus': 'P',
    'Sulfur': 'S',
    'Chlorine': 'Cl',
    'Argon': 'Ar',
    'Potassium': 'K',
    'Calcium': 'Ca',
    'Scandium': 'Sc',
    'Titanium': 'Ti',
    'Vanadium': 'V',
    'Chromium': 'Cr',
    'Manganese': 'Mn',
    'Iron': 'Fe',
    'Cobalt': 'Co',
    'Nickel': 'Ni',
    'Copper': 'Cu',
    'Zinc': 'Zn',
    'Gallium': 'Ga',
    'Germanium': 'Ge',
    'Arsenic': 'As',
    'Selenium': 'Se',
    'Bromine': 'Br',
    'Krypton': 'Kr',
    'Rubidium': 'Rb',
    'Strontium': 'Sr',
    'Yttrium': 'Y',
    'Zirconium': 'Zr',
    'Niobium': 'Nb',
    'Molybdenum': 'Mo',
    'Technetium': 'Tc',
    'Ruthenium': 'Ru',
    'Rhodium': 'Rh',
    'Palladium': 'Pd',
    'Silver': 'Ag',
    'Cadmium': 'Cd',
    'Indium': 'In',
    'Tin': 'Sn',
    'Antimony': 'Sb',
    'Tellurium': 'Te',
    'Iodine': 'I',
    'Xenon': 'Xe',
    'Cesium': 'Cs',
    'Barium': 'Ba',
}

class PeriodicTableQuiz:
    def __init__(self, parent): 
        #parent: parent window of Tkinter
        self.parent = parent
        self.parent.title("Periodic Table Quiz")

        #start numbers 
        self.score = 0
        self.question_number = 0

        #set up a label in Tkinter application window
        self.label_question = tk.Label(parent, text="Please, enter the number of questions you would like to receive (1-20).")
        self.label_question.pack(pady=10)

        #create input field where user can enter the number of desired questions
        #connect it to a tkinter variable 

        self.var_num_questions = tk.StringVar() #Tkinter variable
        self.entry_num_questions = tk.Entry(parent, textvariable=self.var_num_questions)
        self.entry_num_questions.pack(pady=10)

        #create a button for user to start the quiz
        self.button_start_quiz = tk.Button(parent, text="Start the Periodic Table Quiz", command=self.start_quiz)
        self.button_start_quiz.pack(pady=10)


    #initiation of the quiz when user clicks "Start" button
    def start_quiz(self):
        #retrieve user-inputted number and converts it to an integer
        #check if a number between 1-20 is entered to start quiz
        #if entered number is valid, generate a list of questions
        try: 
            num_questions = int(self.var_num_questions.get())
            if 1 <= num_questions <= 20:
                self.questions = self.generate_questions(num_questions)

                #destroy the widgets related to question input
                self.label_question.destroy()
                self.entry_num_questions.destroy()
                self.button_start_quiz.destroy()

                #create label for quiz question
                self.label_question = tk.Label(self.parent, text="")
                self.label_question.pack(pady=10)

                #create widget for user's answer
                self.var_user_answer = tk.StringVar()
                self.entry_user_answer = tk.Entry(self.parent, textvariable=self.var_user_answer)
                self.entry_user_answer.pack(pady=10)

                #create button for submitting answer
                self.button_submit = tk.Button(self.parent, text="Subit", command=self.check_answer)
                self.button_submit.pack(pady=10)

                #start quiz by updating first question
                self.update_question()

            else: #error messages 
                messagebox.showerror("Error", "Please enter a number between 1 and 20.")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a valid number.")

    #generate the quiz questions
    def generate_questions(self, num_questions):
        #convert dictionary into a list of tuples
        elements_list = list(elements.items())
        #shuffle elements randomly, so each quiz has a randomized order of questions
        random.shuffle(elements_list)
        #create a sublist of questions after shuffling and return the sublist
        questions = elements_list[:num_questions]
        return questions

    #update of the quiz interface 
    def update_question(self):
        #check if questions are left in the quiz, then proceeding to set up next questions
        if self.question_number < len(self.questions):
            #unpack current tuple to get the name of element
            element, _ = self.questions[self.question_number]
            #update widget with questions
            self.label_question.config(text=f"What is the chemical symbol for {element}?")
            #clear content of widget, so user get an empty field for each questions
            self.var_user_answer.set("")
        else: #display final score, if there are no more questions
            self.show_score()

    def check_answer(self):
        #retrieve the user's answer from widget
        user_answer = self.var_user_answer.get().strip().upper()
        question, correct_answer = self.questions[self.question_number]

        #check for correct answer and display message, if answer is wrong
        if user_answer == correct_answer.upper():
            self.score += 1
        else:
            messagebox.showinfo("Incorrect", f"Wrong answer! The correct answer is {correct_answer}.")

        self.question_number += 1
        self.update_question()

    #display final score after finishing quiz
    def show_score(self):
        score_message = f"You scored {self.score} out of {len(self.questions)}."
        messagebox.showinfo("Quiz complete", score_message)
        self.parent.destroy()

#create a Tkinter window
#create an instance of the PeriodicTableQuiz class
#start event loop to handle user interaction and update the GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = PeriodicTableQuiz(root)
    root.mainloop()