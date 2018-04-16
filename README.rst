==============================================================================
UnFold Django Plugin.  UnFold plugin to support payments in Django backends
==============================================================================
:Info: This is the README file for UnFold Plugin Django.
:Author: Sweyn Venderbush <sweyn.venderbush@yale.edu>
:Copyright: © 2018, Sweyn Venderbush.
:Date: 2018-05-01
:Version: 0.1.0

.. index: README

PURPOSE
-------
The UnFold plugin for Django backends allows content creators to easily integrate the UnFold payment gateway into their Django-based applications by simply annotating their article View with the UnFold decorator.

INSTALLATION
------------
To install, clone the UnFold plugin directory to your development environment. While in the virtual environment for your application, cd into the cloned directory and run::

    pip install .

You can also create a distributable Wheel of this module to include in distribution of your application. This module is not currently available via ``pip`` but is ready out of the box to be uploaded to [PyPi](https://pypi.python.org).

USAGE
-----
The plugin consists of the decorator ``unfold_required`` which can be applied to any Django View. The decorator can be imported as follows and has the header::

    from unfold_plugin import unfold_required

    @unfold_required(get_article_info)

``get_article_info`` is a function that the user must provide that returns information to the decorator about the article that the View is current attached to. The function takes all the inputs of the view itself::

    get_article_info(request, *args, **kwargs)

It returns a dictionary of information about the article in the following format::

    {
        'price': [the price you would like to charge for the article], 
        'title': [the title of the article you would like displayed to the user],
        'external_id': [the unique ID of the article that you would like to use to identify this article to UnFold]
    }

If you're using class-based Views, the `unfold_required` can be applied to your URL as follows::

    path('exampleview/', unfold_required(get_article_info)(ExampleView.as_view()))

For more information about using view decorators, see [View decorators](https://docs.djangoproject.com/en/2.0/topics/http/decorators/) and [Class-based View decorators](https://docs.djangoproject.com/en/2.0/topics/class-based-views/intro/#decorating-class-based-views).
