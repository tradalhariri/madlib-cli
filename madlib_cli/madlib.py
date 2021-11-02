import re as regex


def printWelcome():
    print("""
    ****************************************
    ******** Welcome to MadLib Game ********
    ----------------------------------------
    - in This game you will be asked to    -
    - enter meaningful words and at the end-
    - the Matlib game will show you funny  -
    - paragraph of your chosen words       -
    ----------------------------------------
    ****************************************
    ****************************************
    """)



def read_template(path):
    try:
        with open(path, 'r') as file:
            content = file.read()
            return content
    except:
        raise FileNotFoundError
    else:
        file.close()

def parse_template(content):
    # r"\{(\w*)\}*"
    # r"\{(.*?)\}"
    languagePartsList = regex.findall(r"\{(\w*)\}*",content)
    contentWithoutLanguageParts = regex.sub(r"\{(\w*)\}*","{}",content)
    return contentWithoutLanguageParts,(*languagePartsList,)
   
def merge(bareContent,languageParts):
    return bareContent.format(*languageParts)
    
def write_template(path,content):
    with open(path,"w") as writer:
        writer.write(content)


if __name__ == "__main__":
    printWelcome()
    content = read_template("tests/assets/make_me_a_video_game_template.txt")
    contentWithoutLanguageParts,languagePartsList = parse_template(content)
    answers = []
    for word in languagePartsList:
        answer = input("Enter "+word+" : ")
        answers.append(answer)
        
    
    contentWithLanguageParts = merge(contentWithoutLanguageParts,answers)
    print()
    print("---------Your Answers-----------")
    print()
    
    print (contentWithLanguageParts)
    write_template("tests/assets/make_me_a_video_game.txt", contentWithLanguageParts)


