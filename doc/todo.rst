=======================
X. Hatak technical TODO
=======================

X.1 Application
===============
implement:
- settings
- routes


endings:
- wsgi app
- commands
- tests session (PyTest?)
- shell

X.1.1 Route
-----------
Rout class should ba a wrapper for config.add_route and add_view, and should be
able to read .yaml files for routing. All the controller values should be as
const controller values.

X.2 Controller
==============
Controller class should be center of all. It should expect request object and
RootFactory. Controller should make objects with new classes:
    - request
    - matchdict
    - template context

Controller will have helper methods:
    - redirect
    - adding static files
    - adding json data to template
    - adding templates

X.2.1 Request
-------------
Request will be inherited from pyramid Request class, and extends it. We will
not use .add_request_method and other magical methods. All new methods should
be implemented by using inheritance.

X.2.2 Matchdict
---------------
Matchdict now is a simple dict. It should be more powerfull and should be able
to transform values.

X.3 RequestAble
===============
RequestAble is a class wich have only method to assign request object, so all
RequestAble like objects will have access to request.

X.4 Model
=========
Model should be RequestAble.

X.4 MiniApps
============
All subapps should be in form of mini apps, which will inherit from application.

