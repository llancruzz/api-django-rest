# Profile Django Rest Framework APP
![Screenshot logo](./docs/logo.png)

## Setting up basic Django Project with Cloudinary

### Step 1: Create our Django Project and configure it to use Cloudinary:

1. Install Packages incl. Django, Cloudinary, Pillow.
2. Create Project.
3. Create env.py file and store Cloudinary url value.
4. In settings.py, add cloudinary to installed apps and create storage.

## Creating the Profile App

### Step 2: Create our Profile Model:

1. Create App, and add to INSTALLED_APPs list.
2. Create the app model e.g Profile.

### Step 3: Add a Signal to Profile Model:

1. Create signal and connect to function.
2. Register model in admin.py.
3. Run Migrations.
4. Create superuser.
5. Save dependencies in requirements.

#### What are signals?
* Signals allow certain senders to notify a set of receivers that some action has taken place. They’re especially useful when many pieces of code may be interested in the same events.
* For example, if we want our profile app to always create a user instance every time a profile is created, we can:
1. Run the Profile App.
2. Send a signal from Profile to User.
3. Run the Create a User Instance code.

### Step 4: Profile List View: GET and PUT:

1. Install Django Rest Framework to workspace, and add to installed_apps.
2. Create the view: ProfileList.
3. Create new urls.py file in profiles, add urls.
4. Add url to drf_api urls.

### Step 5: Create a Serializer:

1. Create serializers.py file in profiles.
2. Create ProfileSerializer.
3. Import and add serializer to ProfileList view. Note: Remember to alter the response.

* Note: Serializers allow complex data such as querysets and model instances to be converted to native Python datatypes that can then be easily rendered into JSON, XML or other content types.

### Step 6: Profile Detail View: GET and PUT Methods:

1. Create Profile GET Method in views.py
   * a. Add urls in profiles
2. Create Profile PUT method in views.py
   * a. Add urls in profiles

#### 6.1 Profile Detail View: GET Method:
   * 3 stages:
     1. fetch the profile id.
     2. serialize the Profile model instance.
     3. return serializer data in the response.

#### 6.2: Profile Detail view: PUT Method:
   * 4 stages:
     1. fetch the profile by id.
     2. call the serializer with the profile and request data.
     3. if data is valid, save and return the instance.
     4. if data is invalid, return the 400 ERROR.

### Step 7: Authentication, authorization and serializer method fields:

1. Create login/ logout button.
2. Create custom permissions.
3. Connect your custom permissions to the profile detail view.
4. Pass the request data from views.py as a context value for each method.


