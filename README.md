# Login-Authenticator
This project is based on creating an application that handles the login and signing up functions of a certain service that requires the user to create an account for using its services. The designed application's main page has the option to **sign up, sign in, delete the account or exit** the portal.  

The user can choose to create a new account on the portal where he needs to enter a desired username, a password, answer a **security question** and verify that they're not a bot by answering the captcha correctly. The user can use the security answer entered while signing up to reset their password later in case they forget it.

We have used the **Caesar Cipher** technique for encrypting the password before saving it to the server to have better security.
The **CAPTCHA technology** has been used, which authenticates that a real person is accessing the application and blocks automated systems. These automated systems fail to read the distorted characters in the graphic that the user has to read and enter to validate.

## Technologies used:
- MySQL
- Captcha Generator
- Tkinter

# Screenshots Of The Application


## The main page.
<img src="https://user-images.githubusercontent.com/71747053/146645345-ccf21fb8-3299-4684-a80b-ac82a5c56b7c.png" alt="Main Page image" width="600"/>


## The signing up page.
<img src="https://user-images.githubusercontent.com/71747053/146645427-eff8c3bf-97bc-4498-a911-790a967a9328.png" alt="Signup Page image" width="600"/>


In case the email entered already exists on the server, then, the following message box pops up:

<img src="https://user-images.githubusercontent.com/71747053/146645643-b989412b-1bac-4cd9-ae06-64b3cc59d996.png" alt="Email already exists image" width="600" height="200"/>


In case the user fails to fill one field and clicks on submit, the following message box pops up:

<img src="https://user-images.githubusercontent.com/71747053/146645575-95fb810d-17c0-44a0-bb7e-f097a509c4d6.png" alt="Empty Field image" width="300" height="200"/>


In case the captcha fails to match, the following message box pops up:

<img src="https://user-images.githubusercontent.com/71747053/146645584-4e08ff62-a13a-4220-9a2e-c78040ba3c1e.png" alt="Incorrect Captcha image" width="300" height="200"/>


In case the password entered in the 'desired password' field and the confirmation password field do not match, the message that the user receives is:

<img src="https://user-images.githubusercontent.com/71747053/146645597-05e3851e-428b-43dc-85f4-903a4e0bedff.png" alt="Passwords do not match image" width="300" height="200"/>


In case all the entered information meets the requirements, the message that the user receives is:

<img src="https://user-images.githubusercontent.com/71747053/146645649-e6be60df-fb4c-4b85-879f-fcfdd86f9bb6.png" alt="Account created successfully image" width="300" height="200"/>





## The login page.
<img src="https://user-images.githubusercontent.com/71747053/146645672-ce2cf160-c104-4565-b3a4-8a9eaac4fe73.png" alt="Login page image" width="600"/>


In case the user fails to fill one field and clicks on submit, the following message box pops up:

<img src="https://user-images.githubusercontent.com/71747053/146645575-95fb810d-17c0-44a0-bb7e-f097a509c4d6.png" alt="Empty field image" width="300" height="200"/>


In case the user fails to enter the password correctly, the login becomes unsuccessful:

<img src="https://user-images.githubusercontent.com/71747053/146645714-ea3b0317-76a7-4a5e-a051-2f225c1de30e.png" alt="Incorrect password image" width="300" height="200"/>


If the user succeeds to enter all the details correctly, the login is successful:

<img src="https://user-images.githubusercontent.com/71747053/146645699-eb7ce8d8-0898-406a-9dcd-02a7d18c24df.png" alt="Login successfull image" width="600" height="200"/>




## The forgot password page.

<img src="https://user-images.githubusercontent.com/71747053/146645732-d8f97788-a14a-4baa-92ae-1896b3ac5578.png" alt="Forgot password page" width="600" />


Let's say that the user fails to enter the right security answer, then they will not be able to change their password and the message box that pops on validating the security answer will be the following:

<img src="https://user-images.githubusercontent.com/71747053/146647033-0854138a-c761-4d88-ae82-24712e1742c5.png" alt="Incorrect security answer image" width="600" height="200"/>



Let's say that the user enters the right security answer, Then the following message pops up:

<img src="https://user-images.githubusercontent.com/71747053/146645805-eceff4bd-db8e-4c7c-bbcd-5ea2621fb3cd.png" alt="Correct security answer image" width="600" height="200"/>


In case the user fails to fill one field and clicks on submit, the following message box pops up:

<img src="https://user-images.githubusercontent.com/71747053/146645575-95fb810d-17c0-44a0-bb7e-f097a509c4d6.png" alt="Empty field image" width="300" height="200"/>


In case the password entered in the 'desired password' field and the confirmation password field do not match, the message that the user receives is:

<img src="https://user-images.githubusercontent.com/71747053/146645597-05e3851e-428b-43dc-85f4-903a4e0bedff.png" alt="Passwords do not match image" width="300" height="200"/>


In case the captcha fails to match, the following message box pops up:

<img src="https://user-images.githubusercontent.com/71747053/146645584-4e08ff62-a13a-4220-9a2e-c78040ba3c1e.png" alt="Incorrect captcha image" width="300" height="200"/>



When the user enters all the required details correctly and clicks submit, the following message pops up:

<img src="https://user-images.githubusercontent.com/71747053/146645821-7b8b1e57-7b74-4ff9-9491-9227e48945b1.png" alt="Password updated image" width="300" height="200"/>






## The delete account page. 

<img src="https://user-images.githubusercontent.com/71747053/146645843-af31c819-a8b8-489a-9860-7b02ef715f3e.png" alt="Delete account page image" width="600" />


In case the user fails to fill one field and clicks on submit, the following message box pops up:

<img src="https://user-images.githubusercontent.com/71747053/146645575-95fb810d-17c0-44a0-bb7e-f097a509c4d6.png" alt="Empty field image" width="300" height="200"/>


In case the captcha fails to match, the following message box pops up:

<img src="https://user-images.githubusercontent.com/71747053/146645584-4e08ff62-a13a-4220-9a2e-c78040ba3c1e.png" alt="Incorrect captcha image" width="300" height="200"/>


In case the user gives an incorrect prompt in place of 'CONFIRM', the user will not be able to delete their account and the following message pops up: 

<img src="https://user-images.githubusercontent.com/71747053/146645877-157183f3-2e49-4b68-9da6-fdf721493efd.png" alt="Incorrect promt image" width="300" height="200"/>


If everything entered matches the details on the server, and the user clicks on submit, the account gets deleted successfully.

<img src="https://user-images.githubusercontent.com/71747053/146645888-36f7e870-6f81-4ae1-bedf-f052e3758239.png" alt="Accounted deleted successfully image" width="600" height="200"/>


