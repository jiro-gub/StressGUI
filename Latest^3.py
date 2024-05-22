import tkinter as tk
from tkinter import filedialog

def definition_app(title, definition, color):
    app = tk.Toplevel()
    app.title(f"{title} Definition")
    app.configure(bg=color)
    label = tk.Label(app, text=f"{title}:", bg=color)
    label.pack(pady=10)
    definition_label = tk.Label(app, text="", bg=color)
    definition_label.pack()

    text = tk.Text(app, height=10, width=40)
    text.insert(tk.END, definition)
    text.config(bg=color)
    text.pack(pady=10)

def button1_action(sub_button):
    if sub_button == "Stress is a Natural Response":
        definition_app("Stress is a Natural Response", "Stress is the body's natural reaction to any change that requires an adjustment or response.It's a survival mechanism that prepares the body to face a challenge or flee from a threat.", "grey")
    elif sub_button == "Types of Stress":
        definition_app("Types of Stress", "There are two main types: acute stress, short-term and triggered by specific events, and chronic stress, which persists over time due to ongoing issues.", "grey")
    elif sub_button == "Effects on the Body":
        definition_app("Effects on the Body", "Stress triggers physiological responses, releasing hormones like cortisol and adrenaline, impacting systems like the immune, cardiovascular, and digestive systems.", "grey")
    elif sub_button == "Motivation":
        definition_app("Motivation", "Moderate levels of stress can serve as a motivational force, helping individuals focus their energy and attention to overcome challenges and achieve goals.", "grey")
    elif sub_button == "Resilience":
        definition_app("Resilience", "Facing and successfully managing stressful situations can build resilience, enhancing an individual's ability to cope with future stressors and adversity.", "grey")
    elif sub_button == "Sources of Stress":
        definition_app("Sources of Stress", "Stress can stem from various sources, including work, relationships, financial concerns, major life changes, and societal pressures.", "grey")
    elif sub_button == "Prevalence":
        definition_app("Prevalence", " Stress is a common experience worldwide, with surveys indicating that a significant portion of the population experiences stress regularly. However, its severity and impact can vary greatly among individuals.", "grey")
    elif sub_button == "Health Risks":
        definition_app("Health Risks", " Chronic stress is linked to various health risks, including cardiovascular diseases, weakened immune system, digestive issues, and even premature aging.", "grey")
    elif sub_button == "Stress Management":
        definition_app("Stress Management", "There are numerous techniques to manage stress, including exercise, relaxation techniques (like meditation or deep breathing), maintaining a healthy lifestyle, seeking social support, and time management.", "grey")
    elif sub_button == "Prevalence":
        definition_app("Prevalence", "Stress is a common experience worldwide, with surveys indicating that a significant portion of the population experiences stress regularly. However, its severity and impact can vary greatly among individuals.", "grey")
    elif sub_button == "Sleep Disturbances":
        definition_app("Sleep Disturbances", "Stress can disrupt sleep patterns, leading to difficulties falling asleep, staying asleep, or experiencing restful sleep. Chronic stress can contribute to insomnia and other sleep disorders.", "grey")
    elif sub_button == "Long-Term Consequences":
        definition_app("Long-Term Consequences", "Prolonged exposure to stress without effective coping mechanisms can have serious long-term consequences, including increased risk of chronic diseases, mental health disorders, and overall decreased quality of life. Prioritizing stress management is crucial for maintaining overall well-being.", "grey")
    elif sub_button == "Hormonal Response":
        definition_app("Hormonal Response", "When stressed, the body releases hormones such as cortisol and adrenaline, which prepare the body for action. These hormones can have wide-ranging effects on various bodily systems.", "grey")
    elif sub_button == "Gender Differences":
        definition_app("Gender Differences", "Research suggests that men and women may experience and respond to stress differently. For example, women may be more likely to seek social support when stressed, while men may be more prone to engaging in solitary activities.", "grey")
    elif sub_button == "Cultural Influences":
        definition_app("Cultural Influences", "Cultural factors play a significant role in shaping how individuals perceive and cope with stress. Different cultures may have varying attitudes towards stress, as well as unique coping strategies and social support networks. Understanding cultural perspectives is crucial for providing effective stress management interventions.", "grey")
    elif sub_button == "Stress in Students":
        definition_app("Stress in Students", "Students often face high levels of stress due to academic pressures, exams, peer relationships, and future career concerns. Learning effective stress management techniques is crucial for academic success and overall well-being.", "grey")
    elif sub_button == "Academic Pressure":
        definition_app("Academic Pressure", "Students often experience stress due to academic expectations, including the pressure to excel in exams, maintain high grades, and meet deadlines for assignments and projects.", "grey")
    elif sub_button == "Social Isolation":
        definition_app("Social Isolation", "Feelings of loneliness and social isolation can contribute to heightened stress levels. Lack of social connection and support networks may exacerbate feelings of anxiety and depression.", "grey")
    elif sub_button == "Stress Relief":
        definition_app("Stress Relief", "Alone time provides a break from the demands and pressures of social interactions, offering a chance to unwind and relax. This respite from external stimuli can alleviate stress levels and promote a sense of calm.", "grey")
    elif sub_button == "Emotional Regulation":
        definition_app("Emotional Regulation", " Being alone allows individuals to process their emotions without external influence. Through self-reflection and introspection, they can better understand and manage their feelings, leading to improved emotional well-being and reduced stress.", "grey")

