# Week 6 - FNB App Academy
--------------------------

## Contact Book

## Section 1: Introduction and Setup

1. **Lesson 1: Intro to the App**
    This week, we begin developing a Contact Book app to store, edit, and manage user contact information using HTML, CSS, JavaScript, and an external API.

2. **Lesson 2: Intro To The API**
    Learn how APIs work and how the Contact Book app communicates with a remote server to manage contact data.

3. **Lesson 3: Setting Up**
    Create the necessary project structure, including HTML, CSS, and JavaScript files, to start building the app.

4. **Lesson 4: The API Key**
    Understand how to set up API authentication.

## Section 2: Viewing Contacts

1. **Lesson 5: Getting the Contact**
    Use the fetch() function to retrieve contact data from the API and handle JSON responses.

2. **Lesson 6: Displaying the Contact**
    Display the fetched contacts dynamically using JavaScript to build a responsive contact table.

3. **Lesson 7: Iterating through a JSON Array**
    Loop through the array of contact objects and generate rows for each contact using for loops and template literals.

4. **Lesson 8: Refresh Button**
    Add a "Refresh" button to manually re-fetch and reload contacts from the API.

## Section 3: Adding New Contacts

1. **Lesson 9: Add Contact Form**
    Create a form with fields for first name, last name, mobile number, email, and an avatar image.

2. **Lesson 10: Creating the FormData Object**
    Use the FormData API to collect form values and prepare them for sending via POST request.

3. **Lesson 11: Submitting the FormData Object**
    Submit the new contact information to the API using fetch() and display the response message.

4. **Lesson 12: Adding the HomeLink Function**
    Add navigation functionality with a "Home" button to return to the main contact list page.

## Section 4: Editing Contacts

1. **Lesson 13: Edit Contact Page Intro**
    Create a new page for editing existing contact information.

2. **Lesson 14: Building the Edit Contact Page**
    Set up the HTML form and page layout to load and update specific contact details.

3. **Lesson 15: Linking to the Edit Contact Page**
    Enable clicking on a contact row to open the edit page using the contact's unique ID.

4. **Lesson 16: Edit Contact Form**
    Pre-fill the form with the existing data and allow users to change the values.

5. **Lesson 17: Getting the ID of the Contacts**
    Extract the contact’s ID from the URL using string methods and pass it to the API call.Extract the contact’s ID from the URL using string methods and pass it to the API call.

6. **Lesson 18: Fetching the Contacts from the DB**
    Use the contact ID to retrieve specific data from the API and display it in the edit form.

7. **Lesson 19: Displaying the Contact Info**
    Populate the avatar and input fields with the contact’s current information.

8. **Lesson 20: Making the Contact Fields Editable**
    Allow form fields to become editable when the "Edit" button is clicked.

## Section 5: Updating and Deleting Contacts

1. **Lesson 21: Submitting the Form – Preparing the FormData Object**
    Rebuild the FormData object with the updated information and the contact ID.

2. **Lesson 22: Submitting the Form – Calling Fetch**
    Send the updated contact data to the server using a POST request to the edit endpoint.

3. **Lesson 23: Deleting a Contact**
    Add a "Delete" button with confirmation logic to remove a contact from the database via API.