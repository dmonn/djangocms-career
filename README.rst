######################
DjangoCMS Career
######################

DjangoCMS Career is a plugin to easily showcase career and educational paths.
The recommended use for this plugin is on a Portfolio- or a personal CV-Website.
The plugin was initially created for - and first used by - my personal `CV-Page`_. Check it out!

.. _CV-Page: https://dmonn.ch


============
Installation
============

This plugin requires `django CMS` 3.0.2+ or higher to be properly installed.

* In your projects `virtualenv`, run ``pip install djangocms-career``.
* Add ``djangocms_career`` to your ``INSTALLED_APPS`` (the order does not matter).
* Run ``manage.py migrate djangocms_career``.

=====
Usage
=====

DjangoCMS Career is a CMS- *Plugin*, which means, you can only use it in the frontend editing mode.
In an available placeholder, just choose a *Career Container Plugin* and use the 'Plus'-Sign to add Positions to it.

=========
Run tests
=========

You can run tests via ``manage.py test djangocms_career``

============
Contributing
============

This is a community project. We love to get any feedback in the form of
`issues`_ and `pull requests`_.

.. _issues: https://github.com/dmonn/djangocms-career/issues
.. _pull requests: https://github.com/dmonn/djangocms-career/pulls




