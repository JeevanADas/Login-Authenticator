# Login-Authenticator
This project is based on creating an application that handles the login and signing up functions of a certain service that requires the user to create an account for using its services. The designed application's main page has the option to **sign up, sign in, delete the account or exit** the portal.  

The user can choose to create a new account on the portal where he needs to enter a desired username, a password, answer a **security question** and verify that they're not a bot by answering the captcha correctly. The user can use the security answer entered while signing up to reset their password later in case they forget it.

We have used the **Caesar Cipher** technique for encrypting the password before saving it to the server to have better security.
The **CAPTCHA technology** has been used, which authenticates that a real person is accessing the application and blocks automated systems. These automated systems fail to read the distorted characters in the graphic that the user has to read and enter to validate.

## Technologies used:
- MySQL
- Captcha Generator
- Tkinter
