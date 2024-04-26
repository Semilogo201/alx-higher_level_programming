
#!/usr/bin/python3
"""A script that
- fetches https://alx-intranet.hbtn.io/status.
- uses urlib package
"""


if __name__ == '__main__':
    import urllib.request

<<<<<<< HEAD
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))

=======
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        content = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))
>>>>>>> e853db45163e08c19ffbfad29d802f8e874b582e
