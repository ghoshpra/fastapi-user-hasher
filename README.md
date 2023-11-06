# fastapi-user-hasher
1. Need to containerize the application
2. Build a container(docker) image and run the container to test the app locally
3. Push to to some repo
4. Create a namespace either by running kubectl command or by creating a manifest file 
5. Create a deployment manifest file and for zero deployment time we should have deployment stratedy as rollling deployment(default)
6. create a secret and mount the secret as ENV variable.
7. Apply the deployment.yaml to apply the change for secret
8. Test with specific user-salt and verify the output
9. Read the aioprometheus documentation and implement the change to capture metrics
