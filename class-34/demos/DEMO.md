# Demo: Deployment Walk Through

Rather than starting from scratch every time let's take advantage of an awesome Github feature - Repository Templates

It so happens that CodeFellows has such a template available. Let's try it out and see if we can save some time.

## Django Project

- Visit [API Quick Start](https://github.com/codefellows/python-401-api-quickstart)
- Show process of `Use this Template`
  - Encourage students to create their own template repository to their liking
- Create a new repo based off `API Quick Start` template
- Rename to `snacks-api`
- inspect `pyproject.toml`
  - Notice the new (or more recent) libraries
    - django-cors-headers
    - django-environ
    - whitenoise
    - etc.
  - The cors-headers aren't needed quite yet, but will be as soon as you have deployed sites that are consuming data from the deployed API.
- > poetry install
  - If you have get errors installing on Mac
    - > `export SYSTEM_VERSION_COMPAT=1`
    - > poetry install

## Update .env

- Make copy of `project/.sample.env`
- Name it `.env` in same folder
  - Inspect the `.env` a bit
  - Update with values you want
  - Here's a handy way to generate a secret key
    - > python -c "import secrets; print(secrets.token_urlsafe())"

## Tweak the Starter

- The API Quick Start has a resource of `Thing`
- Lab will be having a `CookieStand` resource
- For the demo we'll use a `Snack` resource instead
- Refer to README.md in root folder for tips on customizing API.
- Walk through adjusting names in project and app folder to fit the current api.
  - Point out that the new Model will certainly have different attributes than the sample Thing model.
  - When they update the Model make sure other code (e.g. in Serializer) is updated as well.
- Encourage students to NOT cut and paste, but to take the extra couple of minutes to confirm changes as you go.
  - One exception is `api_tester` which you can either ignore for now, or do file level replacement.

## Test Run

- The default for API Quick Start is to use SQLite so we can go ahead and give a test run.
- Make sure you performed migration steps after the customizations.
- run dev server
- Navigate to `http://127.0.0.1:8000/api/v1/snacks/`
- You could go deeper now and create a super user etc. if you like.

## Remote Database Time

- Set up an account and [ElephantSQL](https://www.elephantsql.com/)
  - **NOTE:** No credit card required for free tier.
- Create Database with name `snacks-api-db` on the free plan.
- Select any available region you like.
- Click on the new DB to get details.
- Update `.env` file with relevant details.
  - `User & Default database` is for both `DATABASE_NAME` and `DATABASE_USER`
  - `Server` is for `DATABASE_HOST`
    - Just the domain, not the extra text in parentheses.
- `DATABASE_PORT` is most likely 5432, confirm this in `URL` section
- Activate virtual environment
- `python manage.py migrate`
- `python manage.py createsuperuser`
- `gunicorn snacks_project.wsgi`
- Check `http://localhost:8000/api/v1/snacks/` in browser.
- ctrl+c to shut down server.
- exit virtual environment
- Boom - remote Database
- Time allowing, go back to ElephantSQL and show the ability to run queries on the database.
  - E.g. `select * from snacks_snack`

## Deploy Project - Heroku Time

- install [heroku cli](https://devcenter.heroku.com/articles/heroku-cli)
- `heroku apps:create snacks-api`
- Check remote with `git remote -v`
- If heroku remote doesn't show then `heroku git:remote -a snacks-api`
- Create `heroku.yml` in root folder.
- Add below text to `heroku.yml`

```yaml
build:
  docker:
    web: Dockerfile
release:
  image: web
run:
  web: gunicorn project.wsgi
```

- **IMPORTANT STEP : DO NOT SKIP THIS**
- `heroku stack:set container`
- Add/Commit
- `git push heroku main`
- Go to [heroku](https://www.heroku.com/)
- Login takes you to dashboard
- Select your app
- Go to settings
- Click `reveal config vars` button
- Add config vars to match `.env` file
- `ALLOWED_HOSTS` should match the heroku URL for your app.
  - Click `Open app` button to see it
  - Leave out the `https://` and trailing slash.
  - E.g. snacks-api.herokuapp.com
- It can take a minute for the environment variable changes to take effect
  - > heroku logs --tail will show you progress in terminal
- Once site is ready then see if you can log in, create snacks, etc.
- Bittersweet success!
  - It will be ugly because the styling was lost.
  - This is due to the Heroku file system's "ephemeral" nature
  - One way to handle issue is to run `collectstatic` locally then ACP to heroku.
- We can also use API Tester to see if API working.
- Edit `api_tester.py` to use the new api's url.
- Update the user and password as needed
- > python manage.py api_tester.py create_snack --name=victory
- > python manage.py api_tester.py get_snacks

## Static Assets

- Handle collecting static files so that styling doesn't go away with DEBUG off
- Easiest way is to run collect static locally and commit the `staticfiles` folder
  - There is some trickiness here, especially on Heroku. Often static assets would be on CDN so it's not an issue.
