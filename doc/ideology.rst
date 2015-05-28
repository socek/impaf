=================
2. Impaf Ideology
=================

2.1 Settings
============
There are 3 types of settings:
- project settings (where settings do not change between 2 instances, but
    changes between 2 separe projects, like "project name".)
- envoritment settings (where settings change between 2 instances, like link to
    a database)
- live settings (where settings change on live produkt, for example like "do the
    advertise box should be visible?")

2.1.1 Project Settings
----------------------
Project settings should be made in the project code in the Application class.

2.1.2 Envoritment settings
--------------------------
Envoritment settings should be made by one Application method, but the method
sould be written in one file names "settings/default.py". Besides that, there
can be a "local.py" file wich will be placed on top of the "default.py" file.

2.1.3 Live Settings
-------------------
This should be optional by an external lib. This feature is not needed by all
web applications.

2.2 No more magic!
==================
Magic is when there is no simple way to find "where this method came from" or
"why this is not working". For example, there can be no naming convancon that
will automaticly add controllers or models. No dynamicly added methods.

2.2.1 What is magic?
--------------------
Magic is when you use too mutch of dynamic feature.
    - "Convencion over Configuration" is too magical, because it dynamicly adds
        models/controllers to app. If we try to understand what should be met
        to add model/controller to our app from the working code we could end
        nowhere. It's to magical because we would need to read framework
        documentation to understand.
    - Adding methods dynamicly. If we use some IDE like PyCharm it should be
        able to go to definition when the Type is known.

2.3 Classes and inheritance are good for you
============================================
All controllers should be inherit from bases controllers. New plugins should be
installed by inheriting.

2.4 SubApps should be independent
=================================
SubApps should be able to add:
 - controllers
 - routes
 - static files (like js, css, or images)
 - commands
