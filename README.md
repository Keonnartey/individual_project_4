# Auto Scaling Flask App Using Azure Container Apps [![CI](https://github.com/Keonnartey/individual_project_4/actions/workflows/ci.yml/badge.svg)](https://github.com/Keonnartey/individual_project_4/actions/workflows/ci.yml)

[Price Predictions](https://pricep.azurewebsites.net/)

#### Requirements

The objective of this project is to create a publicly accessible auto-scaling container leveraging Azure Web App Services and Flask. The aim is to deploy a highly scalable web-hosted application, providing a platform for individuals to enhance their understanding of Flask in a well-structured and expansive manner.

#### Flask Web Application:

The web application, defined in *app.py*, serves the purpose of predicting startup company prices within three distinct states: *Florida*, *New York*, and *California*. To facilitate this prediction, the states are treated as categorical variables. To obtain a price prediction for a specific state, users can input binary values (1 or 0) corresponding to the states of interest. By providing a '1' for the target state and '0' for others, the application generates precise price predictions tailored to the selected state, offering users a refined understanding of pricing trends based on geographic location.

<img width="1341" alt="Screenshot 2023-12-06 at 8 34 36 PM" src="https://github.com/Keonnartey/individual_project_4/assets/125210401/35b3a8dc-6613-47cf-a324-2b4afe59b72f">
<img width="1353" alt="Screenshot 2023-12-06 at 8 43 26 PM" src="https://github.com/Keonnartey/individual_project_4/assets/125210401/386e0a47-23c2-401d-9dbe-9b99a37a59e6">

HTML Templates: The project contains HTML templates (home.html and prediction.html) providing a user-friendly interface.

#### Docker Containerization:

*The Dockerfile* is provided to containerize the Flask app the process begins by specifying the desired Python version, installing dependencies, and incorporating necessary components to construct the Docker Image. This crafted image is then deployed to DockerHub, allowing seamless deployment after input and authorization.

#### Deployment to Azure Azure Container Apps:

Azure Configuration: Environment variables are utilized for sensitive information like API tokens. Azure-specific configurations are in place for secure deployment on Azure Container Apps.

#### Preparation 

1. Create a model Notebook and save into a pickle file which is then moved into the Flask app folder
2. Create an App.py and run the model   <img width="1440" alt="Screenshot 2023-12-07 at 11 25 33 AM" src="https://github.com/Keonnartey/individual_project_4/assets/125210401/49b0f737-9d38-47a1-ada9-965ffe0d9264">

3. Create a DockerFile (docker build -t <`insert image name`:tag> . )
4. Create and build a Docker image  <img width="1440" alt="Screenshot 2023-12-07 at 11 25 10 AM" src="https://github.com/Keonnartey/individual_project_4/assets/125210401/63389c84-c213-435f-84dd-03dea2fd2dcc">

6. Docker push the image to DockerHub and copy the image name with the tag
7. On Azure Web App Service, create a resource group, choose DockerFile    <img width="1440" alt="Screenshot 2023-12-07 at 11 28 01 AM" src="https://github.com/Keonnartey/individual_project_4/assets/125210401/3a4828b6-ef74-4be6-a86e-87d6b9ffe63a">

8. Add the Docker Image and the tag   <img width="1440" alt="Screenshot 2023-12-07 at 11 28 32 AM" src="https://github.com/Keonnartey/individual_project_4/assets/125210401/199a65e6-5892-4583-b7b2-7a0ab6a87e4e">

9. Deploy the web app  <img width="1440" alt="Screenshot 2023-12-07 at 11 26 57 AM" src="https://github.com/Keonnartey/individual_project_4/assets/125210401/ee6bc51c-3471-48d9-ad26-3b82b26ec37f">

10. Add the configuration Services  <img width="1440" alt="Screenshot 2023-12-07 at 11 25 47 AM" src="https://github.com/Keonnartey/individual_project_4/assets/125210401/ad96b743-9fa3-4828-8026-350a5d611d24">

11. Launch URL 


#### GitHub Action

After the building of our code we run the actions `format`, `lint` and `test` to ensure Continuous Integration and Continuous Development.

#### References

https://github.com/DerekLW6/Azure-Flask-App/blob/main/README.md
https://code.visualstudio.com/docs/containers/app-service
https://docs.docker.com/engine/reference/commandline/build/
https://learn.microsoft.com/en-us/azure/developer/python/tutorial-containerize-simple-web-app?tabs=web-app-flask
