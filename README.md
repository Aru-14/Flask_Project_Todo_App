# Flask_Project_Todo_App
### 🌟 Features  
- **Add Tasks**: Easily create new to-do items.  
- **View Tasks**: Display all tasks in an organized manner.  
- **Update Tasks**: Modify task details with a user-friendly interface.  
- **Delete Tasks**: Remove completed or unnecessary tasks effortlessly.(will work on your local host not on vercel)
- **Responsive Design**: Built using **Bootstrap** for a clean and modern UI.  

---

### ⚙️ Tech Stack  
- **Backend**: Flask (Python Web Framework)  
- **Frontend**: HTML, CSS, Bootstrap  
- **Database**: SQLAlchemy (ORM for managing tasks)  
- **Deployment**: Vercel

---


 ### 📂 Project Structure 
```
├── app.py # Main application file
├── templates/ # HTML templates for UI
│ ├── index.html # Homepage to display tasks
│ ├── base.html
| ├── update.html
├── static/ #For static CSS and JS
├── instance/
| ├── todo.db # Database models using SQLAlchemy
├── requirements.txt # Dependencies
├── vercel.json # to use vercel for deployment
└── README.md # Project documentation
```

### 🛠️ Installation & Setup  
1. Clone the repository:  
   ```bash
   git clone https://github.com/your-username/flask-todo-app.git
   cd flask-todo-app
   ```
Create a virtual environment and activate it:

   ```bash
  python -m venv venv  
  source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
Install the required dependencies:
   ```bash
  pip install -r requirements.txt
   ```
Run the Flask application:
   ```bash
python app.py
   ```
Open your browser and go to:
   ```
http://127.0.0.1:5000/
   ```
🤝 Contributing
Contributions are welcome! If you'd like to contribute:

Fork the repository.

- Create a feature branch: git checkout -b feature-name.
- Commit your changes: git commit -m 'Add some feature'.
- Push to the branch: git push origin feature-name.
- Open a pull request.

📜 License
This project is licensed under the MIT License. Feel free to use and modify it as needed.

🙌 Acknowledgments
Flask documentation: https://flask.palletsprojects.com/
Bootstrap for responsive design: https://getbootstrap.com/



Feel free to customize it with your name, screenshots, or additional details about your app! 
