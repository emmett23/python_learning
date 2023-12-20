#
# Example file for retrieving data from the internet
# LinkedIn Learning Python course by Joe Marini
#
import urllib.request  # instead of urllib2 like in Python 2.7


def main():
    # open a connection to a URL using urllib2
    weburl = urllib.request.urlopen("http://www.google.com")
    print("result code: " + str(weburl.getcode()))

    data = weburl.read()  # read the data from the URL and print it
    print(data)


if __name__ == "__main__":
    main()
