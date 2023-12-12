# Portfolio Website 
This website is located at: www.grant-melvin.xyz

This project is used to display my resume publicly and demonstrate basic knowledge of the following technologies:
  -  Streamlit
  -  EC2 Instances
  -  Hosted Zones
  -  Github Runners

The EC2 instance contains a streamlit application that runs on port 8501. Web traffic is automatically mapped from port 80 using a reverse proxy with nginx. 

The application is in a continuous integration and deployment pipeline using GitHub runners. When I push a change onto the repository, it is pushed to Dockerhub and pulled onto the official website using the GitHub runners

This project gave me a very rudimentary understanding of how EC2 instances and CI/CD pipelines work which will allow me to migrate a lot of other work that I'd like to publish onto AWS in an effective manner.
