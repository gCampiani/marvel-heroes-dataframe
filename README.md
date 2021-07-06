# marvel-heroes-dataframe

![Image of Marvel Logo](https://www.logosurfer.com/wp-content/uploads/2018/03/marvel-logo_0.png)

Python 3.8.6rc1

A simple program to extract some cool features about Marvel Characters using requests and pandas

## Necessary environment vars

It's only necessary the API keys for this exercise, but i still recommend the use of a .env file

```bash
PUBLIC_API_KEY
PRIVATE_API_KEY
CHARACTERS_URL
```

## Initial configuration

First we need to install pipenv and open it's shell, which will automatically download all dependencies and create a complete virtual environment

```bash
pip install pipenv
python -m pipenv shell
```

## Execution

Just execute main to create your .csv

```bash
python app/main.py <limit>
```

limit must be between 0 and 100 or it will just take 100 as a default value

## Conclusion

Cool exercise for testing some request with limit, offset and a necessary md5 hash
