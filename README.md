
# Just-delivery


Delivery service in telegram bot using DRF and Redis


## Demo

An example of how categories and their contents are displayed to a user in a bot 

![Screenshot from 2024-05-27 10-05-00](https://github.com/k0drin/Just-delivery/assets/124861436/b9122253-32a3-4543-9429-6d01cc6c356a)

![Screenshot from 2024-05-27 10-15-39](https://github.com/k0drin/Just-delivery/assets/124861436/df0f808e-1fa5-469e-961f-ce884bf22a09)




## Deployment

Go to the folder where you want to copy the project and run the command:
```bash
  git clone https://github.com/k0drin/Just-delivery.git
```
Then go to the Just-delivery folder and run this command to install all the dependencies:
```bash
  pip install -r requirements.txt
```
If the dependencies are not installed, then the reason may be an incompatibility between the version of the libraries and your version of Pihon. If everything is successful, you can proceed to the next step and apply the database migration with the command:
```bash
  python manage.py migrate

```
Now you can create a super user using the command:
```bash
python manage.py createsuperuser

```

Now if all steps were completed successfully, you can start the local server with the command:
```bash
python manage.py runserver
```
## Roadmap

- Project file structure
  
![roadmap](https://github.com/k0drin/Just-delivery/assets/124861436/0f6f6786-e301-4dd6-9745-24b5b52b197a)
