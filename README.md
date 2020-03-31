# Calligraphy Evaluation Backend Service

## Overview
Calligraphy Evaluation Backend Service, aka CE_Backend, is the API and content management service of Calligraphy Evaluation service. Using django auth system to handle user accounts, groups, permissions and cookie-based user sessions. In case of API systems, token-based authentication is used.

### Known Issues
- Server errors when handling invalid inputs from client.

### Main Structure
Web service framework: [Django](https://github.com/django/django)

### Features
- Using REST API to provide interactive features.
- User-friendly overall model sets management application.



## Requirements
Python >= 3.7

### Dependencies

**All dependencies should be pre-installed in running environment.**

A highly version of the package will still work in theory, but it's not been tests.

| Package                | Recommend Version |
| ---------------------- | ------------------ |
| Django                 | 3.0.3              |
| django-admin           | 2.0.0              |
| django-excel-response2 | 2.0.8              |
| djangorestframework    | 3.11.0             |



## Usage

```
$ [python environment path] manage.py runserver [port]
```
Examples
```bash
Linux & macOS
$ python3 manage.py runserver 8000

Windows
$ python manage.py runserver 8000
```



## Applications

The project is comprised of the following apps.

### Evaluation API
**Endpoint path**: `/api`

**Config**:
- Serializers: `/eva/serializers.py`
- Views (ex. Standard data sets): `/eva/views`
- Standard data sets: `/eva/view_data.py` 

### Content Management Portal
**Endpoint path**: `/admin`

**Config**: `/eva/admin.py`

**Documents**: [The Django admin site](https://docs.djangoproject.com/en/3.0/ref/contrib/admin/)




## API Reference
[API Reference at wiki](https://github.com/aqutor/CE_Backend/wiki/API-Reference).




## Contribution
Please use *issues* on Github.com properly. To resolve every issue, you should include **all details** that would *possibly* affect the result of the product. It's an awesome practice if you use the template provided on the issues page and fill out all necessary sections.




## License

[The MIT License](http://opensource.org/licenses/MIT)

Copyright (c) 2020 Zhou Aotian <[https://io.airscr.com/](https://io.airscr.com/)>