def button2_action(sub_button):
    if sub_button == "Physical Symptoms":
        definition_app("Physical Symptoms", "Practice relaxation techniques such as deep breathing, meditation, or progressive muscle relaxation.", "grey")
    elif sub_button == "Fatigue or Insomnia":
        definition_app("Fatigue or Insomnia", "Establish a consistent sleep routine, limit caffeine and screen time before bed, and try relaxation exercises.", "grey")
    elif sub_button == "Changes in Appetite":
        definition_app("Changes in Appetite", "Focus on maintaining a balanced diet, eat regular meals, and avoid emotional eating by finding alternative coping strategies like exercise or hobbies.", "grey")
    elif sub_button == "Irritability or Moodiness":
        definition_app("Irritability or Moodiness", "Practice mindfulness and self-awareness to recognize triggers, engage in regular physical activity to release tension, and seek social support from friends or a therapist.", "grey")
    elif sub_button == "Difficulty Concentrating":
        definition_app("Difficulty Concentrating", "Break tasks into smaller, manageable steps, prioritize tasks, use tools like to-do lists or planners, and consider mindfulness or cognitive-behavioral techniques to improve focus.", "grey")
    elif sub_button == "Increased Heart Rate or Chest Pain":
        definition_app("Increased Heart Rate or Chest Pain", "Practice relaxation techniques like deep breathing or visualization, engage in regular physical activity to improve cardiovascular health, and consult a healthcare professional if symptoms persist.", "grey")
    elif sub_button == "Social Withdrawal":
        definition_app("Social Withdrawal", "Make an effort to maintain social connections, reach out to friends or family for support, join groups or clubs with shared interests, and consider seeking professional help if feelings of isolation persist.", "grey")
    elif sub_button == "Neglecting Responsibilities":
        definition_app("Neglecting Responsibilities", "Break tasks into smaller, manageable steps, prioritize responsibilities, delegate when possible, and seek assistance or guidance from colleagues, teachers, or family members.", "grey")
    elif sub_button == "Increased Use of Substances":
        definition_app("Increased Use of Substances", "Seek healthier coping strategies such as exercise, hobbies, or talking to a trusted friend or counselor, and consider seeking professional help if substance use becomes problematic.", "grey")
    elif sub_button == "Physical Symptoms Without Medical Cause":
        definition_app("Physical Symptoms Without Medical Cause", "Practice stress management techniques like deep breathing or meditation, consult a healthcare professional to rule out any underlying medical conditions, and consider therapy to address psychological factors contributing to physical symptoms.", "grey")
    elif sub_button == "Emotional Changes":
        definition_app("Emotional Changes", "Engage in activities that bring you joy and relaxation, such as hobbies, spending time with loved ones, or practicing mindfulness and gratitude.", "grey")
    elif sub_button == "Procrastination":
        definition_app("Procrastination", "Break tasks into smaller, manageable steps, set achievable goals, and reward yourself for completing tasks. Additionally, practice time management techniques such as the Pomodoro Technique or setting deadlines.", "grey")
    elif sub_button == "Cognitive Distortions":
        definition_app("Cognitive Distortions", "Challenge negative thoughts by examining evidence and considering alternative perspectives. Cognitive-behavioral therapy (CBT) techniques, such as thought restructuring or keeping a thought journal, can be helpful in identifying and reframing cognitive distortions.", "grey")
    elif sub_button == "Financial Worries":
        definition_app("Financial Worries", "Create a budget to track expenses and prioritize financial goals, seek financial counseling or advice from a professional, and explore strategies to increase income or reduce expenses. Additionally, practice stress management techniques to cope with financial stressors effectively.", "grey")
    elif sub_button == "Digestive Issues":
        definition_app("Digestive Issues", "Adopt healthy eating habits, such as consuming a balanced diet with plenty of fiber and hydration, practicing mindful eating, and avoiding triggers like caffeine or spicy foods. Stress-reduction techniques like deep breathing or progressive muscle relaxation can also help alleviate digestive symptoms.", "grey")
    elif sub_button == "Physical Tension":
        definition_app("Physical Tension", "Incorporate regular exercise into your routine to release physical tension, practice relaxation techniques such as yoga or tai chi, and consider massage therapy or acupuncture to alleviate muscle tension.", "grey")
    elif sub_button == "Increased Pessimism/Hopelessness":
        definition_app("Increased Pessimism/Hopelessness", " Practice gratitude by focusing on things you're thankful for, challenge negative thoughts with evidence-based reasoning, engage in activities that bring joy or purpose, and seek support from a therapist or counselor to work through feelings of hopelessness.", "grey")
    elif sub_button == "Ruminating Thoughts":
        definition_app("Ruminating Thoughts", "Practice mindfulness to bring awareness to the present moment, challenge repetitive thoughts by focusing on problem-solving or positive outcomes, engage in activities that distract and redirect your attention, and consider therapy to learn cognitive-behavioral techniques for managing rumination.", "grey")
    elif sub_button == "Decreased Motivation/Apathy":
        definition_app("Decreased Motivation/Apathy", "Break tasks into smaller, more manageable goals, set rewards for completing tasks, seek inspiration from others or try new activities to reignite passion and motivation, and consider seeking therapy to explore underlying issues contributing to apathy.", "grey")
    elif sub_button == "Forgetfulness/Disorganization":
        definition_app("Forgetfulness/Disorganization", "Use organizational tools such as planners, calendars, or apps to keep track of responsibilities, break tasks into smaller, manageable steps, and practice mindfulness to improve focus and concentration.", "grey")

