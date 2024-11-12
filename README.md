Jenkins Pipeline to Clone GitHub Repository Using Personal Access Token and deploy the project on server.

This Jenkins pipeline demonstrates on how to deploy a project on the live server with just one click. The user just needs to push the code from local to github and then a webhook will get triggered which will take the push event from github to jenkins. Jenkins will trigger the pipeline which contains the steps on how to deploy the project on the live server.

**Prerequisites**

**Jenkins Server**: Ensure Jenkins is installed and configured.

**Project Server**: Server on which project needs to be deployed. (It could be same as jenkins server or any other server).

**GitHub Personal Access Token**: Generate a PAT with appropriate repository access permissions on GitHub and store it in Jenkins credentials under an identifier, such as github_token.

**Jenkins Git Plugin**: Verify that the Git plugin is installed on Jenkins to support Git operations.

**GitHub Repository:** Have the repository URL ready for cloning.

**Repository Access**: The PAT should have at least repo scope permissions on GitHub to allow cloning.
