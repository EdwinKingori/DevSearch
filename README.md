# DevSearch Collaboration Platform.

## Introduction
Developing a collaboration platform for software developers to find collaborators for open-source or freelance projects, enabling networking and teamwork on various development tasks. The platform includes a built-in messaging system that allows for direct communication through an inbox feature.

![image](https://github.com/user-attachments/assets/c94dad3b-3e2e-477f-958a-f0b5181d0de4)

![image](https://github.com/user-attachments/assets/103661ee-30ca-44e6-8ffe-8b0269b448c0)

![image](https://github.com/user-attachments/assets/69e9afef-0f82-49d0-b1a8-340088a62989)



![image](https://github.com/user-attachments/assets/cc0cafc6-5849-46d2-9ebc-29ab171ce77e)


The objective of this project is to provide a dedicated niche for developers to connect with like-minded individuals, form teams, and collaborate on diverse development tasks.

## Features

User Profiles: Developers can create detailed profiles describing and showcasing their skills, experience, and interests.

Project Listings: Users can post open-source or freelance projects, detailing the requirements, goals and request collobartion.

Search Functionality: Search for developers or projects based on skills (tags), name, and other criteria.

Direct Messaging: Built-in inbox for seamless communication between users.

Team Management: Collaborators can form and manage teams for projects.

# Tools Used

Backend: Django (Python) main framework used for development.

Django Rest Framework: utilizing RESTFUL APIs to make requests and allow for seamless integrations with various clients such as web. The project also allows flexibility for opensource integrations such as integrating with mobile clients.  

Frontend: HTML, CSS, JavaScript

Database: SQLite (for development), MySQL (for production)

Authentication: Django’s built-in authentication system with additional features for user profiles. Utilizing permissions DjangoRestFrameworks's restapi authentication such as IsAuthenticated. 

API Testing Tool: utilizing Postman for testing and documenting the project's API endpoints

# Installation procedure

#### Prerequisites

Python 3.x
pip
Virtual environment (optional but recommended)

# Steps to Fork or Clone: 

  1. clone the respository
     
    git cone https://github.com/EdwinKingori/DevSearch.git
    cd devsearch
     
  2. Create and activate a virtual environment:
     
    python3 -m venv venv
    source venv/bin/activate
    
  3. Install dependencies:

    pip install -r requirements.txt

  4. Apply database migrations:

    python3 manage.py migrate

  5. Create super user to access the admin panel

    python3 manage.py createsuperuser
    
  6. Run the development server:

    python3 manage.py runserver

## Contributions

Contributions are welcome! To contribute:

Fork the repository.

Create a new branch:

    git checkout -b feature/your-feature-name

Commit your changes:

    git commit -m "Add your feature description"

Push to the branch:

    git push origin feature/your-feature-name

Open a pull request.

### Contact

  For any questions, critics, suggestions, or feedback, please contact:

Email: eddmunyiri@gmail.com

GitHub: https://github.com/EdwinKingori/

### HAVE FUN!
