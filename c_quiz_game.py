quiz = {
    "What does CPU stand for?": "Central Processing Unit",
    "What does RAM stand for?": "Random Access Memory",
    "What does ROM stand for?": "Read-Only Memory",
    "What does HDD stand for?": "Hard Disk Drive",
    "What does SSD stand for?": "Solid State Drive",
    "What does GPU stand for?": "Graphics Processing Unit",
    "What does BIOS stand for?": "Basic Input/Output System",
    "What does USB stand for?": "Universal Serial Bus",
    "What does LAN stand for?": "Local Area Network",
    "What does WAN stand for?": "Wide Area Network",
    "What does WLAN stand for?": "Wireless Local Area Network",
    "What does HTTP stand for?": "Hypertext Transfer Protocol",
    "What does HTTPS stand for?": "Hypertext Transfer Protocol Secure",
    "What does URL stand for?": "Uniform Resource Locator",
    "What does HTML stand for?": "Hypertext Markup Language",
    "What does CSS stand for?": "Cascading Style Sheets",
    "What does JavaScript stand for?": "JavaScript Object Notation",
    "What does AJAX stand for?": "Asynchronous JavaScript and XML",
    "What does API stand for?": "Application Programming Interface",
    "What does IP stand for?": "Internet Protocol",
    "What does TCP stand for?": "Transmission Control Protocol",
    "What does UDP stand for?": "User Datagram Protocol",
    "What does DNS stand for?": "Domain Name System",
    "What does FTP stand for?": "File Transfer Protocol",
    "What does SMTP stand for?": "Simple Mail Transfer Protocol",
    "What does POP stand for?": "Post Office Protocol",
    "What does IMAP stand for?": "Internet Message Access Protocol",
    "What does CPU cache stand for?": "Central Processing Unit cache",
    "What does RFID stand for?": "Radio-Frequency Identification",
    "What does JSON stand for?": "JavaScript Object Notation",
    "What does XML stand for?": "Extensible Markup Language",
    "What does SQL stand for?": "Structured Query Language",
    "What does IDE stand for?": "Integrated Development Environment",
    "What does SSL stand for?": "Secure Sockets Layer",
    "What does TLS stand for?": "Transport Layer Security",
    "What does ASCII stand for?": "American Standard Code for Information Interchange",
    "What does HTML5 stand for?": "Hypertext Markup Language version 5",
    "What does CSS3 stand for?": "Cascading Style Sheets version 3",
    "What does MVC stand for?": "Model View Controller",
    "What does AI stand for?": "Artificial Intelligence",
    "What does ML stand for?": "Machine Learning",
    "What does DL stand for?": "Deep Learning",
    "What does CLI stand for?": "Command Line Interface",
    "What does VM stand for?": "Virtual Machine",
    "What does XSS stand for?": "Cross-site Scripting",
    "What does CSRF stand for?": "Cross-site Request Forgery",
    "What does SQLi stand for?": "SQL Injection",
    "What does IoT stand for?": "Internet of Things",
    "What does BIOS stand for?": "Basic Input/Output System",
    "What does NLP stand for?": "Natural Language Processing",
    "What does CNN stand for?": "Convolutional Neural Network",
    "What does HDD stand for?": "Hard Disk Drive",
    "What does SSD stand for?": "Solid State Drive",
    "What does GPU stand for?": "Graphics Processing Unit",
    "What does BIOS stand for?": "Basic Input/Output System",
    "What does USB stand for?": "Universal Serial Bus",
    "What does LAN stand for?": "Local Area Network",
    "What does WAN stand for?": "Wide Area Network",
    "What does WLAN stand for?": "Wireless Local Area Network",
    "What does HTTP stand for?": "Hypertext Transfer Protocol",
    "What does HTTPS stand for?": "Hypertext Transfer Protocol Secure",
    "What does URL stand for?": "Uniform Resource Locator",
    "What does HTML stand for?": "Hypertext Markup Language",
    "What does CSS stand for?": "Cascading Style Sheets",
    "What does JavaScript stand for?": "JavaScript Object Notation",
    "What does AJAX stand for?": "Asynchronous JavaScript and XML",
    "What does API stand for?": "Application Programming Interface",
    "What does IP stand for?": "Internet Protocol",
    "What does TCP stand for?": "Transmission Control Protocol",
    "What does UDP stand for?": "User Datagram Protocol",
    "What does DNS stand for?": "Domain Name System",
    "What does FTP stand for?": "File Transfer Protocol",
    "What does SMTP stand for?": "Simple Mail Transfer Protocol",
    "What does POP stand for?": "Post Office Protocol",
    "What does IMAP stand for?": "Internet Message Access Protocol",
    "What does CPU cache stand for?": "Central Processing Unit cache",
    "What does RFID stand for?": "Radio-Frequency Identification",
    "What does JSON stand for?": "JavaScript Object Notation",
    "What does XML stand for?": "Extensible Markup Language",
    "What does SQL stand for?": "Structured Query Language",
    "What does IDE stand for?": "Integrated Development Environment",
    "What does SSL stand for?": "Secure Sockets Layer",
    "What does TLS stand for?": "Transport Layer Security",
    "What does ASCII stand for?": "American Standard Code for Information Interchange",
    "What does HTML5 stand for?": "Hypertext Markup Language version 5",
    "What does CSS3 stand for?": "Cascading Style Sheets version 3",
    "What does MVC stand for?": "Model View Controller",
    "What does AI stand for?": "Artificial Intelligence",
    "What does ML stand for?": "Machine Learning",
    "What does DL stand for?": "Deep Learning",
    "What does CLI stand for?": "Command Line Interface",
    "What does VM stand for?": "Virtual Machine",
    "What does XSS stand for?": "Cross-site Scripting",
    "What does CSRF stand for?": "Cross-site Request Forgery",
    "What does SQLi stand for?": "SQL Injection",
    "What does IoT stand for?": "Internet of Things"
}

################################################################################################################


print("Welcome to my Computer Quiz !!")

playing = input("Do you want to play? ")

def play():
    print("Okay! Let's play :) ")
    score = 0
    for question, answer in quiz.items():
        user_answer = input(question + " ")
        if user_answer.lower() == answer.lower():
            print("Correct!!")
            score += 1
            print(f"Score: {score}")
        else:
            print("Incorrect!")
            print(f" your score is {score}")
            play_again = input("Do you wanna restart again? ")
            if play_again == "yes":
                play()
            else:
                quit()

if playing == "yes":
    play()
else:
    quit()






















































































































































































