# Gamma News - A News App in Django


https://github.com/subhro1530/blog_news_project/assets/113383437/1b4b9da3-0ca5-435b-9e3f-eb4b65259a3e




This Django web application allows users to view news articles and create/delete their own blogs. Additionally, the site administrator can perform CRUD operations on blogs using API calls.

## Features

1. **Authentication**
   - User login and logout functionality.
   - User registration with standard password validation.
   - Forgot password validation for resetting passwords.

2. **API Calls and Dashboard**
   - Fetch and display news image and title on the home page after logging in.
   - Redirect users to detailed articles when clicking on news clip images.
   - Users can create blogs with title, content, and automatic creation date.
   - Users can delete their own blogs from the dashboard.

3. **Serializers - Django REST Framework**
   - Site administrator can view existing blogs list in JSON format through API endpoint only.
   - Site administrator can perform CRUD operations on blogs through API endpoints only.

4. **Bootstrap Designing (Optional)**
   - Usage of font-awesome based delete icon in the dashboard.
   - Bootstrap form-controls for blogs creation form.

## Deployment

As a part of the final exercise of this assignment, you must deploy the web app preserving all functionalities and the databases involved. You may use the following free-of-cost deployment platforms:

1. GitHub Pages
2. Heroku
3. DigitalOcean
