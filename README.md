# Introduction

Welcome, this repository is a compilation of my *pass-time projects*. Most of these will be based on python but, would try to include
projects in other languages as well!. So, I hope you enjoy & benefit from this repository, it will be open to suggestions and additions
feel free to contact me through the means below for collaborations and queries which you may have. Happy Coding!

Disclaimer: These projects are purely for educational purpose, the author [ME!] is not be held responsible for any illicit use of them.
            If you are to use the code in your projects, please give the author the due credit. This repository is distributed through 
            the [**GNU Public License v3**](https://www.gnu.org/licenses/gpl-3.0.en.html).

Discord : [Davezacofficial](https://discord.com/users/585744645862981644)

Guilded : [Davezacofficial](https://www.guilded.gg/u/davezacofficial)

Instagram : [Davezacoffical](https://www.instagram.com/davezachofficial/)

Twitter : [Davezacoffical](https://twitter.com/Davezacofficial)

## URLRequests

You might have seen this version of code in many repos, but this is my version of the same with a few minor tweaks. The following documentation specifies the language 
and libraries used to build this project.

### Language : [**Python**](https://www.python.org/)

### Libraries Used : [optparse](https://docs.python.org/3/library/optparse.html), [time](https://docs.python.org/3/library/time.html), [random](https://docs.python.org/3/library/random.html), [requests](https://requests.readthedocs.io/en/latest/)

### Usage : 

```bash
python3 urlrequests.py --link https://bit.ly/ProfileGitHub --time 25 
```
							
### Documentation 

This a project which enables you to send requests to a certain URL either at a fixed interval of time or random interval of time by using the *requests* library.
Depending on the type of URL you must specify the contents of the [*headers*](https://www.geeksforgeeks.org/http-headers/), for instance URLs from URLShorteners 
such as [*bit.ly*](https://bit.ly) require header contents as follows: 
```
'Content-Type': 'text/html',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36' 
```
but for other URLs, you may get away without specifying them. 

It also utilizes the other libraries such as *optparse*  to parse the options provided during command execution. The other libraries include
the *time* library to provide time intervals between each requests, it's a necessary evil required to prevent abuse the provided URLs. Last, but not the least it utilizes
*random* library to generate a time interval between *5-30* seconds incase the time interval is not specified.

Just a word of caution, if the time inteval is specified **manually** be sure 
to give a *minimum* of **5** seconds of time interval between each request. You can also change the *User-Agent* based on your liking. The help menu can be used as follows:

```
python3 urlrequests.py --help 

Output:
Usage: shortener.py [options]

Options:
  -h, --help            show this help message and exit
  -l LINK, --link=LINK  [Reuqired] Used to specify a link for sending requests
  -t TIME, --time=TIME  [Optional] Used to specify the time interval between
                        each request
If time is not specified, a random time interval
between 5 to 30 seconds would be selected between each request.
Example: python3 urlrequests.py --link https://bit.ly/ProfileGitHub --time 20
```

Hope you found this project useful, if you have any queries feel free to raise an issue or contact me using the above-mentioned means! 

### Future Imporvements:

- To be able to provide custom *User-Agent* via the execution command.
- Add an option for specifying a time interval for the random time-interval option.
- Further House-Keeping & Beautification of Code.

## Future Projects [Coming Soon!]

![Under Construction](https://user-images.githubusercontent.com/83908831/189478899-ce0f9de1-f24b-4118-9882-b5f6ddaab72d.png)






											 