def display_text(event=None):
    text = input_entry.get()
    output_text.insert(tk.END, text + "\n")
    input_entry.delete(0, tk.END)

def save_journal():
    text_to_save = output_text.get("1.0", tk.END)
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text_to_save)

def load_journal():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "r") as file:
            saved_text = file.read()
            output_text.insert(tk.END, saved_text)

def button3_action(sub_button):
    if sub_button == "Your Journal":
        journal_window = tk.Toplevel()
        journal_window.title("Your Journal")
        
        title_label = tk.Label(journal_window, text="Enter Text Below:")
        title_label.pack()
        
        global input_entry  # make input_entry global
        input_entry = tk.Entry(journal_window)
        input_entry.pack()
        input_entry.bind("<Return>", display_text)
        
        global output_text  # make output_text global
        output_text = tk.Text(journal_window, height=10, width=40)
        output_text.pack()
        
        save_button = tk.Button(journal_window, text="Save", command=save_journal)
        save_button.pack()
        
        load_button = tk.Button(journal_window, text="Load", command=load_journal)
        load_button.pack()

root = tk.Tk()
root.title("StressSensei")
root.config(bg="black")

label = tk.Label(root, text="**Stress Facts & Coping Mechanisms**", bg="grey", font=("Helvetica", 14))
label.pack(pady=50, padx=50)

