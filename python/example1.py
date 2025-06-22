from tidyml.parser import TidyMLParser


if __name__ == "__main__":
    parser = TidyMLParser()

    text = '''
    users = [
      user {
        name = "Gokul"
        age = 40
        admin = true
        skills = ["python", "c++", "leadership"]
      },
      user {
        name = "Kiran"
        age = 35
        admin = false
        skills = ["go", "java"]
      }
    ]
    '''

    result = parser.parse(text)
    print(result)
