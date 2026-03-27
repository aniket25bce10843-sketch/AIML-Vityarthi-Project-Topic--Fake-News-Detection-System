import tkinter as tk
from tkinter import messagebox
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
#Sample News
news = [
    "This is the coldest day of the month",
    "There are seven continents in the Earth",
    "The account has been credited with 10000 rupees",
    "Click to get free mobile phone",
    "Technology improves everyone and helps everybody",
    "The cost of the newspaper is doubled from now on",
    "You have to enter your pin after scanning the QR code to recieve money",
    "The fuel prices has been increased",
        ]
labels = ['Y','Y','N','N','Y','N','N','Y']  
#N= Fake, #Y= Real
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(news)
#Model Training
model = LogisticRegression()
model.fit(X, labels)
#Predicting the function
def detect_news():
    user_text = entry.get()

    if not user_text.strip():
        result_label.config(text="Enter the text of the news", fg="red")
        return

    text_vec = vectorizer.transform([user_text])
    prediction = model.predict(text_vec)[0]

    if prediction == 'N':
        result_label.config(text="News is Fake (Fake News)", fg="blue")
    else:
        result_label.config(text="News is Real (Real News)", fg="purple")
#Code For Making Graphical User Interface(GUI)
root = tk.Tk()
root.title("Fake News Detection System")
root.geometry("650x350")

tk.Label(root, text="Fake News Detection System",font=("Arial", 15)).pack(pady=15)
tk.Label(root, text="Enter The Text Of The News:").pack()

entry = tk.Entry(root, width=60)
entry.pack(pady=15)

tk.Button(root, text="Check the news", command=detect_news).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial"))
result_label.pack(pady=25)

root.mainloop()