button1 = tk.Menubutton(root, text="Facts & Info.", bg="white", width=0, height=2)
button1.pack(side="left", pady=50, padx=25)
button1.menu = tk.Menu(button1, tearoff=0)
button1["menu"] = button1.menu
button1.menu.add_command(label="Stress is a Natural Response", command=lambda: button1_action("Stress is a Natural Response"))
button1.menu.add_command(label="Types of Stress", command=lambda: button1_action("Types of Stress"))
button1.menu.add_command(label="Effects on the Body", command=lambda: button1_action("Effects on the Body"))
button1.menu.add_command(label="Motivation", command=lambda: button1_action("Motivation"))
button1.menu.add_command(label="Resilience", command=lambda: button1_action("Resilience"))
button1.menu.add_command(label="Sources of Stress", command=lambda: button1_action("Sources of Stress"))
button1.menu.add_command(label="Prevalence", command=lambda: button1_action("Prevalence"))
button1.menu.add_command(label="Health Risks", command=lambda: button1_action("Health Risks"))
button1.menu.add_command(label="Stress Management", command=lambda: button1_action("Stress Management"))
button1.menu.add_command(label="Prevalence", command=lambda: button1_action("Prevalence"))
button1.menu.add_command(label="Sleep Disturbances", command=lambda: button1_action("Sleep Disturbances"))
button1.menu.add_command(label="Long-Term Consequences", command=lambda: button1_action("Long-Term Consequences"))
button1.menu.add_command(label="Hormonal Response", command=lambda: button1_action("Hormonal Response"))
button1.menu.add_command(label="Gender Differences", command=lambda: button1_action("Gender Differences"))
button1.menu.add_command(label="Cultural Influences", command=lambda: button1_action("Cultural Influences"))
button1.menu.add_command(label="Stress in Students", command=lambda: button1_action("Stress in Students"))
button1.menu.add_command(label="Academic Pressure", command=lambda: button1_action("Academic Pressure"))
button1.menu.add_command(label="Social Isolation", command=lambda: button1_action("Social Isolation"))
button1.menu.add_command(label="Stress Relief", command=lambda: button1_action("Stress Relief"))
button1.menu.add_command(label="Emotional Regulation", command=lambda: button1_action("Emotional Regulation"))

button2 = tk.Menubutton(root, text="Coping Mechanisms", bg="white", width=0, height=2)
button2.pack(side="left", padx=25)
button2.menu = tk.Menu(button2, tearoff=0)
button2["menu"] = button2.menu
button2.menu.add_command(label="Physical Symptoms", command=lambda: button2_action("Physical Symptoms"))
button2.menu.add_command(label="Fatigue or Insomnia", command=lambda: button2_action("Fatigue or Insomnia"))
button2.menu.add_command(label="Changes in Appetite", command=lambda: button2_action("Changes in Appetite"))
button2.menu.add_command(label="Irritability or Moodiness", command=lambda: button2_action("Irritability or Moodiness"))
button2.menu.add_command(label="Difficulty Concentrating", command=lambda: button2_action("Difficulty Concentrating"))
button2.menu.add_command(label="Increased Heart Rate or Chest Pain", command=lambda: button2_action("Increased Heart Rate or Chest Pain"))
button2.menu.add_command(label="Social Withdrawal", command=lambda: button2_action("Social Withdrawal"))
button2.menu.add_command(label="Neglecting Responsibilities", command=lambda: button2_action("Neglecting Responsibilities"))
button2.menu.add_command(label="Increased Use of Substances", command=lambda: button2_action("Increased Use of Substances"))
button2.menu.add_command(label="Physical Symptoms Without Medical Cause", command=lambda: button2_action("Physical Symptoms Without Medical Cause"))
button2.menu.add_command(label="Emotional Changes", command=lambda: button2_action("Emotional Changes"))
button2.menu.add_command(label="Procrastination", command=lambda: button2_action("Procrastination"))
button2.menu.add_command(label="Cognitive Distortions", command=lambda: button2_action("Cognitive Distortions"))
button2.menu.add_command(label="Financial Worries", command=lambda: button2_action("Financial Worries"))
button2.menu.add_command(label="Digestive Issues", command=lambda: button2_action("Digestive Issues"))
button2.menu.add_command(label="Physical Tension", command=lambda: button2_action("Physical Tension"))
button2.menu.add_command(label="Increased Pessimism/Hopelessness", command=lambda: button2_action("Increased Pessimism/Hopelessness"))
button2.menu.add_command(label="Ruminating Thoughts", command=lambda: button2_action("Ruminating Thoughts"))
button2.menu.add_command(label="Decreased Motivation/Apathy", command=lambda: button2_action("Decreased Motivation/Apathy"))
button2.menu.add_command(label="Forgetfulness/Disorganization", command=lambda: button2_action("Forgetfulness/Disorganization"))

button3 = tk.Menubutton(root, text="Your Journal", bg="white", width=0, height=2)
button3.pack(side="left", padx=25)
button3.menu = tk.Menu(button3, tearoff=0)
button3["menu"] = button3.menu
button3.menu.add_command(label="Your Journal", command=lambda: button3_action("Your Journal"))

root.mainloop()
